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

        self.normal_distribution = Normal(self.loc, self.scale)

    def print_locs(self):
        print(self.locs)

    def print_rhos(self):
        print(self.rhos)

    def to(self, *args, **kwargs):
        self = super().to(*args, **kwargs)
        self.normal_distribution = Normal(self.loc.to(*args, **kwargs), self.scale.to(*args, **kwargs))
        return self

    def forward(self, x):
        std = (1.0 +torch.tanh(self.rhos))/2*(self.max_scale-self.min_scale) +self.min_scale
        mask = (std < self.threshold_value).float()
        data = x + std * self.normal_distribution.sample(self.given_shape)

        x = torch.clamp(
                data * mask + 0 * (1 - mask) + self.locs,
                0,
                1
            )

        return x
