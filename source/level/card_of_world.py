#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
author:Hervé BERAUD
filename:card_of_world.py
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
    from const import GREEN_PELOUSE
    from const import WINDOW_HEIGHT
    from const import WINDOW_WIDTH
    from objects.players import Hero
    from objects.nature import Cloud
    from objects.weapon import Bomb
    import core
    from engine.jukebox import Jukebox
except ImportError as e:
    print(e)

def card_of_world(window):
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

    window.blit(background, (0, 0))
    pygame.display.flip()

    #bomb = Bomb()
    allsprites = pygame.sprite.RenderPlain()

    for number in range(random.randint(4, 6)):
        altitude = random.randint(0, 300)
        speed = random.randint(1, 6)
        allsprites.add(Cloud(altitude, speed))

    hero = Hero()
    allsprites.add(hero)

    pygame.draw.rect(background, GREEN_PELOUSE, (0, 500, WINDOW_WIDTH, 100))

    brand, brand_rect = core.load_image('Battle-story.png', -1)
    brand_rect.left = WINDOW_WIDTH / 2 - brand_rect.width / 2
    brand_rect.top = WINDOW_HEIGHT / 3 - brand_rect.height / 2
    background.blit(brand, brand_rect)

    #bombsprites = pygame.sprite.RenderPlain((bomb))
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
        hero.play_auto_animation()
        allsprites.update()
        #bombsprites.update()
        window.blit(background, (0, 0))
        allsprites.draw(window)
        pygame.display.flip()
        FPS_CLOCK.tick(FPS_FREQUENCY)

