#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
author:Hervé BERAUD
filename:main.py
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
    'intro' : '01_-_kmmerer_-_Wicked_game_(Freedom_rmx_by_kmmerer).mp3',
    'test' : 'test.vaw'
}
class Jukebox():
    """
    """

    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = object.__new__(cls)
            logging.info('Create jukebox...')
        return cls._instance

    def __init__(self):
        """
        """
        logging.info('Initialize jukebox')
        pygame.mixer.init()
        self.load('test')

    def load(self, tracks):
        """
        """
        pist = '{0}{1}' . format(RESOURCES_PATH_MUSIC, JUKEBOX[tracks])
        logging.info('Loading pist : {0}' . format(pist))
        pygame.mixer.music.load(pist)

    def play(self):
        """
        """
        logging.info('Playing soundtrack')
        pygame.mixer.music.play(-1, 0.0)

    def stop(self):
        logging.info('Stopping soundtrack')
        pygame.mixer.music.stop()

    def change(self, tracks):
        """
        """
        if self.get_busy:
            self.stop()
        self.load(tracks)
        self.play()
