import torch

TENSOR = torch.tensor([[[1, 2, 3], [4, 5, 6], [7, 8, 9]]])

print(TENSOR)
print(f"nDim: {TENSOR.ndim}")
print(f"Shap is: {TENSOR.shape}")