# Notes

This repo is just me messing around with tensorflow 2.

### Deformable Conv Nets

The `defconv` layer is taken from [here](https://github.com/DHZS/tf-deformable-conv-layer/blob/adf3b64e343e43da1c32d88a1d0cc05763b7d41a/nets/deformable_conv_layer.py). I had to modify it in a few places to make it run in the Tensorflow 2.0 RC.

### Nvidia GPU fixes

`util.fix_gpu()` fixes Tensorflow 2.0 RC on 16xx and 20xx series Nvidia GPUs. Call that before running anything if you have one of those.

### Reloading on edit

```python
from importlib import reload
reload(mnist)
```

### Stardard Workflow

```python
from importlib import reload
import util
util.fix_gpu()
import mnist
mnist.train_loop(5)
reload(mnist)
mnist.train_loop(5)
```
