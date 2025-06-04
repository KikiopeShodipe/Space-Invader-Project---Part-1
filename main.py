import pygame
import random
import math
#initialize the windows
pygame.init()
WIDTH,HEIGHT=800,500
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Space Invaders Game")
pygame.display.set_icon(pygame.image.load('ufo.png'))
background=pygame.image.load('backgroung.png')
player_img=pygame.transfoem.scale(pygame.image.load('spaceship.png'),(65,65))
PLAYER_WIDTH,PLAYER_HEIGHT=65,65
player_img=pygame.transfoem.scale(pygame.image.load('enemy.png'),(65,65))
ENEMY_WIDTH,ENEMY_HEIGHT=65,65
player_img=pygame.transfoem.scale(pygame.image.load('bullet.png'),(33,33))
BULLET_WIDTH,BULLET_HEIGHT=33,33
# Fonts
font = pygame.font.Font('freesansbold.ttf', 32)
over_font = pygame.font.Font('freesansbold.ttf', 64)
# Player
player_x = WIDTH // 2 - PLAYER_WIDTH // 2
player_y = HEIGHT - PLAYER_HEIGHT - 20
player_speed = 5
player_x_change = 0