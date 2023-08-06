# -*- coding:UTF-8 -*-
#!/usr/bin/env python
from __future__ import print_function
from setuptools import setup

setup(
 name="tool_utils", #随便起，跟打包名称无关
 version="0.0.4",
 author="act",
 author_email="xxxxx@xxx.com",
 license="Apache License",
 url="https://xxxxxxxxx",
 packages=["tool_utils"], #包名
 install_requires=["cx_Oracle <= 7.0.0 ", "traceback2 <= 1.4.0"],
 classifiers=[
 "Environment :: Web Environment",
 "Intended Audience :: Developers",
 "Operating System :: OS Independent",
 "Topic :: Text Processing :: Indexing",
 "Topic :: Utilities",
 "Topic :: Internet",
 "Topic :: Software Development :: Libraries :: Python Modules",
 "Programming Language :: Python",
 "Programming Language :: Python :: 3.8"
 ],
)

#name:打包的名称，以后会根据这个包名去下载包
#version:版本号
#author:作者
#author_email:作者email
#license:LiCENSE文件,授权方式
#url:项目地址
#package:打包的项目包名
#install_requires:依赖的包以及版本号
#classifieers:是要求的环境



#删除打包出来的文件夹 build , dist , tool_utils.egg
#打包命令：  python setup.py sdist bdist_wheel
#上传命令：  twine upload dist/*


