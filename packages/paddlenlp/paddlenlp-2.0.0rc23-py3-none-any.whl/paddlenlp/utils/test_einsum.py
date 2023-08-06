import paddle
import paddlenlp.utils.ops as ops
import torch
import time
import numpy as np
import argparse
from paddlenlp.utils.log import logger

parser = argparse.ArgumentParser()
parser.add_argument(
    "--device",
    default="gpu",
    type=str,
    choices=['gpu', 'cpu'])

parser.add_argument(
    "--dtype",
    default="float32",
    type=str,
    choices=['float32', 'float64'])

parser.add_argument(
    "--epochs",
    default=10000,
    type=int)

parser.add_argument(
    "--test_backward",
    default=0,
    type=int,
    choices=[0,1])

args = parser.parse_args()
paddle.set_device(args.device)

def torch_einsum(eqn, *operands):
    if args.device == 'gpu':
        device = torch.device('cuda:0')
    else:
        device = torch.device(args.device)
    torch_operands = [torch.tensor(x, device=device, requires_grad=True) for x in operands]

    start = time.perf_counter()
    for i in range(0, args.epochs):
        forward_result = torch.einsum(eqn, *torch_operands)
        if args.test_backward != 0:
            if len(forward_result.shape) == 0:
                forward_result.backward()
            else:
                forward_result.sum().backward()
    torch.cuda.synchronize()
    elapsed = time.perf_counter() - start
    return elapsed

def paddlenlp_einsum(eqn, *operands):
    paddle_operands = [paddle.to_tensor(x, stop_gradient=False) for x in operands]

    start = time.perf_counter()
    for i in range(0, args.epochs):
        forward_result = ops.einsum(eqn, *paddle_operands)
        if args.test_backward != 0:
            if len(forward_result.shape) == 0:
                forward_result.backward()
            else:
                forward_result.sum().backward()
    _ = forward_result.numpy() # for synchronize
    elapsed = time.perf_counter() - start
    return elapsed

def test_einsum_performace(shapes):
    A, B, C, D, l, w, r = [np.random.rand(*x).astype(args.dtype) for x in shapes]
    test_list = [
        ("abc,dce->adbe", A, B), 
        ("abcd,dfg->abcfg", C, D),  # tensor tensor contraction
        ("bn,anm,bm->ba", l, w, r),  # as torch.bilinear
    ]
    for num, test in enumerate(test_list):
        torch_result = torch_einsum(test[0], *test[1:])
        torch.cuda.empty_cache()
        paddle_result = paddlenlp_einsum(test[0], *test[1:])
        print("=========================={}=================================".format(num), flush=True)
        print("paradigm: {} shape: {}".format(test[0], " | ".join([str(x.shape) for x in test[1:]])), flush=True)
        print("torch spends {}ms/epochs".format(torch_result * 1000 / args.epochs), flush=True)
        print("paddle spends {}ms/epochs".format(paddle_result * 1000 / args.epochs), flush=True)
        print("Time ratio: paddle/torch = {}.".format(paddle_result/torch_result), flush=True)
        print("===========================================================", flush=True)

if __name__ == "__main__":
    base_shapes = (5, 7, 3, 2, 9, 11, 13, 4, 10, 20, 30)
    large_shapes = (512, 768, 8, 4, 256, 11, 1024, 512, 128, 64, 256)
    all_test_shapes = {
        # A, B, C, D, l, r, w
        "1e4": [[10, 7, 3], [6, 3, 8], [5, 7, 3, 8], [8, 4, 9], [2, 4], [3, 4, 5], [2, 5]],
        "1e7": [[10, 70, 30], [60, 30, 8], [5, 7, 30, 8], [8, 40, 90], [20, 40], [30, 40, 5], [20, 5]],
        "1e10": [[100, 70, 30], [600, 30, 80], [50, 70, 30, 80], [80, 40, 90], [200, 40], [300, 40, 50], [200, 50]],
    }
    for magnitude, shapes in all_test_shapes.items():
        print("Computational magnitude: ", magnitude, flush=True)
        test_einsum_performace(shapes)