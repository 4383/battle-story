#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
author: Hervé BERAUD
filename: decor.py
Module handler for decor elements (penetrable, non penetrable)
'''
try:
    import sys
    import pygame
    from pygame.locals import *
except ImportError as e:
    print(e)

class Block(pygame.sprite.Sprite):
    '''
    Simple object that represent basic element decor
    '''

    def __init__(self, image, rect):
        '''
        '''
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = pygame.Rect(rect, self.image.get_size())
