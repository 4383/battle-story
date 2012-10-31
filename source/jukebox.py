#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
author:Hervé BERAUD
filename:jukebox.py
"""
try:
    import sys
    import logging
    import pygame
    from pygame.locals import *
    from const import RESOURCES_PATH_MUSIC
except ImportError as e:
    print(e)

JUKEBOX = {
    'intro' : '01_-_kmmerer_-_Wicked_game_(Freedom_rmx_by_kmmerer).vaw',
    'final' : 'Tunguska_Electronic_Music_Society_-_Oleg_Sirenko_-_Invasion_.vaw'
}
class Jukebox():
    """
    """

    _instance = None

    def __new__(cls):
        """
        """
        if not cls._instance:
            cls._instance = object.__new__(cls)
            logging.info('Create jukebox...')
        return cls._instance

    def __init__(self):
        """
        """
        logging.info('Initialize jukebox')
        pygame.mixer.init()

    def load(self, tracks):
        """
        """
        if tracks not in JUKEBOX:
            logging.error('Track doesn\'t exist : {0}' . format(tracks))
        pist = '{0}{1}' . format(RESOURCES_PATH_MUSIC, JUKEBOX[tracks])
        logging.info('Loading pist : {0}' . format(pist))
        pygame.mixer.music.load(pist)

    def play(self):
        """
        """
        logging.info('Playing soundtrack')
        pygame.mixer.music.play(-1, 0.0)

    def stop(self):
        """
        """
        logging.info('Stopping soundtrack')
        pygame.mixer.music.stop()

    def change(self, tracks):
        """
        """
        if self.get_busy:
            self.stop()
        self.load(tracks)
        self.play()

    def quit(self):
        """
        """
        logging.info('Jukebox shutdown. Bye')
        pygame.mixer.quit()
