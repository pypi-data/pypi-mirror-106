#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： hj
# datetime： 2021/5/13 0013 下午 2:47 
# ide： PyCharm2020.1.3

import sys
import os
sys.path.append('/edysdk/')
from edysdk.edy3 import sum


def fun1():
    print("这是edw1模块的函数1")

def fun2():
    print("这是edw1模块的函数2")

def fun3():
    s=sum(3,7)
    print("sum总和为：%s"%(s))

# fun3()