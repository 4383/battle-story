#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
author:Hervé BERAUD
filename:main.py
"""
try:
    import ConfigParser
    import logging
    import os
    import sys
    import pygame
    from pygame.locals import *
except ImportError as e:
    print(e)

config = ConfigParser.ConfigParser()
# Path for resource and other.
PATH = '{0}{1}' . format(os.getcwd(), os.sep)
RESOURCES_PATH = '{0}resources{1}' . format(PATH, os.sep)
RESOURCES_PATH_IMG = '{0}resources{1}pictures{1}' . format(PATH, os.sep)
RESOURCES_PATH_MUSIC = '{0}resources{1}music{1}' . format(PATH, os.sep)
RESOURCES_PATH_FONT = '{0}resources{1}fonts{1}' . format(PATH, os.sep)
RESOURCES_PATH_IMG_MAPS = '{0}resources{1}pictures{1}maps{1}' . format(PATH, os.sep)
FONT_DK_SAMHAIN = '{0}DK_Samhain.ttf' . format(RESOURCES_PATH_FONT)
LOG_FILE = '{0}log{1}trace.log' . format(PATH, os.sep)
CONFIG_FILE = '{0}source{1}conf.ini' . format(PATH, os.sep)
CONFIG_LEVEL_PATH = '{0}source{1}level{1}' . format(PATH, os.sep)
if not config.read(CONFIG_FILE):
    logging.error('Not configuration file available')
    sys.exit(1)
logging.info('Loading config file OK !')
# Diplay configuration
WINDOW_WIDTH = config.getint('BASIC', 'WINDOW_WIDTH')
WINDOW_HEIGHT = config.getint('BASIC', 'WINDOW_HEIGHT')
FPS_FREQUENCY = config.getfloat('BASIC', 'FPS_FREQUENCY')
FPS_CLOCK = pygame.time.Clock()
# Color
GREEN = (0, 255, 0)
GREEN_PELOUSE = (0, 205, 0)
BLACK = (0, 0, 0)
CIEL = (0, 191, 255)

if __name__ == '__main__':
    print('PATH : {0}' . format(PATH))
    print('RESOURCES_PATH : {0}' . format(RESOURCES_PATH))
    print('RESOURCES_PATH_IMG : {0}' . format(RESOURCES_PATH_IMG))
    print('RESOURCES_PATH_MUSIC : {0}' . format(RESOURCES_PATH_MUSIC))
    print('RESOURCES_PATH_FONT : {0}' . format(RESOURCES_PATH_FONT))
    print('LOG_FILE : {0}' . format(LOG_FILE))
    print('CONFIG_FILE : {0}' . format(CONFIG_FILE))
    print('FPS_FREQUENCY : {0}' . format(FPS_FREQUENCY))
    print('FPS_CLOCK : {0}' . format(FPS_CLOCK))
    print('GREEN : {0}' . format(GREEN))
    print('BLACK : {0}' . format(BLACK))
