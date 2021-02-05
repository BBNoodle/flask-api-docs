# -*- coding: utf-8 -*- 
# @Time : 2/5/21 10:10 AM 
# @Author : mxt
# @File : setup.py

import setuptools


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="xt-FlaskAPIDocs",
    version="0.0.2",
    author="Maoxinteng",
    author_email="1214403402@qq.com",
    description="Interface automation document based on flash.",
    long_description='Flask-Docs',
    long_description_content_type="text/markdown",
    url="https://github.com/mxtadmin/flask-api-docs",
    packages=[
        "flask_docs"
    ],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires=">=3.6",
    install_requires=["Flask"],
)
