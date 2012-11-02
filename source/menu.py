#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
author:Hervé BERAUD
filename:menu.py
"""
try:
    import sys
    import random
    import pygame
    from pygame.locals import *
    from const import BLACK
    from const import CIEL
    from const import FONT_DK_SAMHAIN
    from const import FPS_FREQUENCY
    from const import FPS_CLOCK
    from const import GREEN
    from objects.nature import Cloud
    import core
    from jukebox import Jukebox
except ImportError as e:
    print(e)

def main_menu(window):
    """
    Create a main menu
    """
    # Play music
    jukebox = Jukebox()
    jukebox.load('intro')
    jukebox.play()

    # Create background
    background = pygame.Surface(window.get_size())
    background = background.convert()
    background.fill(CIEL)

    if pygame.font:
        font = pygame.font.Font(FONT_DK_SAMHAIN, 46)
        brand_text = font.render('Battle-Story', 1, (10, 10, 10))
        brand_text_pos = brand_text.get_rect(
            centerx=background.get_width()/2,
            centery=background.get_height()/2
        )
        background.blit(brand_text, brand_text_pos)

    window.blit(background, (0, 0))
    pygame.display.flip()

    allsprites = pygame.sprite.RenderPlain()

    for number in range(random.randint(4, 6)):
        altitude = random.randint(0, 300)
        speed = random.randint(1, 6)
        allsprites.add(Cloud(altitude, speed))

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                quit_menu(window)
        allsprites.update()
        window.blit(background, (0, 0))
        allsprites.draw(window)
        pygame.display.flip()
        #pygame.display.update()
        FPS_CLOCK.tick(FPS_FREQUENCY)

def quit_menu(window):
    """
    Create a quit menu
    Called when user want quit game
    """
    jukebox = Jukebox()
    jukebox.load('final')
    jukebox.play()
    while True:
        window.fill(BLACK)
        for event in pygame.event.get():
            if event.type == QUIT:
                core.quit_game()
        pygame.display.update()
        FPS_CLOCK.tick(FPS_FREQUENCY)

