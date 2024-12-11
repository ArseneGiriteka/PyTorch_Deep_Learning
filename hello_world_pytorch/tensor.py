from random import random

import torch

TENSOR = torch.tensor([[[1, 2, 3], [4, 5, 6], [7, 8, 9]]])

print(TENSOR)
print(f"nDim: {TENSOR.ndim}")
print(f"Shape is: {TENSOR.shape}")

# Create random tensor
random_tensor = torch.rand(2, 4)
print(f"my random tensor(2, 4): {random_tensor}")
print(f"random_tensor.ndim = {random_tensor.ndim}")

random_tensor = torch.rand(10, 10, 10)
print(f"my random tensor(10, 10, 10): {random_tensor}")
print(f"random_tensor.ndim = {random_tensor.ndim}")
print(f"dtype is :{random_tensor.dtype}")

def create_random_image():
    random_image_size_tensor = torch.rand(size=(3, 224, 224)) #hieght, width, color chanel(R, G, B)