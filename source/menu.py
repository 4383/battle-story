#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
author:Hervé BERAUD
filename:menu.py
"""
try:
    import gettext
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
    import level.card_of_world as play
    import core
    from engine.jukebox import Jukebox
    from engine.game import Game
except ImportError as e:
    print(e)

_ = gettext.gettext

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
        play_txt = font.render(_('JOUER'), 1, (10, 10, 10))
        play_txt_pos = play_txt.get_rect(
            centerx=200,
            centery=background.get_height()/2
        )
        background.blit(play_txt, play_txt_pos)

        load_txt = font.render(_('CHARGER'), 1, (10, 10, 10))
        load_txt_pos = load_txt.get_rect(
            centerx=550,
            centery=background.get_height()/2
        )
        background.blit(load_txt, load_txt_pos)

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
                quit_menu(window)
            elif event.type == MOUSEBUTTONDOWN:
                posx, posy = pygame.mouse.get_pos()
                if posx >= play_txt_pos.left and \
                   posx <= play_txt_pos.left + play_txt_pos.width and \
                   posy >= play_txt_pos.top and \
                   posy <= play_txt_pos.top + play_txt_pos.height:
                    print("jeu")
                    game = Game('map1')
                    game.play(window)
                elif posx >= load_txt_pos.left and \
                   posx <= load_txt_pos.left + load_txt_pos.width and \
                   posy >= load_txt_pos.top and \
                   posy <= load_txt_pos.top + load_txt_pos.height:
                    print("Load")
        hero.play_auto_animation()
        allsprites.update()
        #bombsprites.update()
        window.blit(background, (0, 0))
        allsprites.draw(window)
        pygame.display.flip()
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

