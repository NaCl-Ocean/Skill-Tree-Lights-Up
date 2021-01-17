# 数据类型的转换

## * / tensor

`torch.tensor(data, dtype, device, requires_grad,pin_memory)`

- 可以用于将下面涉及到的所有数据类型转换为tensor，eg:list to tensor，ndarray to tensor, scalar to tensor
- 进行了data的copy，返回的tensor与原数据不共享内存，需要指定数据类型



## tensor / ndarray

- tensor to numpy `tensor.numpy()`
- numpy to tensor `torch.from_numpy(np.ndarray)`
  - 上述两种转换得到的tensor/ndarray 与原ndarray/tensor共享内存，数据类型一致

## tensor / python

注：python中基本数据类型，主要指number与list

- `tensor.item()`  tensor中只有一个元素，转换为python中的标准number数据类型（int，float）
- `tensor.tolist()` tensor中有多个元素，转换为list（若tensor为多维，则转换为嵌套list）
- `torch.tensor(list or scalar, dtype, device, requires_grad)` list 或者 tensor转为tensor  



## tensor / cv2

注：这里的tensor指 H\*W\*C，RGB，数据类型为torch.float32，归一化到0-1之间的tensor

- tensor to cv2

  ```
  image = image.mul(255).clamp(0, 255).to(torch.uint8)
  image = image.permute((1, 2, 0))
  image = image.numpy()
  image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
  ```

- cv2 to tensor

  ```python
  div_num = 2**8 - 1
  img = img[:, :, ::-1].transpose(2, 0, 1)  # BGR to RGB, channel last to channel first
  img = np.ascontiguousarray(img)
  img = torch.from_numpy(img)
  ```





## PIL.image / cv2

注：cv2读进来的图以numpy.ndarray来表示，因此不包含任何关于图像格式的信息，默认读进来的格式为BGR，显示的时候也只会以BGR的格式来显示，因此在显示时如果ndarray不是按照BGR的格式来存的话，显示的图片颜色就乱掉了。PIL.image可以包含关于图像格式的信息（mode），在显示的时候会根据mode来进行相应的显示。默认为RGB mode

- **cv2 to PIL.image** `PIL.image.fromarray(numpy.ndarray, mode)` 
  - 这里的mode需要根据此时numpy.ndarray存储图像的格式来设置，如RGB，RGBA，L等等，默认为RGB
  - 注：这里mode不包括BGR，因此如果ndarray是BGR格式的话，需要先利用cv2.cvtcolor转换一下
  - [PILimage support mode](https://pillow.readthedocs.io/en/latest/handbook/concepts.html#concept-modes)
- **PIL.image to cv2**  `cv2.cvtcolor(numpy.asarray(image),cv2.COLOR_RGB2BGR)`

## tensor / PIL.image

- tensor to PIL.image `torchvision.transforms.ToPILimage()(tensor)` 
  - tensor的类型为 C\*H\*W，float，归一化到0-1
  - 这里ToPILimage做的事情其实还是将tensor转换为cv2，之后将cv2转换为了PILimage

