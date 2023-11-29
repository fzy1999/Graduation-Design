import torch

# 创建一个张量并设置 requires_grad=True，表示需要计算梯度
x = torch.tensor(2.0, requires_grad=True)

# 定义一个函数 y = x^2
y = x**2

# 自动计算梯度
y.backward(torch.tensor(4.0))

# 打印梯度
print(x.grad)
