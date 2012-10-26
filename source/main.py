#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
author:Hervé BERAUD
filename:main.py
"""
try:
    import pygame
    import sys
    from pygame.locals import *
except ImportError as e:
    print(e)

GREEN = (0, 255, 0)

def line(window):
    pygame.draw.line(window, GREEN, (60, 60), (120, 60), 4)

def main():
    """
    Bootstrap or main function
    Initializing PYGAME, create game loop and other features
    """
    print('===========================================')
    print('\t\tBattle-story')
    print('\t\tCreated by : 4383')
    print('===========================================')
    print('Loading pygame...')
    pygame.init()
    print('Initializing pygame...')
    window = pygame.display.set_mode((400, 300))
    pygame.display.set_caption('battle-story')
    print('Running')

    line(window)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                print('Pygame shutdown please wait...')
                pygame.quit()
                print('Byby')
                sys.exit(0)
        pygame.display.update()

if __name__ == '__main__':
    main()
