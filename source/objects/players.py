#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
author:Hervé BERAUD
filename:nature.py
"""
try:
    import os
    import sys
    import pygame
    from pygame.locals import *
    import core
except ImportError as e:
    print(e)

class Hero(pygame.sprite.Sprite):
    """
    Nature element for background showing a simple cloud
    """

    def __init__(self, fps = 10):
        """
        """
        self.img_walks, self.rects_walks = core.load_sliced_sprites(34, 60, 'player{0}walks.png' . format(os.sep))
        self.img_stay, self.rects_stay = core.load_sliced_sprites(34, 60, 'player{0}stays.png' . format(os.sep))
        pygame.sprite.Sprite.__init__(self)
        self._images = None

        self._start = pygame.time.get_ticks()
        self._delay = 1000 / fps
        self._last_update = 0
        self._frame = 0
        self.posx = 0
        self.stop = False

        self.actual_position = 0

    def walk(self, t):
        if self._images == None:
            self._images = self.img_walks
            self.rects = self.rects_walks
        if self.posx >= 400:
            self.stop = True
            self._images = None
            return
        self._animate(t)
        self.posx += 3
        self.rect.topleft = self.posx, 500 - self.rect.height

    def stay(self, t):
        if self._images == None:
            self._images = self.img_stay
            self.rects = self.rects_stay
        self._animate(t)
        self.rect.topleft = self.posx, 500 - self.rect.height

    def _animate(self, t):
        if t - self._last_update > self._delay:
            self._frame += 1
            if self._frame >= len(self._images):
                self._frame = 0
            self.image = self._images[self._frame]
            self.rect = self.rects[self._frame]
            self._last_update = t

    def play_auto_animation(self):
        t = pygame.time.get_ticks()
        if not self.stop:
            self.walk(t)
        else:
            self.stay(t)
