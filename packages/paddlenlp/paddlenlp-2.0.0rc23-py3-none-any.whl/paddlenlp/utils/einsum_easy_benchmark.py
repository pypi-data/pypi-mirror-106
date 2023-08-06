import paddle
import paddlenlp.utils.ops as ops
import torch
import time
import numpy as np

def torch_einsum(x, y, epochs, device='gpu'):
    if device == 'gpu':
        tdevice = torch.device('cuda:0')
    else:
        tdevice = torch.device('cpu')
    tx = torch.tensor(x, device=tdevice, requires_grad=True) 
    ty = torch.tensor(y, device=tdevice, requires_grad=True) 
    start = time.perf_counter()
    for i in range(0, epochs):
        result = torch.einsum("abc,cde->adbe", tx, ty)
        result.sum().backward()

    torch.cuda.synchronize()
    elapsed = time.perf_counter() - start
    print('torch spends {} s/epochs'.format(elapsed/epochs))
    return tx.grad, ty.grad

def paddlenlp_einsum(x, y, epochs, device='gpu'):
    paddle.set_device(device)
    px = paddle.to_tensor(x, stop_gradient=False)
    py = paddle.to_tensor(y, stop_gradient=False)
    start = time.perf_counter()
    for i in range(0, epochs):
        result = ops.einsum('abc,cde->adbe', px, py)
        result.sum().backward()
    presult = result.numpy()
    elapsed = time.perf_counter() - start
    print('paddlenlp spends {} s/epochs'.format(elapsed/epochs))
    return px.grad, py.grad

def linear3d_opt(input, weight):
    B, T, D = input.shape
    H = 12
    weight = paddle.reshape(weight, (D, D))
    result = paddle.matmul(input, weight)
    result = paddle.reshape(result, [B, T, H, -1])
    result = paddle.transpose(result, [0, 2, 1, 3])
    return result

def linear3d(input, weight):
    B, T, D = input.shape
    H = 12
    reshape_input = paddle.unsqueeze(input, 1)
    reshape_w = paddle.reshape(weight, [D, H, D // H])
    reshape_w = paddle.transpose(reshape_w, [1, 0, 2])
    reshape_w = paddle.unsqueeze(reshape_w, 0)
    result = paddle.matmul(reshape_input, reshape_w)
    return result

def paddlenlp_linear3d(x, y, epochs, device='gpu', opt=True):
    paddle.set_device(device)
    px = paddle.to_tensor(x)
    py = paddle.to_tensor(y)
    if opt:
        linear = linear3d_opt
    else:
        linear = linear3d
    start = time.perf_counter()
    for i in range(0, epochs):
        result = linear(px, py)
    presult = result.numpy()
    elapsed = time.perf_counter() - start
    print('paddlenlp linear3d spends {} s/epochs. opt = {}'.format(elapsed/epochs, opt))


x = np.random.rand(8, 3072, 768).astype('float32')
y = np.random.rand(768, 12, 64).astype('float32')
epochs = 10000
device = 'gpu'

# paddlenlp_linear3d(x, y, epochs, device)
# paddlenlp_linear3d(x, y, epochs, device, False)
tdx, tdy = torch_einsum(x, y, epochs, device)
pdx, pdy = paddlenlp_einsum(x, y, epochs, device)
