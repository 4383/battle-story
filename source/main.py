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
except ImportError as e:
    print(e)

GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

def quit_game():
    logging.info('Pygame shutdown please wait...')
    pygame.quit()
    logging.info('Byby')
    sys.exit(0)


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
    fps_frequency = 30
    fps_clock = pygame.time.Clock()
    logging.info('FPS frequency : %s' % fps_frequency)
    window = pygame.display.set_mode((400, 300), 0, 32)
    pygame.display.set_caption('battle-story')
    cat = Cat(window)
    jukebox = Jukebox()
    jukebox.play()
    logging.info('Running game')

    # A dégager
    start = 60

    while True:
        window.fill(BLACK)
        for event in pygame.event.get():
            if event.type == QUIT:
              jukebox.stop()
              quit_game()

        cat.move()

        pygame.display.update()
        fps_clock.tick(fps_frequency)

if __name__ == '__main__':
    main()
