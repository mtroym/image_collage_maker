# -*- coding: utf-8 -*- 
"""
Project:        image_collage_maker
Creator:        TROY.MAO
Create time:    2020-07-18 23:47 Shanghai, China
Filename:       setup.py
Introduction:   - 
"""

import os

from setuptools import setup, find_packages

path = os.path.abspath(os.path.dirname(__file__))

try:
    with open(os.path.join(path, 'README.md')) as f:
        long_description = f.read()
except Exception as e:
    long_description = "image collage maker"

print(find_packages())
setup(
    name="collage_maker",
    version="0.0.2",
    keywords=("image", "image collage"),
    description="image collage maker",
    long_description=long_description,
    long_description_content_type='text/markdown',
    python_requires=">=3.6.8",
    license="MIT Licence",

    url="https://github.com/mtroym/image_collage_maker",
    author="Yiming Mao",
    author_email="maoym.troy@gmail.com",

    packages=find_packages(),
    include_package_data=True,
    install_requires=["opencv-python", "opencv-contrib-python", "numpy"],
    platforms="any",

    scripts=[],
)
