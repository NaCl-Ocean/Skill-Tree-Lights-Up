import torch
from torch import optim
from torch import nn
# w_4 = torch.tensor([1,2,3])
# w_3 = torch.tensor([1,2,3])
# sgd = optim.SGD([w_4,w_3],lr=0.1)
# w_2 = torch.tensor([1,2,3])
# sgd.add_param_group({'params':w_2,'lr':0.01})
#
# state_dict = torch.load('test.pkl')
# print(sgd.state_dict())
# sgd.load_state_dict(state_dict)
# print(sgd.state_dict())

net = nn.Module