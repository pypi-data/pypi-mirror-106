from torch import nn
import torch
from torch.distributions.normal import Normal

class Cloak(nn.Module):
    def __init__(self, input_shape=[32, 3, 224, 224]):
        super().__init__()

        self.given_shape = input_shape[1:]

        self.threshold_value = 1.0

        self.locs = torch.nn.Parameter(torch.zeros(input_shape[1:]))
        self.rhos = torch.nn.Parameter(torch.ones(input_shape[1:]) * -4)

        # Normal Distribution buffers
        self.register_buffer("loc", torch.tensor(0.))
        self.register_buffer("scale", torch.tensor(1.))

        self.min_scale = 0.0001
        self.max_scale = 2.0

        self.rhos.requires_grad = False
        self.locs.requires_grad = False

    def print_locs(self):
        print(self.locs)

    def print_rhos(self):
        print(self.rhos)

    def forward(self, x):
        std = (1.0 +torch.tanh(self.rhos))/2*(self.max_scale-self.min_scale) +self.min_scale
        mask = (std < self.threshold_value).float()
        data = x + std * Normal(self.loc, self.scale).sample(self.given_shape)

        x = torch.clamp(
                data * mask + torch.min(x) * (1 - mask) + self.locs,
                torch.min(x),
                torch.max(x)
            )

        return x
