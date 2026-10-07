import torch
import torch.nn as nn

class AcousticModel(nn.module):
    def __init__(self, input_dim=13, hidden_dim=128, output_dim=29, num_layers=2)