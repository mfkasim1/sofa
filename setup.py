import os
from setuptools import setup, find_packages
from version import get_version

setup(
    name='sofa',
    version=get_version(),
    description='The forward model of the moving sofa problem',
    url='https://github.com/mfkasim91/sofa',
    author='mfkasim91',
    author_email='firman.kasim@gmail.com',
    license='BSD-3',
    packages=find_packages(),
    python_requires=">=2.7",
    install_requires=[
        "numpy>=1.8.2",
        "matplotlib>=1.5.3",
        "shapely>=1.6.0",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: Scientific/Engineering :: Mathematics",
        "License :: OSI Approved :: MIT License",

        "Programming Language :: Python :: 2.7"
    ],
    keywords="optimization simulation",
    zip_safe=False
)
