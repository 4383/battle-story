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
    from const import WINDOW_WIDTH
except ImportError as e:
    print(e)

#class AnimatedSprite(pygame.sprite.Sprite):
#    """
#    """
#
#    def __init__(self, images, fps = 10):
#        """
#        """
#        pygame.sprite.Sprite.__init__(self)
#        self._images = images
#
#        # Track the time we started, and the time between updates.
#        # Then we can figure out when we have to switch the image.
#        self._start = pygame.time.get_ticks()
#        self._delay = 1000 / fps
#        self._last_update = 0
#        self._frame = 0
#        self.image = None
#
#        # Call update to set our first image.
#        self.update()
#
#    def update(self, t):
#        """
#        """
#        # Note that this doesn't work if it's been more that self._delay
#        # time between calls to update(); we only update the image once
#        # then, but it really should be updated twice.
#
#        if t - self._last_update > self._delay:
#            self._frame += 1
#            if self._frame >= len(self._images):
#                self._frame = 0
#            self.image = self._images[self._frame]
#            self._last_update = t

class Bomb(pygame.sprite.Sprite):
    """
    """

    def __init__(self, fps = 10):
        """
        """
        images, self.rects = core.load_sliced_sprites(64, 64, 'weapon{0}explode.png' . format(os.sep))
        pygame.sprite.Sprite.__init__(self)
        self._images = images

        # Track the time we started, and the time between updates.
        # Then we can figure out when we have to switch the image.
        self._start = pygame.time.get_ticks()
        self._delay = 1000 / fps
        self._last_update = 0
        self._frame = 0

        # Call update to set our first image.
        self.update()
        self.actual_position = 0

    def update(self):
        """
        """
        # Note that this doesn't work if it's been more that self._delay
        # time between calls to update(); we only update the image once
        # then, but it really should be updated twice.
        t = pygame.time.get_ticks()

        if t - self._last_update > self._delay:
            self._frame += 1
            if self._frame >= len(self._images):
                self._frame = 0
            self.image = self._images[self._frame]
            self.rect = self.rects[self._frame]
            #self.rect.left += self.actual_position
            #if self.actual_position < WINDOW_WIDTH:
            #    self.actual_position += 64
            #else:
            #    self.actual_position += 64
            self._last_update = t

#class Bomb(AnimatedSprite):
#    """
#    """
#
#    def __init__(self):
#        """
#        """
#        images = core.load_sliced_sprites(64, 64, 'weapon{0}explode.png' . format(os.sep))
#        AnimatedSprite.__init__(self, images)
#
#    def update(self):
#        """
#        """
#        super(AnimatedSprite, self).update(pygame.time.get_ticks())
#
#    def draw(self):
#        """
#        """
#        super(Animated, self).draw()
