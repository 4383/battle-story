#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
author:Hervé BERAUD
filename:game.py
"""
try:
    import ConfigParser
    import sys
    import logging
    import datetime
    import pygame
    from pygame.locals import *
    from engine.jukebox import Jukebox
    from const import RESOURCES_PATH_IMG_MAPS
    from const import CONFIG_LEVEL_PATH
    from const import LOG_FILE
    from const import FPS_FREQUENCY
    from const import WINDOW_WIDTH
    from const import WINDOW_HEIGHT
    import menu
except ImportError as e:
    print(e)

config = ConfigParser.ConfigParser()

class Game():
    """
    Create, configure and run a party of game
    """

    def __init__(self, level_conf_name):
        """
        Initialize object game
        """
        if not level_conf_name:
            raise Exception('Configuration level file is not defined')
        self.config_file = '{0}{1}.ini' . format(CONFIG_LEVEL_PATH, level_conf_name)
        self.load_conf()
        level = Level(self.conf_level)

    def load_conf(self):
        """
        Load every config for this party (level)
        """
        if not config.read(self.config_file):
            logging.error('Not configuration file available')
            sys.exit(1)

        self.conf_level = config.items('MAPPING')
        #self.mapper = config.get('MAPPING', 'MAPPER')
        #self.map_pattern = config.get('MAPPING', 'PATTERN')
        #self.map_render = config.get('MAPPING', 'RENDER')


class Level():
    """
    Create a level map and return list of element not
    walkable
    """

    def __init__(self, conf):
        """
        """
        if type(conf) is not 'dict':
            self.conf = dict(conf)

        print(self.conf['mapper'])
        print(self.conf['mapper_widht'])
        print(self.conf['mapper_height'])


        self._set_mapper(
            self.conf['mapper'],
            self.conf['mapper_widht'],
            self.conf['mapper_height']
        )

        self._set_pattern(
            self.conf['pattern'],
            self.conf['pattern_width'],
            self.conf['pattern_height']
        )

        self._set_render(
            self.conf['render'],
            self.conf['render_width'],
            self.conf['render_height']
        )

    def _check_conf():
        """
        """

    def _set_mapper(self, str_picture, int_block_width, int_block_height):
        """
        Configure mapper.
        Mapper is a basic picture with only colored blocks to
        define position of this and use to creating rendered maps
        string picture define the picture to load.
        int width define the width of an unit block.
        int height define the height of an unit block.
        """
        self._mapper = self._loader(
            str_picture,
            int_block_width,
            int_block_height
        )

    def _set_pattern(self, str_picture, int_block_width, int_block_height):
        """
        """
        self._pattern = self._loader(
            str_picture,
            int_block_width,
            int_block_height
        )
        print(self._pattern)

    def _set_render(self, str_picture, int_block_width, int_block_height):
        """
        """
        self._render, self.render_rect = self._loader(
            str_picture,
            int_block_width,
            int_block_height,
            False
        )
        print(self._render)

    def make(self):
        """
        """

    def _loader(self, str_picture, int_width, int_height, bool_abstract=True):
        """
        Load an image and extract and create mapping matrice contening
        list of color ordered or just load
        and extract image and return ordered array contening picture
        """
        if type(int_width) is not 'int':
            int_width = int(int_width)
        if type(int_height) is not 'int':
            int_height = int(int_height)
        if bool_abstract:
            row = []
            columns = []
        else:
            images = []
            rects = []
        fullname = '{0}{1}' . format(RESOURCES_PATH_IMG_MAPS, str_picture)
        master_image = pygame.image.load(fullname).convert_alpha()

        master_width, master_height = master_image.get_size()
        for j in xrange(int(master_height/int_height)):
            for i in xrange(int(master_width/int_width)):
                if bool_abstract:
                    columns.append(master_image.get_at((
                        i * int_width,
                        j * int_height
                    )))
                else:
                    tmp_img = master_image.subsurface((
                        i*int_width,
                        j*int_height,
                        int_width,
                        int_height
                    ))
                    images.append(tmp_img)
                    rects.append(tmp_img.get_rect())
            if bool_abstract:
                row.append(columns)
                columns = []
        if bool_abstract:
            return row
        else:
            return images, rects

    def _map_to_render(self):
        """
        """

class Artificial_intelligence():
    """
    Control AI for action against player
    """

    def ___init__():
        """
        """

if __name__ == "main":
    level = Level()
