参考 https://pytorch.org/tutorials/advanced/torch_script_custom_ops.html
这个网站提供的例子蛮蠢的,需要opencv,CMakeLists.txt也写错了
### 第一种方案
``` shell
mkdir build
cd build
cmake -DCMAKE_PREFIX_PATH="$(python -c 'import torch.utils; print(torch.utils.cmake_prefix_path)')" ..
make -j
python testOp.py
```
遇到了如下两个问题
```shell
Could NOT find CUDA (missing: CUDA_INCLUDE_DIRS) (found version "7.5")

CMake Error at CMakeLists.txt:10 (target_compile_features):
  target_compile_features specified unknown feature "cxx_std_14" for target
  "warp_perspective".
```

#### cmake问题
需要的最低cmake版本为3.8.1
安装cmake
``` shell
wget https://github.com/Kitware/CMake/releases/download/v3.16.0/cmake-3.16.0.tar.gz
tar -zxvf cmake-3.16.0.tar.gz
cd cmake-3.16.0
./bootstrap && make
make install
```

#### cuda问题
解决方案:
export PATH=/usr/local/cuda-10.2/bin/:$PATH
nvcc -V 确认

### 其它方法
- 使用JIT compilation
- 使用Setuptools
- 都很阴间的编译,我拒绝