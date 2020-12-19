#by- Team Algoristy
#Space Fighting game in python using pygame

#importing library
import pygame
import random
from os import path
pygame.init()

#creating window
BLACK = (0,0,0)
WHITE = (255, 255, 255)
GREEN = (0, 0, 255)
YELLOW = (255, 255, 0)
width = 480
height = 600
fps = 60
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Space fighting")
clock = pygame.time.Clock()

#loading images/art
img_dir = path.join(path.dirname(__file__), '../data')
bk = pygame.image.load("data/bk/bk.png")
playerimgreal = pygame.image.load(("data/player/player.png"))
playerimg = pygame.transform.scale(playerimgreal, (95, 100))
playermini = pygame.transform.scale(playerimgreal, (30, 31))
speaker = pygame.image.load("data/otherImages/speaker.png")
speaker = pygame.transform.scale(speaker, (50, 50))
history = pygame.image.load("data/otherImages/history.png")
history = pygame.transform.scale(history, (80, 90))
upload = pygame.image.load("data/otherImages/upload.png")
upload = pygame.transform.scale(upload, (40, 40))
highscore = pygame.image.load("data/otherImages/highscore.png")
highscore = pygame.transform.scale(highscore, (40, 40))
update = pygame.image.load("data/otherImages/update.png")
update = pygame.transform.scale(update, (90, 40))
no_sound = pygame.image.load("data/otherImages/no_sound.png")
back = pygame.image.load("data/otherImages/back.png")
no_sound = pygame.transform.scale(no_sound, (70, 70))
games_img = [pygame.transform.scale(pygame.image.load("data/history_games/space_battle.jpg"), (200,250)),
             pygame.transform.scale(pygame.image.load("data/history_games/space_invasion_1980.jpg"), (200,250)),
             pygame.transform.scale(pygame.image.load("data/history_games/space_invasion_alien_shooter_war.jpg"), (200,250)),
             pygame.transform.scale(pygame.image.load("data/history_games/space_invasion_thunder.jpg"), (200,250)),
             pygame.transform.scale(pygame.image.load("data/history_games/space_war.jpg"), (200,250)),
             pygame.transform.scale(pygame.image.load("data/history_games/air_fighter.jpg"), (200,250)),
             pygame.transform.scale(pygame.image.load("data/history_games/and_many_more.jpg"), (200,250))]
game_name = ["Space Battle","Space Invasion 1980",
             "Space Invasion: Alien Shooter War",
             "Space Invasion Thunder", "Space War",
             "Air Fighter", "And Many More"]
next_img = pygame.image.load("data/otherImages/next.png")
next_img = pygame.transform.scale(next_img, (50,50))
enemyimg = [pygame.image.load("data/enemy/enemy1.png"),pygame.image.load("data/enemy/enemy2.png"),pygame.image.load("data/enemy/enemy3.png")]
enemyimg[0] = pygame.transform.scale(enemyimg[0], (60, 70))
enemyimg[0] = pygame.transform.rotate(enemyimg[0], 180)
enemyimg[1] = pygame.transform.scale(enemyimg[1], (75, 80))
enemyimg[1] = pygame.transform.rotate(enemyimg[1], 180)
enemyimg[2] = pygame.transform.scale(enemyimg[2], (70, 70))
enemyimg[2] = pygame.transform.rotate(enemyimg[2], 180)

explosion = {}
explosion['lg'] = []
explosion['sm'] = []
explosion['player'] = []
for i in range(9):
    filename = 'regularExplosion/regularExplosion0{}.png'.format(i)
    img = pygame.image.load(path.join(img_dir, filename)).convert()
    img.set_colorkey(BLACK)
    img_lg = pygame.transform.scale(img, (75, 75))
    explosion['lg'].append(img_lg)
    img_sm = pygame.transform.scale(img, (40, 40))
    explosion['sm'].append(img_sm)
    filename = 'sonicExplosion/sonicExplosion0{}.png'.format(i)
    img = pygame.image.load(path.join(img_dir, filename)).convert()
    img.set_colorkey(BLACK)
    explosion['player'].append(img)

live = pygame.image.load("data/powers/life.png")
live = pygame.transform.scale(live, (40, 40))
med = pygame.image.load("data/powers/med.png")
med = pygame.transform.scale(med, (40, 40))
laser = pygame.image.load("data/powers/laser.png")
elaser = pygame.transform.scale(laser, (8, 25))
shield = pygame.image.load("data/powers/shield.png")
shield = pygame.transform.scale(shield, (35, 35))
shootup = pygame.image.load("data/powers/shootup.png")
shootup = pygame.transform.scale(shootup, (35, 35))

#importing sound
shoot_sound = pygame.mixer.Sound("data/music/pew.wav")
power1_sound = pygame.mixer.Sound("data/music/pow1.wav")
power2_sound = pygame.mixer.Sound("data/music/pow2.wav")
exp1_sound = pygame.mixer.Sound("data/music/expl1.wav")
exp2_sound = pygame.mixer.Sound("data/music/expl2.wav")
exp_sound = [exp1_sound, exp2_sound]
pow_sound = [power1_sound, power2_sound]
playerexp_sound = pygame.mixer.Sound("data/music/explosion.wav")
pygame.mixer.music.load("data/music/bkmusic.mp3")
pygame.mixer.music.play(loops =-1)

#making sprites
all_sprites = pygame.sprite.Group()
mob = pygame.sprite.Group()
enemybullets = pygame.sprite.Group()
playerbullets = pygame.sprite.Group()
powerups = pygame.sprite.Group()
explosionsprite = pygame.sprite.Group()

tilesize = 35
score = 0
play = False
