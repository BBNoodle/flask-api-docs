# -*- coding: utf-8 -*- 
# @Time : 2/5/21 10:10 AM 
# @Author : mxt
# @File : set_up.py

import setuptools


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="xt-FlaskAPIDocs",
    version="0.0.1",
    author="Maoxinteng",
    author_email="1214403402@qq.com",
    description="Interface automation document based on flash.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mxtadmin/doap-date-utils",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires=">=3.6",
    install_requires=["Flask"],
)