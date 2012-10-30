#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
author:Hervé BERAUD
filename:main.py
"""
try:
    import os
except ImportError as e:
    print(e)

PATH = '{0}{1}' . format(os.getcwd(), os.sep)
RESOURCES_PATH = '{0}resources{1}' . format(PATH, os.sep)
RESOURCES_PATH_IMG = '{0}resources{1}images{1}' . format(PATH, os.sep)
RESOURCES_PATH_MUSIC = '{0}resources{1}music{1}' . format(PATH, os.sep)
LOG_FILE = '{0}log{1}trace.log' . format(PATH, os.sep)

if __name__ == '__main__':
    print(PATH)
    print(RESOURCES_PATH)
    print(RESOURCES_PATH_IMG)
