import pygame, sys, time
from pygame.locals import*
from image_info import*

# 기본 설정 - 프레임
pygame.init()
FPS = pygame.time.Clock()

# 창 설정
WINDOWWIDTH = 1240
WINDOWHEIGHT = 980
windowSurface = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT), 0, 32)
pygame.display.set_caption("The sea restaurant")

# 스프라이트 설정 
SPRITESHEET = pygame.image.load("sprites.png")
ICONSHEET = pygame.image.load("IconSprites.png")
UISHEET = pygame.image.load("UIsheet.png")
GAMEOVER = pygame.image.load("game_over.png")
GAMECLEAR = pygame.image.load("game_clear.png")

## 움직임 및 상태
MOVESPEED = 20

moveDown = False
moveUp = False
moveRight = False
moveLeft = False

isFishing = False
isCooking = False
isCleaning = False

isOver = False
isClear = False

Maginot_line_x_list = [500,625,700,750,800,825,850,875,900,925,950,975,1000,
                  1025,1050,1075,1100]
Maginot_line_y_list = [400,425,450,475,500,525,550,575,600,625,650,675,700,
                       725, 750, 800, 850]

Maginot_line_x = Maginot_line_x_list[16]
Maginot_line_y = Maginot_line_y_list[0]

# 테스트 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
game_over = pygame.Rect(500, 500, 50, 50)
game_clear = pygame.Rect(500, 800, 50, 50)
 
while True:
    # 배경 출력
    for background in backgrounds:
        if background == background1:
            windowSurface.blit(background, (0,0),
                               (0,0,WINDOWWIDTH,WINDOWHEIGHT))
        else:
            windowSurface.blit(background, (0,0),
                               (30,0,WINDOWWIDTH,WINDOWHEIGHT))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == KEYDOWN:
            if event.key == K_DOWN or event.key == K_s:
                moveDown = True
                moveUp = False
            if event.key == K_UP or event.key == K_w:
                moveUp = True
                moveDown = False
            if event.key == K_RIGHT or event.key == K_d:
                moveRight = True
                moveLeft = False
            if event.key == K_LEFT or event.key == K_a:
                moveLeft = True
                moveRight = False
            if event.key == 27:
                pygame.quit()
                sys.exit()
        if event.type == KEYUP:
            if event.key == K_DOWN or event.key == K_s:
                moveDown = False
            if event.key == K_UP or event.key == K_w:
                moveUp = False
            if event.key == K_RIGHT or event.key == K_d:
                moveRight = False
            if event.key == K_LEFT or event.key == K_a:
                moveLeft = False

    # 플레이어 이동 범위 - 플레이어 캐릭터가 맨 아래일 때 오류가 남 왜지?
    #for i in range(0, 17):
    #    if i == 0:
    #        Maginot_line_y = Maginot_line_y_list[0]
    #    else:
    #        if Maginot_line_x_list[i-1] < player.left <= Maginot_line_x_list[i]:
    #            Maginot_line_y = Maginot_line_y_list[i]
    #            for i in range(0, 17):
    #                if i == 0:
    #                    Maginot_line_x = Maginot_line_x_list[0]
    #                else:
    #                    if Maginot_line_y_list[i-1] < player.top <= Maginot_line_y_list[i]:
    #                        Maginot_line_x = Maginot_line_x_list[i]
    
    if moveDown and player.bottom < WINDOWHEIGHT-10:
        player.top += MOVESPEED
        player_image = player_F[0]
    if moveUp and player.top > Maginot_line_y:
        player.top -= MOVESPEED
        player_image = player_B[0]
    if moveRight and player.right < Maginot_line_x:
        player.left += MOVESPEED
        player_image = player_R[0]
    if moveLeft and player.left > 0:
        player.left -= MOVESPEED
        player_image = player_L[0]

    windowSurface.blit(SPRITESHEET, player, player_image['sprite_pos'])
    windowSurface.blit(ICONSHEET, (player.left-20, player.top-40), icon_image['sprite_pos'])

    pygame.draw.rect(windowSurface, BLACK, game_over)
    pygame.draw.rect(windowSurface, WHITE, game_clear)

    if player.colliderect(game_over):
        isOver = True
    if player.colliderect(game_clear):
        isClear = True

    if isOver == True:
        windowSurface.blit(GAMEOVER, (0,0))
    if  isClear == True:
        windowSurface.blit(GAMECLEAR, (0,0))

    pygame.display.update()
    FPS.tick(100)
