import pygame


def explosion_large():
    #
    explosion_large = pygame.mixer.Sound("music/Explo_Large.wav")
    explosion_large.play()


def explosion_small():
    #
    explosion_small = pygame.mixer.Sound("music/Explo_Small.wav")
    explosion_small.play()


def bullet_whiz():
    #
    bullet_whiz = pygame.mixer.Sound("music/Bullet_Whiz.wav")
    bullet_whiz.play()


def bg_music():
    #
    pygame.mixer.music.load("music/order_music.mp3")

