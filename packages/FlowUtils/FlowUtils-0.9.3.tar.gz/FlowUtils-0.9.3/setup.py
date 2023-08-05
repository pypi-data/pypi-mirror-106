from setuptools import setup, Extension, dist

dist.Distribution().fetch_build_eggs(['numpy>=1.7'])

import numpy as np


with open("README.md", "r") as fh:
    long_description = fh.read()

logicle_extension = Extension(
    'flowutils.logicle_c',
    sources=[
        'flowutils/logicle_c_ext/_logicle.c',
        'flowutils/logicle_c_ext/logicle.c'
    ],
    include_dirs=[np.get_include(), 'flowutils/logicle_c_ext'],
    extra_compile_args=['-std=c99']
)

setup(
    name='FlowUtils',
    version='0.9.3',
    packages=['flowutils'],
    package_data={'': []},
    description='Flow Cytometry Standard Utilities',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Scott White',
    author_email='whitews@gmail.com',
    license='BSD',
    url="https://github.com/whitews/flowutils",
    ext_modules=[logicle_extension],
    install_requires=['numpy>=1.7'],
    classifiers=[
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.6'
    ]
)
