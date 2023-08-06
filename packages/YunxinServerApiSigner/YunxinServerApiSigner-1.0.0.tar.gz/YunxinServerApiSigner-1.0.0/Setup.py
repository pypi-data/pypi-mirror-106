from setuptools import setup, find_packages

setup(
    name="YunxinServerApiSigner",
    version="1.0.0",
    author="netease.jiaojian1",
    author_email="netease.jiaojian1@hotmail.com",
    description="云信服务端api签名器",
    url="https://g.hz.netease.com/jiaojian1/yunxinserverapisigner",
    packages=find_packages(),
    install_requires=['pandas', 'openpyxl', ],
)