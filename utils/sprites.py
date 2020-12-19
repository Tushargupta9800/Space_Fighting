#by- Team Algoristy
#Space Fighting game in python using pygame

#importing libraries
from utils.setandvar import*
from utils.widgets import*
from utils.history import*
from utils.http import*
import pygame
import random
pygame.init()
global music

class Pbullet(pygame.sprite.Sprite):
    def __init__ (self, x, space):
        pygame.sprite.Sprite. __init__ (self)
        self.image = elaser
        self.rect = self.image.get_rect()
        self.rect.center = x
        self.rect.centerx += space
        self.speed = -7

    def update(self):
        self.rect.y += self.speed

        if self.rect.top <= 0:
            self.kill()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = playerimg
        self.rect = self.image.get_rect()
        self.radius = 35
        self.rect.centerx = width/2
        self.rect.bottom = height - 10
        self.speed = 0
        self.shield = 100
        self.life = 3
        self.power = 1
        self.hidden = False
        self.shieldon = False
        self.last_shot = pygame.time.get_ticks()
        self.hide_time = pygame.time.get_ticks()
        self.power_time_shoot = pygame.time.get_ticks()
        self.power_time_shield = pygame.time.get_ticks()
        self.time = pygame.time.get_ticks()
        self.show_time = 0
        self.menu = False
        self.music = 1

    def update(self):
        if self.life == 0:
            self.menu = True
            self.hidden = True
            self.hide_time = pygame.time.get_ticks()
            
        if self.hidden and pygame.time.get_ticks()- self.hide_time > 1000:
                self.hidden = False
                self.rect.centerx = width/2
                self.rect.bottom = height - 10
                

        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] and pygame.time.get_ticks() - self.time >= 250:
            self.time = pygame.time.get_ticks()
            if self.music == 1:
                shoot_sound.play()
            if self.power == 1 or self.power == 2:
                pbullet = Pbullet(self.rect.center,0)
                all_sprites.add(pbullet)
                playerbullets.add(pbullet)
            elif self.power == 3 and pygame.time.get_ticks() - self.power_time_shoot <= 7000:
                pbullet1 = Pbullet(self.rect.center,23)
                pbullet2 = Pbullet(self.rect.center,-23)
                all_sprites.add(pbullet1, pbullet2)
                playerbullets.add(pbullet1, pbullet2)
            else:
                self.power = 1
        
        if key[pygame.K_RIGHT]:
            self.rect.x += 5
            if self.rect.right >= width:
                self.rect.right = width
        if key[pygame.K_LEFT]:
            self.rect.x -= 5
            if self.rect.left <= 0:
                self.rect.left = 0

    def hide(self):
        self.shieldon = True
        self.power = 2
        self.power_time_shield  = pygame.time.get_ticks()
        writeonscreen('OOPS! You Died',width/2, height/2 - 50, 30)
        self.rect.x = 1000

class Ebullet(pygame.sprite.Sprite):
    def __init__ (self, x):
        pygame.sprite.Sprite. __init__ (self)
        self.image = elaser
        self.rect = self.image.get_rect()
        self.rect.center = x
        self.speed = 10

    def update(self):
        self.rect.y += self.speed

        if self.rect.top >= height:
            self.kill()

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = random.choice(enemyimg)
        self.rect = self.image.get_rect()
        self.radius = 30
        self.rect.top = -100
        i = random.randrange(100, 400) 
        self.rect.left = i
        self.bullet = False
        self.bullet_time = pygame.time.get_ticks()
        self.speedx = random.randrange(-2, 2)
        self.speedy = random.randrange(1, 5)
        self.shieldon = True

    def update(self):
        if self.bullet:
            self.bullet = False
            if self.rect.top <= 400 and self.shieldon:
                ebullet = Ebullet(self.rect.center)
                all_sprites.add(ebullet)
                enemybullets.add(ebullet)

        if not self.bullet and pygame.time.get_ticks() - self.bullet_time > 1500:
            self.bullet_time = pygame.time.get_ticks()
            self.bullet = True

        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.y >= height or self.rect.right <= 0 or self.rect.left >= width:
            self.kill()
            a = Enemy()
            mob.add(a)
            all_sprites.add(a)

class Explosion(pygame.sprite.Sprite):
        def __init__(self, x, size, prin):
            pygame.sprite.Sprite.__init__(self)
            self.size = size
            self.x = x
            self.frame = 0
            self.image = explosion[self.size][self.frame]
            self.rect = self.image.get_rect()
            self.rect.center = x
            self.time = pygame.time.get_ticks()
            self.text = prin

        def update(self):
            writeonscreen(self.text,width/2, height/2, 30)
            if pygame.time.get_ticks() - self.time >= 100:
                self.frame += 1
                if self.frame == len(explosion[self.size]) - 1:
                    self.kill()
                self.image = explosion[self.size][self.frame]

class Powerup(pygame.sprite.Sprite):
    def __init__ (self, center, text):
        pygame.sprite.Sprite. __init__ (self)
        if text == 'shield':
            self.image = shield
        elif text == 'med':
            self.image = med
        elif text == 'live':
            self.image = live
        else:
            self.image = shootup

        self.rect = self.image.get_rect()
        self.rect.center = center
        self.speed = 5

    def update(self):
        self.rect.y += self.speed

def makeenemy():
    a = Enemy()
    all_sprites.add(a)
    mob.add(a)

def makeexplosion(x, text, prin):
    a = Explosion(x, text, prin)
    all_sprites.add(a)
    explosionsprite.add(a)

def drop(center, text):
    a = Powerup(center, text)
    all_sprites.add(a)
    powerups.add(a)
        
