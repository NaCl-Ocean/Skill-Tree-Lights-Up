import torch
from torch.utils.tensorboard import SummaryWriter



def forward_hook(module,input,output ):
    fmap.append(input)

fmap = list()