from __future__ import print_function

from distutils.command.build import build
import distutils.spawn
import os.path as osp
import shlex
import subprocess
import sys

from setuptools import find_packages
from setuptools import setup


# https://github.com/skvark/opencv-python/blob/master/setup.py
def install_packages(*requirements):
    # No more convenient way until PEP 518 is implemented;
    # setuptools only handles eggs
    subprocess.check_call(
        [sys.executable, "-m", "pip", "install"] + list(requirements)
    )


# https://github.com/skvark/opencv-python/blob/master/setup.py
def get_or_install(name, version=None):
    """If a package is already installed, build against it. If not, install

    """
    # Do not import 3rd-party modules into the current process
    import json
    js_packages = json.loads(
        # valid names & versions are ASCII as per PEP 440
        subprocess.check_output(
            [sys.executable,
             "-m", "pip", "list", "--format", "json"]).decode('ascii'))
    try:
        [package] = (package for package in js_packages
                     if package['name'] == name)
    except ValueError:
        install_packages("%s==%s" % (name, version) if version else name)
        return version
    else:
        return package['version']

version = "0.0.1"

cxx_args = ['-std=c++11', '-std=c++14']

nvcc_args = [
    '-gencode', 'arch=compute_50,code=sm_50',
    '-gencode', 'arch=compute_52,code=sm_52',
    '-gencode', 'arch=compute_60,code=sm_60',
    '-gencode', 'arch=compute_61,code=sm_61',
    '-gencode', 'arch=compute_70,code=sm_70',
    '-gencode', 'arch=compute_70,code=compute_70'
]


if sys.argv[-1] == "release":
    if not distutils.spawn.find_executable("twine"):
        print(
            "Please install twine:\n\n\tpip install twine\n", file=sys.stderr,
        )
        sys.exit(1)

    commands = [
        "git tag v{:s}".format(version),
        "git push origin master --tag",
        "python setup.py sdist",
        "twine upload dist/fastflownet-{:s}.tar.gz".format(version),
    ]
    for cmd in commands:
        print("+ {}".format(cmd))
        subprocess.check_call(shlex.split(cmd))
    sys.exit(0)


setup_requires = []

with open('requirements.txt') as f:
    install_requires = []
    for line in f:
        req = line.split('#')[0].strip()
        install_requires.append(req)



class BuildWithSubmodules(build):

    def run(self):
        return build.run(self)


def main():
    from torch.utils.cpp_extension import BuildExtension
    from torch.utils.cpp_extension import CUDAExtension

    setup(
        cmdclass={'build': BuildWithSubmodules,
                  'build_ext': BuildExtension},
        name="fastflownet",
        version=version,
        description="A python library",
        author="iory",
        author_email="ab.ioryz@gmail.com",
        url="https://github.com/iory/fastflownet",
        long_description=open("README.md").read(),
        long_description_content_type="text/markdown",
        license="MIT",
        classifiers=[
            "Development Status :: 5 - Production/Stable",
            "Intended Audience :: Developers",
            "Natural Language :: English",
            "License :: OSI Approved :: MIT License",
            "Programming Language :: Python",
            "Programming Language :: Python :: 2.7",
            "Programming Language :: Python :: 3.5",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: Implementation :: CPython",
        ],
        packages=find_packages(),
        package_data={'fastflownet':
                      [
                          'correlation_package/correlation_cuda.cc',
                          'correlation_package/correlation_cuda_kernel.cu',
                          'correlation_package/correlation_cuda_kernel.cuh',
                      ]},
        zip_safe=False,
        setup_requires=setup_requires,
        install_requires=install_requires,
        ext_modules=[
            CUDAExtension('correlation_cuda', [
                'fastflownet/correlation_package/correlation_cuda.cc',
                'fastflownet/correlation_package/correlation_cuda_kernel.cu'
            ], extra_compile_args={'cxx': cxx_args, 'nvcc': nvcc_args}),
        ],
    )


if __name__ == '__main__':
    main()
