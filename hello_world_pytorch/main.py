import torch

# Create a tensor
x = torch.tensor([[1, 2], [3, 4]])
print("Tensor x:\n", x)

# Perform a tensor operation
y = x + 5
print("Tensor y:\n", y)

# Check GPU
if torch.cuda.is_available():
    device = torch.device("cuda")
    z = x.to(device)  # Move tensor to GPU
    print("Tensor z on GPU:\n", z)
else:
    print("CUDA not available. Running on CPU.")
