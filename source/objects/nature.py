#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
author:Hervé BERAUD
filename:nature.py
"""
try:
    import sys
    import pygame
    from pygame.locals import *
    import core
except ImportError as e:
    print(e)

class Cloud(pygame.sprite.Sprite):
    """
    Nature element for background showing a simple cloud
    """

    def __init__(self, altitude, move=2):
        """
        """
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = core.load_image('cloud.png', -1)
        self.altitude = altitude
        self.rect.topleft = 0, altitude
        self.move = move
        self.altitude = altitude
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()

    def update(self):
        """
        """
        newpos = self.rect.move((self.move, 0))
        if not self.area.contains(newpos):
            if self.rect.left > self.area.right:
                self.rect.topleft = -self.rect.left, self.altitude
                newpos = self.rect.move((self.move, 0))
        self.rect = newpos
