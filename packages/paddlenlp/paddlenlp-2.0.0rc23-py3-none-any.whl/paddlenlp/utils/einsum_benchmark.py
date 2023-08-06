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
    "--shape",
    default="base",
    type=str,
    choices=['large', 'base'])

args = parser.parse_args()
paddle.set_device(args.device)

def torch_einsum(eqn, *operands):
    if args.device == 'gpu':
        device = torch.device('cuda:0')
    else:
        device = torch.device(args.device)
    torch_operands = [torch.tensor(x, device=device, requires_grad=True) for x in operands]

    forward_elapsed = 0
    backward_elapsed = 0
    for i in range(0, args.epochs):
        start = time.perf_counter()
        forward_result = torch.einsum(eqn, *torch_operands)
        forward_elapsed += time.perf_counter() - start

        if len(forward_result.shape) == 0:
            start = time.perf_counter()
            forward_result.backward()
            backward_elapsed += time.perf_counter() - start
        else:
            start = time.perf_counter()
            forward_result.sum().backward()
            backward_elapsed += time.perf_counter() - start

    torch.cuda.synchronize()
    backward_result = [x.grad for x in torch_operands]
    del torch_operands
    del backward_result 
    del forward_result
    backward_result = forward_result = None
    return forward_result, backward_result, forward_elapsed, backward_elapsed

def paddlenlp_einsum(eqn, *operands):
    paddle_operands = [paddle.to_tensor(x, stop_gradient=False) for x in operands]

    forward_elapsed = 0
    backward_elapsed = 0
    for i in range(0, args.epochs):
        start = time.perf_counter()
        forward_result = ops.einsum(eqn, *paddle_operands)
        forward_elapsed += time.perf_counter() - start

        if len(forward_result.shape) == 0:
            start = time.perf_counter()
            forward_result.backward()
            backward_elapsed += time.perf_counter() - start
        else:
            start = time.perf_counter()
            forward_result.sum().backward()
            backward_elapsed += time.perf_counter() - start

    _ = forward_result.numpy() # for synchronize
    backward_result = [x.grad for x in paddle_operands]
    del paddle_operands
    del backward_result 
    del forward_result
    backward_result = forward_result = None
    return forward_result, backward_result, forward_elapsed, backward_elapsed

def test_einsum_performace(shape=(5, 7, 3, 2, 9, 11, 13, 4, 10, 20, 30)):
    x = np.random.rand(shape[0]).astype(args.dtype)
    y = np.random.rand(shape[1]).astype(args.dtype)
    A = np.random.rand(shape[2], shape[0]).astype(args.dtype)
    B = np.random.rand(shape[3], shape[0]).astype(args.dtype)
    C = np.random.rand(shape[3], shape[2], shape[0]).astype(args.dtype)
    D = np.random.rand(shape[3], shape[0], shape[1]).astype(args.dtype)
    E = np.random.rand(shape[1], shape[4]).astype(args.dtype)
    F = np.random.rand(shape[3], shape[2], shape[0], shape[1]).astype(args.dtype)
    G = np.random.rand(shape[1], shape[5], shape[6]).astype(args.dtype)
    H = np.random.rand(shape[7], shape[7]).astype(args.dtype)
    I = np.random.rand(shape[2], shape[7], shape[7]).astype(args.dtype)
    l = np.random.rand(shape[0], shape[8]).astype(args.dtype)
    r = np.random.rand(shape[0], shape[9]).astype(args.dtype)
    w = np.random.rand(shape[10], shape[8], shape[9]).astype(args.dtype)
    
    test_list = [
        # -- Vector
        ("i->", x),                 # sum
        ("i,i->", x, x),            # dot
        ("i,i->i", x, x),           # vector element-wise mul
        ("i,j->ij", x, y),          # outer
        # -- Matrix
        ("ij->ji", A),              # transpose
        ("ij->j", A),               # row sum
        ("ij->i", A),               # col sum
        ("ij,ij->ij", A, A),        # matrix element-wise mul
        ("ij,j->i", A, x),          # matrix vector multiplication
        ("ij,kj->ik", A, B),        # matmul
        ("ij,ab->ijab", A, E),      # matrix outer product
        # -- Tensor
        ("aij,ajk->aik", C, D),     # batch matmul
        ("ijk,jk->i", C, A),        # tensor matrix contraction
        ("aij,jk->aik", D, E),      # tensor matrix contraction
        ("abcd,dfg->abcfg", F, G),  # tensor tensor contraction
        ("ijk,jk->ik", C, A),       # tensor matrix contraction with double indices
        ("ijk,jk->ij", C, A),       # tensor matrix contraction with double indices
        ("ijk,ik->j", C, B),        # non contiguous
        ("ijk,ik->jk", C, B),       # non contiguous with double indices
        # -- Ellipsis
        ("i...->...", H),
        ("ki,...k->i...", A.T, B),
        ("k...,jk", A.T, B),
        # -- Other
        ("bn,anm,bm->ba", l, w, r),  # as torch.bilinear
    ]
    for num, test in enumerate(test_list):
        torch_result = torch_einsum(test[0], *test[1:])
        torch.cuda.empty_cache()
        paddle_result = paddlenlp_einsum(test[0], *test[1:])
        print("=========================={}=================================".format(num), flush=True)
        print("paradigm: {} shape: {}".format(test[0], " | ".join([str(x.shape) for x in test[1:]])), flush=True)
        # print("forward equal: {}".format(np.allclose(torch_result[0].cpu().detach().numpy(), paddle_result[0].numpy())), flush=True)
        # for i in range(len(torch_result[1])):
        #    print("gradient of {} equal: {}".format(i, np.allclose(torch_result[1][i].cpu().numpy(), paddle_result[1][i])), flush=True)
        print("torch: forward={}s, backward={}s".format(torch_result[2], torch_result[3]), flush=True)
        print("paddle: forward={}s, backward={}s".format(paddle_result[2], paddle_result[3]), flush=True)
        print("Forward time ratio: paddle/torch = {}.".format(paddle_result[2]/torch_result[2]), flush=True)
        print("Backward time ratio: paddle/torch = {}.".format(paddle_result[3]/torch_result[3]), flush=True)
        print("===========================================================", flush=True)

if __name__ == "__main__":
    base_shape = (5, 7, 3, 2, 9, 11, 13, 4, 10, 20, 30)
    large_shape = (512, 768, 8, 4, 256, 11, 3, 512, 128, 64, 256)
    # small shape
    if args.shape == "base":
        test_einsum_performace(base_shape)

    # large shape
    if args.shape == "large":
        test_einsum_performace(large_shape)