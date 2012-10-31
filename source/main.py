#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
author:Hervé BERAUD
filename:main.py
"""
try:
    import sys
    import logging
    import datetime
    import pygame
    from pygame.locals import *
    from cat import Cat
    from jukebox import Jukebox
    from const import LOG_FILE
    from const import FPS_FREQUENCY
    import menu
except ImportError as e:
    print(e)

def main():
    """
    Bootstrap or main function
    Initializing PYGAME, create game loop and other features
    """
    logging.basicConfig(filename=LOG_FILE, level=logging.DEBUG)
    logging.info(datetime.datetime.now())
    logging.info('Loading pygame...')
    pygame.init()
    logging.info('Initializing pygame...')
    logging.info('FPS frequency : %s' % FPS_FREQUENCY)
    window = pygame.display.set_mode((400, 300), 0, 32)
    pygame.display.set_caption('battle-story')
    cat = Cat(window)
    jukebox = Jukebox()
    logging.info('Running game')

    # A dégager
    start = 60

    while True:
        menu.main_menu(window)

if __name__ == '__main__':
    main()
