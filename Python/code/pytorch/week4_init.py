import torch
from torch import nn

#
# input = torch.tensor([2,3,4,5,6,7],dtype=torch.float)
# input.add_(0)
# # out = input*input
#
# print(input.std()/out.std())
# gain = nn.init.calculate_gain('sigmoid')
# print(gain)

w = torch.empty(10, 5)
nn.init.sparse_(w, sparsity=0.1)

print(w)

