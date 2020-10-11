from torch.utils.data import DataLoader
import torch
import matplotlib
from PIL import Image
import glob
import os
import torchvision.transforms as transforms
import numpy as np
torch.nn.Mo
class RMB_Dataset():
    def __init__(self,dir):
        dog_dir = os.path.join(dir,'dogs')
        cat_dir = os.path.join(dir,'cats')
        self.image_path = glob.glob(dog_dir+'/*.jpg') + glob.glob(cat_dir+'/*.jpg')

        self.tranform = transforms.Compose([
            transforms.ToTensor(),
            transforms.RandomErasing()])
    def __len__(self):
        return len(self.image_path)
    def __getitem__(self, item):
        img_origin = Image.open(self.image_path[item])
        img_transform = self.tranform(img_origin)
        img_origin = transforms.ToTensor()(img_origin)
        label = os.path.basename(self.image_path[item]).split('.')[0]
        return img_origin,img_transform


train_dataset = RMB_Dataset('../dogs-vs-cats/train')
b = train_dataset[[0,2]]
train_dataloader = DataLoader(train_dataset)
for i,data in enumerate(train_dataloader):
    img_origin,img_transform = data
    img_origin = torch.squeeze(img_origin)
    img_origin = torch.transpose(img_origin,0,1).transpose(1,2)
    img_origin = (np.array(img_origin)*255).astype('uint8')
    img_origin = Image.fromarray(img_origin)
    img_origin.show()
    img_transform = torch.squeeze(img_transform)
    img_transform = torch.transpose(img_transform, 0, 1).transpose(1, 2)
    img_transform = (np.array(img_transform) * 255).astype('uint8')
    img_transform = Image.fromarray(img_transform)
    img_transform.show()
