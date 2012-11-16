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
    from const import LOG_FILE
    from const import FPS_FREQUENCY
    from const import WINDOW_WIDTH
    from const import WINDOW_HEIGHT
    from engine.jukebox import Jukebox
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
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
    pygame.display.set_caption('BATTLE-STORY')
    cat = Cat(window)
    jukebox = Jukebox()
    logging.info('Running game')

    while True:
        menu.main_menu(window)

if __name__ == '__main__':
    main()
