#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
author:Hervé BERAUD
filename:menu.py
"""
try:
    import sys
    import pygame
    from pygame.locals import *
    from const import RESOURCES_PATH_IMG
    from const import FPS_FREQUENCY
    from const import FPS_CLOCK
    from const import GREEN
    from const import BLACK
    import core
    from jukebox import Jukebox
except ImportError as e:
    print(e)

def main_menu(window):
    """
    Create a main menu
    """
    jukebox = Jukebox()
    jukebox.load('intro')
    jukebox.play()
    while True:
        window.fill(GREEN)
        for event in pygame.event.get():
            if event.type == QUIT:
              jukebox.stop()
              quit_menu(window)
        pygame.display.update()
        FPS_CLOCK.tick(FPS_FREQUENCY)

def quit_menu(window):
    jukebox = Jukebox()
    jukebox.load('final')
    jukebox.play()
    while True:
        window.fill(BLACK)
        for event in pygame.event.get():
            if event.type == QUIT:
                core.quit_game()
        pygame.display.update()
        FPS_CLOCK.tick(FPS_FREQUENCY)

