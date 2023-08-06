# -*- coding: utf-8 -*-
from setuptools import find_packages, setup
from os import path as os_path
import time
this_directory = os_path.abspath(os_path.dirname(__file__))
"""帮助[https://www.notion.so/6bade2c6a5f4479f82a4e67eafcebb3a]

上传到anaconda
https://docs.anaconda.com/anacondaorg/user-guide/tasks/work-with-packages/
 
    """
# 读取文件内容
def read_file(filename):
    with open(os_path.join(this_directory, filename), encoding='utf-8') as f:
        long_description = f.read()
    return long_description

# 获取依赖
def read_requirements(filename):
    return [line.strip() for line in read_file(filename).splitlines()
            if not line.startswith('#')]
# long_description="""

# 这里是说明
# 一个创建库的demo
# http://www.terrychan.org/python_libs_demo/
# """

long_description=read_file("README.md")
setup(
    name='tkit_transformer_xl', #修改包名字-
    version='0.0.0.6',
    description='Terry toolkit tkit_transformer_xl',
    author='Terry Chan',
    author_email='napoler2008@gmail.com',
    url='https://github.com/napoler/tkit_transformer_xl',
    # install_requires=read_requirements('requirements.txt'),  # 指定需要安装的依赖
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        'pytorch-lightning>=1.2.10',
        'transformers>=4.0.0',
        'memory-transformer-xl>=0.1.0',
        'tkit-memory-performer-xl>=0.0.1.0'

    ],
    packages=['tkit_transformer_xl'])

"""
pip freeze > requirements.txt

python3 setup.py sdist
#python3 setup.py install
python3 setup.py sdist upload
"""


# 上传发布帮助

# https://www.notion.so/terrychanorg/PyPi-pip-b371898f30ec4f268688edebab8d7ba1



# ## 打包项目

# ```
# pip install wheel # 安装wheel模块

# python setup.py sdist  # 源码包
# python setup.py bdist_wheel --universal # 打包为无需build的wheel。其中--universal表示py2和py3通用的pure python模块。不满足通用或pure条件的模块不需加此参数
# ```

# ## 上传项目

# 先在pypi注册一个账户：[https://pypi.org/account/register/](https://pypi.org/account/register/)

# 然后安装上传所需模块：

# `pip install twine`

# 最后上传：

# `twine upload dist/*`