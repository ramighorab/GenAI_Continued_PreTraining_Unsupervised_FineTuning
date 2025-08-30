import torch

# Use this to check if your machine (e.g. Mac Laptop) supports CUDA and would have VRAM

print("CUDA available:", torch.cuda.is_available())
print("Device:", torch.cuda.current_device() if torch.cuda.is_available() else "CPU")
print("CUDA device count:", torch.cuda.device_count())
print("Device name:", torch.cuda.get_device_name(0) if torch.cuda.is_available() else "No CUDA device")
print("Available memory:",
      torch.cuda.get_device_properties(0).total_memory if torch.cuda.is_available() else "No CUDA device")


# Use this to check if your machine (e.g. Mac Laptop) supports Metal Performance Shaders

print("MPS available:", torch.backends.mps.is_available())
