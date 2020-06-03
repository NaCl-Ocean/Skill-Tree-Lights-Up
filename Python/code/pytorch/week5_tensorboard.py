import torch
from torch.utils.tensorboard import SummaryWriter


writer = SummaryWriter(log_dir='test_log',comment='test tensoroard')
for x in range(100):
    writer.add_scalar('y=2x',x*2,x)
    writer.add_scalar('y=pow(x,2)',x**2,x)

writer.close()