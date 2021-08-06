import torch
from torch import nn

loss = nn.CrossEntropyLoss()
input = torch.randn(3, 9, requires_grad=True)
print(input)
target = torch.empty(3, dtype=torch.long).random_(5)
print(target)
output = loss(input, target)
print(output)