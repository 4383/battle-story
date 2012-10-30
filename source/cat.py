#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
author:Hervé BERAUD
filename:main.py
"""
try:
    import sys
    import pygame
    from pygame.locals import *
    from const import RESOURCES_PATH_IMG
except ImportError as e:
    print(e)

class Cat():
    """
    """

    def __init__(self, window):
        """
        """
        self.window = window
        self.img = pygame.image.load('{0}cat.png' . format(RESOURCES_PATH_IMG))
        self.catx = 10
        self.caty = 10

    def move(self):
        """
        """
        if self.catx < 220:
            self.catx += 5
            self.caty += 5

        self.window.blit(self.img, (self.catx, self.caty))
