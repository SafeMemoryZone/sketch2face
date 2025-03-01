# Test if torch is supporting CUDA (crucial for this model) 

import torch

if torch.cuda.is_available():
    print("CUDA available")
    print("CUDA device count: ", torch.cuda.device_count())
    print("CUDA active device name: ", torch.cuda.get_device_name(torch.cuda.current_device()))
    print("torch version: ", torch.__version__)

else:
    print("CUDA not available")
    print("torch version: ", torch.__version__)