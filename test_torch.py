import torch

def test_torch():
    print("PyTorch version:", torch.__version__)
    print("CUDA available:", torch.cuda.is_available())

if __name__ == "__main__":
    test_torch()
