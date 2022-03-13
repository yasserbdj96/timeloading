#!/usr/bin/env python
# coding:utf-8
#code by:YasserBDJ96
#email:yasser.bdj96@gmail.com

#START{
from setuptools import setup,find_packages
setup(
    name="timeloading",
    version="0.0.1",
    author="YasserBDJ96",
    author_email="yasser.bdj96@gmail.com",
    description='''Animated loading bar. This package is a loading bar that appears when a specific function is run an animation and text. This bar is stoped to run after the function has finished working. You can control the shape and the waiting message, even the animation and its colors.''',
    long_description_content_type="text/markdown",
    long_description=open('README.md','r').read(),
    license='''MIT License''',
    packages=find_packages(),
    url="https://yasserbdj96.github.io/",
    project_urls={
        'Source Code': "https://github.com/yasserbdj96/timeloading",
        'Instagram': "https://www.instagram.com/yasserbdj96/",
    },
    install_requires=[],
    keywords=['yasserbdj96','python','loading','bar'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Software Development :: Libraries :: Python Modules",
        'Topic :: Communications :: Email'
    ],
    python_requires=">=3.x.x"
)
#}END.