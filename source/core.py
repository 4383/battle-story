#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
author:Hervé BERAUD
filename:core.py
"""
try:
    import os
    import sys
    import logging
    import pygame
    from pygame.locals import *
    from engine.jukebox import Jukebox
    from const import RESOURCES_PATH_IMG
except ImportError as e:
    print(e)

def quit_game():
    """
    Quit game safety and properly
    """
    logging.info('Pygame shutdown please wait...')
    jukebox = Jukebox()
    jukebox.stop()
    jukebox.quit()
    pygame.quit()
    logging.info('Byby')
    sys.exit(0)

def load_image(name, colorkey=None, alpha=False):
    """
    load a simple picture
    """
    fullname = '{0}{1}' . format(RESOURCES_PATH_IMG, name)
    try:
        if not alpha:
            image = pygame.image.load(fullname)
        else:
            image = pygame.image.load(fullname).convert_alpha()
    except pygame.error, message:
        print "image not find :", name
        raise SystemExit, message
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    if not alpha:
        return image, image.get_rect()
    else:
        return image, image.get_size()

def load_sliced_sprites(w, h, filename):
    """
    Load a composed picture from sprite file.
    Using for creating animation
    """
   # images = []
   # master_image, master_size = load_image(filename)

   # master_width, master_height = master_size
    images = []
    rects = []
    fullname = '{0}{1}' . format(RESOURCES_PATH_IMG, filename)
    master_image = pygame.image.load(fullname).convert_alpha()

    master_width, master_height = master_image.get_size()
    for j in xrange(int(master_height/h)):
        for i in xrange(int(master_width/w)):
            tmp_img = master_image.subsurface((i*w,j*h,w,h))
            images.append(tmp_img)
            rects.append(tmp_img.get_rect())
    return images, rects

def _loader(str_picture, int_width, int_height, bool_abstract=True):
    """
    Load an image or extract and create mapping matrice contening
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
    fullname = str_picture
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
