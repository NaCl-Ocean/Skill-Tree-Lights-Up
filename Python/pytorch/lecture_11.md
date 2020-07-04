# 分布式训练

- 本文特指`torch.distribute.DistributedParallel`（单机多卡）
- `group`
  - 即进程组。默认情况下，只有一个组，一个 `job` 即为一个组，也即一个 `world`。
- `world size`
  - 全局进程数
- `rank`
  - 进程号，`rank = 0` 的主机为 `master` 节点。
- `local_rank`
  - 当前进程使用的`GPU` 编号，非显式参数，由 `torch.distributed.launch` 内部指定，
- 实现的方法
  - 在每次迭代中，**每个进程具有自己的 `optimizer`** ，并独立完成所有的优化步骤，进程内与一般的训练无异。
  - 在各进程梯度计算完成之后，各进程需要将梯度进行汇总平均，然后再由 **`rank=0` 的进程**，将其 `broadcast` 到所有进程。之后，**各进程用该梯度和各自的`optimizer`**来更新参数。
  - 由于每个进程拥有独立的解释器和 `GIL`
  - 相比于`DataParallel`，`DataParallel`全程维护一个 `optimizer`，对各 `GPU` 上梯度进行求和，而在主 `GPU` 进行参数更新，之后再将模型参数 `broadcast` 到其他 `GPU`。

## 运行train.py

- ```shell
  CUDA_VISIBLE_DEVICES=0,1,2,3 python -m torch.distribute.launch --nproc_per_node=num_of_GPU train.py (--arg1 --arg2 --arg3 and all other arguments of your training script)
  ```

-  相当于利用`torch.distribute.launch` 去执行`train.py`，`torch.distibute.launch` 会向`train.py`传递`--local_rank` 参数，也就是当前进程使用的GPU

## train.py

- 上面说到，`train.py`需要接收`--local_rank`参数，因此需要引入`argumentparser`来解析该参数

  - ```python
    parser.add_argument("--local_rank", type=int, default=0)
    ```

- 指定使用的GPU

  - ```python
    torch.cuda.set_device(args.local_rank)  #利用torch.distribute.launch 传递的local_rank参数指定GPU
    ```

- 初始化初始化GPU通信方式和参数的获取方式

  - ```
    torch.distributed.init_process_group(backend="nccl", init_method="env://")
    
    ```

- 进程间同步
  - ```python
    def synchronize():
        if not distributed.is_available():
            return
    
        if not distributed.is_initialized():
            return
    
        world_size = distributed.get_world_size()
    
        if world_size == 1:
            return
    
        distributed.barrier()
    ```

  - [distributed.barrier()用法参考](https://stackoverflow.com/questions/59760328/how-does-torch-distributed-barrier-work)

    - 本质上是一个阻塞进程的工具，当所有进程都处于阻塞状态时，所有进程解除阻塞，进入运行状态

- 将模型迁移DistributedDataParallel

  - ```python
    model = torch.nn.parallel.DistributedDataParallel(
            model, device_ids=[args.local_rank], output_device=args.local_rank,
            # this should be removed if we update BatchNorm stats
            broadcast_buffers=True,
        )
    model = model.module
    ```

- `Dataloader`

  - 主要修改的是`data sampler`，利用的是`DistributedSampler`

    - ```python
      train_sampler = torch.utils.data.distributed.DistributedSampler(train_dataset)
      ```

    - [DistributedSampler详细用法参看这里](https://pytorch.org/docs/stable/data.html?highlight=distributedsampler#torch.utils.data.distributed.DistributedSampler)

  - dataloader定义需要注意的是 batchsize设置的是单卡的batch，不是多卡合起来的batch

    - ```python
      train_loader = DataLoader(
          train_set,
          batch_size=batch_size_per_gpu,
          sampler=train_sampler,
          num_workers=cfg['RUNTIME']['NUM_WORKERS'],
          collate_fn=collate_fn(cfg['INPUT']['SIZE_DIVISIBLE']),
      )
      ```

## 示例

```python
import torch
import argparse
import torch.distributed as dist


parser = argparse.ArgumentParser()
parser.add_argument('--local_rank', default=-1, type=int,
                    help='node rank for distributed training')
args = parser.parse_args()


dist.init_process_group(backend='nccl')
torch.cuda.set_device(args.local_rank)
synchronize()


train_dataset = ...
train_sampler = torch.utils.data.distributed.DistributedSampler(train_dataset)


train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=..., sampler=train_sampler)


model = ...
model = torch.nn.parallel.DistributedDataParallel(model, device_ids=[args.local_rank],output_device=args.local_rank)
model = model.module

optimizer = optim.SGD(model.parameters())


for epoch in range(100):
   for batch_idx, (data, target) in enumerate(train_loader):
      images = images.cuda(non_blocking=True)
      target = target.cuda(non_blocking=True)
...
      output = model(images)
      loss = criterion(output, target)
...
optimizer.zero_grad()
loss.backward()
optimizer.step()
```



# 其他

- `distributed.get_world_size()` 获取进程总数
- `distributed.get_rank()` 获取当前进程序号
- `distributed.is_available()`

  

