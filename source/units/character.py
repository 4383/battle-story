#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Author : Hervé BERAUD
Filename : character.py
"""
try:
    import ConfigParser
    import sys
    import logging
    import datetime
    import pygame
    from pygame.locals import *
    from const import RESOURCES_PATH_IMG_MAPS
    from const import CONFIG_LEVEL_PATH
    from const import LOG_FILE
    from const import FPS_FREQUENCY
    from const import FPS_CLOCK
    from const import WINDOW_WIDTH
    from const import WINDOW_HEIGHT
    import core
except ImportError as e:
    print(e)

config = ConfigParser.ConfigParser()

class Character():
    """
    """

    def __init__(self):
        """
        """
        self.life = 100
        self.config_file = '{0}{1}.ini' . format(CONFIG_UNITS_PATH, unit_conf_name)
        self.load_conf()

    def load_conf(self):
        """
        Load every config for this party (level)
        """
        if not config.read(self.config_file):
            logging.error('Not configuration file available')
            sys.exit(1)

        self.conf_unit = config.items('UNIT')

    def dammage(self, point):
        """
        """
        if self.life:
            self.life -= point

    def is_alive(self):
        """
        """
        if self.life:
            return True
        return False

class Hero(Character, pygame.sprite.Sprite):
    """
    """

    def __init__(
        self,
        start_pos,
        all_sprite,
        solid_sprite,
        hero_sprite
    ):
        """
        """
        Character.__init__(self, 'hero')
        pygame.sprite.Sprite.__init__(self)
        self._all_images = {
            'up' : core._loader(
                Character.conf_unit['TOP_IMAGE'],
                Character.conf_unit['TOP_BLOCK_WIDTH'],
                Character.conf_unit['TOP_BLOCK_HEIGHT']
            ),
            'right' : core._loader(
                Character.conf_unit['RIGHT_IMAGE'],
                Character.conf_unit['RIGHT_BLOCK_WIDTH'],
                Character.conf_unit['RIGHT_BLOCK_HEIGHT']
            ),
            'down' : core._loader(
                Character.conf_unit['DOWN_IMAGE'],
                Character.conf_unit['DOWN_BLOCK_WIDTH'],
                Character.conf_unit['DOWN_BLOCK_HEIGHT']
            ),
            'left' : core._loader(
                Character.conf_unit['LEFT_IMAGE'],
                Character.conf_unit['LEFT_BLOCK_WIDTH'],
                Character.conf_unit['LEFT_BLOCK_HEIGHT']
            )
        }
        self.rect = pygame.Rect(
            start_pos,
            (Character.conf_unit['DOWN_BLOCK_WIDTH'], Character.conf_unit['DOWN_BLOCK_HEIGHT'])
        )
        self.speed = 3

    def action(self, event):
        """
        """
        # Attack
        if event.key == K_SPACE:
            self.attack()
        else:
            self.move()

    def move(self):
        """
        """
        if event.key == K_UP:
            self.rect.topleft = (self.rect.posx, (self.rect.posy + self.speed))
        elif event.key == K_DOWN:
            pass
        elif event.key == K_RIGHT:
            pass
        elif event.key == K_LEFT:
            pass

    def attack(self):
        """
        """
