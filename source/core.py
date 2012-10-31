#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
author:Hervé BERAUD
filename:core.py
"""
try:
    import sys
    import logging
    import pygame
    from jukebox import Jukebox
except ImportError as e:
    print(e)

def quit_game():
    """
    Quit game safety and properly
    """
    logging.info('Pygame shutdown please wait...')
    jukebox = Jukebox()
    jukebox.quit()
    pygame.quit()
    logging.info('Byby')
    sys.exit(0)


