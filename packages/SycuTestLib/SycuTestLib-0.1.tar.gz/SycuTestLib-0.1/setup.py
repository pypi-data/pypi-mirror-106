from setuptools import setup,find_packages

long_description = "" #这里可以导入外部的README.md

setup(
    name='SycuTestLib', # 项目名
    version='0.1', # 如 0.0.1/0.0.1.dev1
    description='This is a Test Lib', 
    long_description = 'None', 
    url='https://github.com/tanxinyue/multable', # 如果有github之类的相关链接
    author='LiChunYu', # 作者
    author_email='28898830@qq.com', # 邮箱
    license='SYCU',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='Test', # 关键词之间空格相隔一般
    install_requires = [
    ],
    packages=find_packages(),
    include_package_data = True, #
    entry_points={ #如果发布的库包括了命令行工具

      }
)