'''
Description: 
version: 
Author: GongZiyao
Date: 2021-05-10 18:13:03
LastEditors: GongZiyao
LastEditTime: 2021-05-17 18:36:48
'''
from setuptools import setup

with open('README.rst', 'r') as f:
    long_description = f.read()

setup(
    name='PyMultition',
    version='0.1.4',
    url='https://github.com/Gzyjl/PyMultition',
    author="GongZiyao",
    author_email='gong.ziyao@outlook.com',
    keywords='python multition Instanciate',
    long_description=long_description,
    description='A Multiton Class for preventing duplicate instances based on serializing init values.',
    packages=['PyMultition'],
    license='MIT',  # 开源许可证类型
    classifiers=[
        'Operating System :: OS Independent',
        'Topic :: Software Development',
        'Programming Language :: Python :: 3.7',
    ],
)
