from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CppExtension

setup(
    name="warp_perspective",
    ext_modules=[
        CppExtension(
            "warp_perspective",
            ["example_app/warp_perspective/op.cpp"],
            libraries=["opencv_core", "opencv_imgproc"],
        )
    ],
    cmdclass={"build_ext": BuildExtension.with_options(no_python_abi_suffix=True)},
)

# 这个也只是一种编译方式,如此阴间,还不如cmake