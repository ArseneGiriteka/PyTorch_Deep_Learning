import torch

scalar = torch.tensor(89)
print(scalar)
print(f"the dimension of {scalar} is {scalar.ndim} and the shape is {scalar.shape} and the value associated is {scalar.item()} and its data is {scalar.data}")

vector = torch.tensor([2, 7])

print(f"{vector} dimension is {vector.ndim} and the shape is {vector.shape} and its data is {vector.data}")

matrix = torch.tensor([[1, 0], [0, 1]])

print(f"{matrix} has dimension of {matrix.ndim} and the shape is {matrix.shape} and its data is {matrix.data}")
