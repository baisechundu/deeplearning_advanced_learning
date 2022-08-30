# /usr/bin/python3
# -*- coding:utf-8 -*-
"""
# @time: 2022/8/30 22:37
# @Author: baiyang
# Email: 308982012@qq.com
# File: malloc_collect.py
# @software: PyCharm
"""
import ctypes
import os
import random
import time
from threading import Thread

import psutil

MEMORY_THRESHOLD = 500000000  # byte


def trim_memory():
    libc = ctypes.CDLL("libc.so.6")
    return libc.malloc_trim(0)


def should_trim_memory() -> bool:
    # check if we're close to our OOM limit through psutil
    process = psutil.Process(os.getpid())
    return process.memory_info().rss > MEMORY_THRESHOLD


def trim_loop() -> None:
    while True:
        time.sleep(random.randint(30, 60))  # jitter between 30 and 60s
        if not should_trim_memory():
            continue
        ret = trim_memory()
        print("trim memory result: ", ret)


def main() -> None:
    # run web server
    thread = Thread(name="TrimThread", target=trim_loop)
    thread.daemon = True
    thread.start()
