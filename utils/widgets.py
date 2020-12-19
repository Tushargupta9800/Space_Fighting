#importing libraries

import pygame
pygame.init()
from utils.setandvar import*
from utils.sprites import*

#this function writes the text on the screen
def writeonscreen(text,x,y, size):
    font = pygame.font.match_font('arial')
    fonter = pygame.font.Font(font, size)
    makesurface = fonter.render(text, True, (255, 255, 255))
    text_rect = makesurface.get_rect()
    text_rect.center = (x, y)
    win.blit(makesurface, text_rect)

#this function displays the health of the player on the screen
def displayhealth(health):
    ret = False
    if health <= 0:
        health = 0
        ret = True

    length = 100
    height = 10
    writeonscreen('Health', 50, 17, 15)
    outline = pygame.Rect(30, 27, length, height)
    fill_rect = pygame.Rect(30, 27, health, height)
    pygame.draw.rect(win, GREEN, fill_rect)
    pygame.draw.rect(win, WHITE, outline, 2)
    return ret

#this function displays life of the player
def displaylives(life):
    for i in range (life):
        win.blit(playermini, (350 + (i-1)*tilesize, 15))

#pausing the screen
def pausethescreen():
    wait = True
    while wait:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_p:
                    wait = False


#printing the time elapsed for the powerups
def print_time_elapsed(time_elapsed, text,y, z, x):
    length = 100
    height = 10
    writeonscreen(text,x, y, 15)
    outline = pygame.Rect(30, z, length, height)
    fill_rect = pygame.Rect(30, z, 100 - time_elapsed, height)
    pygame.draw.rect(win, YELLOW, fill_rect)
    pygame.draw.rect(win, WHITE, outline, 2)
