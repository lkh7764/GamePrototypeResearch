import pygame, sys, time
from pygame.locals import*


# 배경 이미지 설정
background1 = pygame.image.load("background1.png")
background2 = pygame.image.load("background2.png")
background3 = pygame.image.load("background3.png")
background4 = pygame.image.load("background4.png")
background5 = pygame.image.load("background5.png")
background6 = pygame.image.load("background6.png")
background_ship = pygame.image.load("ship.png")
backgrounds = [background1, background2, background3, background4,
              background5, background6, background_ship]

# 플레이어 설정
player = pygame.Rect(0,350,60,100)
## 이미지
player_F1 = {'sprite_pos': (0,0,60,100)}
player_F2 = {'sprite_pos': (60,0,60,100)}
player_F3 = {'sprite_pos': (120,0,60,100)}
player_F = [player_F1, player_F2, player_F3]

player_B1 = {'sprite_pos': (0,100,60,100)}
player_B2 = {'sprite_pos': (60,100,60,100)}
player_B3 = {'sprite_pos': (120,100,60,100)}
player_B = [player_B1, player_B2, player_B3]

player_R1 = {'sprite_pos': (0,200,60,100)}
player_R2 = {'sprite_pos': (60,200,60,100)}
player_R3 = {'sprite_pos': (120,200,60,100)}
player_R = [player_R1, player_R2, player_R3]

player_L1 = {'sprite_pos': (0,300,60,100)}
player_L2 = {'sprite_pos': (60,300,60,100)}
player_L3 = {'sprite_pos': (120,300,60,100)}
player_L = [player_L1, player_L2, player_L3]

player_image = player_F[0]

# 아이콘 이미지 설정
icon_fishing = {'sprite_pos': (0,0,100,70)}
icon_cooking = {'sprite_pos': (100,0,100,70)}
icon_cleaning = {'sprite_pos': (200,0,100,70)}

icon_image = icon_fishing
