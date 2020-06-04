# 前引

- hook定义：是计算机程序设计术语，指通过**拦截软件模块间的函数调用、消息传递、事件传递**来修改或扩展操作系统、应用程序或其他软件组件的行为的各种技术。处理被拦截的函数调用、事件、消息的代码，被称为钩子（hook）

- **module call方法执行流程（foraward）**

  - ```python
      def __call__(self, *input, **kwargs):
            # forward_pre_hook
            for hook in self._forward_pre_hooks.values():
                result = hook(self, input)
                if result is not None:
                    if not isinstance(result, tuple):
                        result = (result,)
                    input = result
            # forward
            if torch._C._get_tracing_state():
                result = self._slow_forward(*input, **kwargs)
            else:
                result = self.forward(*input, **kwargs)
            # forward_hook
            for hook in self._forward_hooks.values():
                hook_result = hook(self, input, result)
                if hook_result is not None:
                    result = hook_result
            # backwrad_hook
            if len(self._backward_hooks) > 0:
                var = result
                while not isinstance(var, torch.Tensor):
                    if isinstance(var, dict):
                        var = next((v for v in var.values() if isinstance(v, torch.Tensor)))
                    else:
                        var = var[0]
                grad_fn = var.grad_fn
                if grad_fn is not None:
                    for hook in self._backward_hooks.values():
                        wrapper = functools.partial(hook, self)
                        functools.update_wrapper(wrapper, hook)
                        grad_fn.register_hook(wrapper)
            return result
    ```

- 从上面可以看到，注册了hook函数之后，在call方法就会调用hook函数，**而函数的输入是定死的，也就是传入什么由call方法决定**

# Tensor.register_hook

- 注册一个反向传播的hook函数，也就是在反向传播时拦截
- `Tensor.register_hook(hook_fn)`
- hook_fn 仅一个输入参数，为张量的梯度
  - 返回值为None，则该tensor的梯度不改变
  - 返回值为Tensor，则该tensor的梯度被返回的Tensor代替



# forward_hook

- 注册Module的前向传播hook函数，在module前向传播**后**拦截
- `module.register_forawrd_hook(hook_fn)`
- `hook_fn(module,input,output)`
  - module：当前网络层
  - input：当前网络层输入数据
  - output：当前网络层输出数据



# forward_pre_hook

- 注册Module的前向传播hook函数，在module前向传播**前**拦截

- `module.register_forawrd_pre_hook(hook_fn)`
- `forawrd_pre_hook(module,input)`
  - 返回值为None，input不发生该百年
  - 返回值不为None，module前向传播时input替换为return

# backward_hook

- 和`Tensor.hook`相似
- `module.register_backward_hook(hook_fn)`
- `hook_fn(module,grad_input,grad_output)`
  - grad_input：当前网络层输入梯度数据
  - grad_output：当前网络层输出梯度数据