def printhistory():
    wait = True
    ignite = pygame.time.get_ticks()
    index = 0
    max_index = 7 
    while wait:
        clock.tick(10)
        win.blit(bk, (0,0))
        win.blit(back, (20,20))
        win.blit(next_img, (width - 100, 150))
        win.blit(games_img[index], (150, 80))
        writeonscreen("Little History", width/2 + 10, 50, 30)
        writeonscreen(game_name[index] , 250, 345, 15)
        historytxt()
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_q:
                    pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if x > 20 and x < 85 and y > 20 and y < 85:
                    wait = False
                if x > width - 100 and x < width - 50 and y > 150 and y < 200:
                    index += 1
                    index = index%max_index
            if event.type == pygame.QUIT:
                pygame.quit()
        if pygame.time.get_ticks() - ignite > 500:
            makeexplosion((random.randrange(50, 450), random.randrange(50, 550)), 'lg', '')
            ignite = pygame.time.get_ticks()
        explosionsprite.update()
        explosionsprite.draw(win)
        pygame.display.flip()
        pygame.display.update()
        
def showmenu(score, play, player):
    internet = checkInternet()
    #if internet == 1:
        #data = getall()
    wait = True
    ignite = pygame.time.get_ticks()
    while wait:
        win.blit(bk, (0,0))
        writeonscreen("Space Fighting", width/2, 40, 60)
        fp = open("data/score.txt", "r")
        high_score = fp.read()
        high_score = int(high_score, base = 10)
        fp.close()
        if play:
            if high_score <= score:
                fp = open("data/score.txt", "w+")
                fp.truncate(0)
                fp.write(str(score))
                fp.close()
                writeonscreen("Congrats! You made a new High Score", width/2, 230, 28)
                high_score = score
                writeonscreen("Your score: ", width/2 - 15, 280, 50)
                if data[9]["score"] <= score:
                    writeonscreen("Congrats you have made a World Score", width/2, 335, 25)
                    writeonscreen("_____________________________________", width/2, 340, 25)
                    writeonscreen("_____________________________________", width/2, 335, 25)
                font = pygame.font.match_font('arial')
                fonter = pygame.font.Font(font, 45)
                makesurface = fonter.render(str(score), True, (255, 255, 0))
                text_rect = makesurface.get_rect()
                text_rect.left = width/2 + 85
                text_rect.centery = 280
                win.blit(makesurface, text_rect)
            else:
                font = pygame.font.match_font('arial')
                fonter = pygame.font.Font(font, 43)
                makesurface = fonter.render(str(high_score), True, (255, 255, 0))
                text_rect = makesurface.get_rect()
                text_rect.left = width/2 + 45
                text_rect.centery = 250
                writeonscreen("Better Luck Next Time", width/2, 200, 40)
                writeonscreen("Highscore: ", width/2 - 35, 250, 40)
                if data[9]["score"] <= score:
                    writeonscreen("Congrats you have made a World Score", width/2, 340, 25)
                    writeonscreen("_____________________________________", width/2, 340, 25)
                    writeonscreen("_____________________________________", width/2, 345, 25)
                win.blit(makesurface, text_rect)
                writeonscreen("Your score: ", width/2 - 35, 300, 40)
                makesurface = fonter.render(str(score), True, (255, 0, 255))
                text_rect = makesurface.get_rect()
                text_rect.left = width/2 + 50
                text_rect.centery = 300
                win.blit(makesurface, text_rect)
        else:
            writeonscreen("CONTROLS:", width/2, 200, 35)
            writeonscreen("Use Space bar to shoot", width/2, 250, 30)
            writeonscreen("Use arrow keys to move", width/2, 280, 30)
            writeonscreen("Prev Highscore: ", width/2 - 30, 330, 35)
            font = pygame.font.match_font('arial')
            fonter = pygame.font.Font(font, 35)
            makesurface = fonter.render(str(high_score), True, (255, 255, 0))
            text_rect = makesurface.get_rect()
            text_rect.left = width/2 + 75
            text_rect.centery = 330
            win.blit(makesurface, text_rect)

        win.blit(playerimg, (width/2 - 52, 450))
        win.blit(enemyimg[0], (135, 92))
        win.blit(enemyimg[1], (205, 85))
        win.blit(enemyimg[2], (290, 90))
        win.blit(speaker, (30,100))
        win.blit(history, (width - 100, 85))
        if player.music == 0:
            win.blit(no_sound, (20,90))
        writeonscreen("By- Team Algoristy", 370, 572, 30)
        writeonscreen("Use 's' to pause and 'e' to end the game", width/2, 410, 20)
        writeonscreen("Press 'p' to play and 'q' to quit the game", width/2, 380, 20)
        clock.tick(10)
        if pygame.time.get_ticks() - ignite > 500:
            makeexplosion((random.randrange(50, 450), random.randrange(50, 550)), 'lg', '')
            ignite = pygame.time.get_ticks()
        toprint = [med, shield, shootup, live]
        for i in range (0, 4):
            win.blit(toprint[i], (50 + i*42, 550)) 
        explosionsprite.update()
        explosionsprite.draw(win)
        pygame.display.flip()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if x > width - 100 and x < width - 20 and y > 85 and y < 175:
                    printhistory()
                if x > 30 and x < 85 and y > 90 and y < 140:
                    player.music = 1 - player.music
                    if player.music == 0:
                        pygame.mixer.music.pause()
                    if player.music == 1:
                        pygame.mixer.music.unpause()
                
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_p:
                    wait = False
                elif event.key == pygame.K_q:
                    pygame.quit()
