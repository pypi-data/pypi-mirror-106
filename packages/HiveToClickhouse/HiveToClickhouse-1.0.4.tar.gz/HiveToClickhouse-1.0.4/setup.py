# -*- coding:utf-8 -*-
import os
import requests

from setuptools import setup, find_packages

# 包名
name = 'HiveToClickhouse'
with open('requirements.txt', 'r') as f:
    # requirements.txt 可用 pipreqs ./ 命令生成
    requirements = [i for i in f.readlines() if i.strip()]

def md_to_rst(from_file, to_file):
    """
    将markdown格式转换为rst格式
    @param from_file: {str} markdown文件的路径
    @param to_file: {str} rst文件的路径
    """
    response = requests.post(
        url='http://c.docverter.com/convert',
        data={'to': 'rst', 'from': 'markdown'},
        files={'input_files[]': open(from_file, 'rb')}
    )

    if response.ok:
        with open(to_file, "wb") as f:
            f.write(response.content)
md_to_rst("README.md", "README.rst")
with open('README.rst', 'r') as f:
    reade_me = f.read()

setup(
    # 版本号，添加为打包文件的后缀名
    version='1.0.4',
    # 对项目简短的一个形容
    description='hive sql 转clickhouse sql',

    py_modules=['HiveToClickhouse'],
    # 打包起来的包的文件名
    name=name,
    # 作者: xiongrencong
    author='iyourcar',
    # 作者的邮箱: xiongrencong@youcheyihou.com
    author_email='xiongrencong@youcheyihou.com',
    # 包的详细描述, 相当于readme
    long_description=reade_me,
    # 需要安装的依赖包
    install_requires=requirements,
    # 参数决定包是否作为一个 zip 压缩后的 egg 文件安装（True），还是作为一个以 .egg 结尾的目录安装（False）, 有些环境不支持zip安装，可设置为False
    zip_safe=False
)

