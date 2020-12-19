#by- Team Algoristy
#Space Fighting game in python using pygame

import pygame
pygame.init()
from random import randint
from utils.setandvar import*
from utils.sprites import*
from utils.widgets import*

play = False
#main loop
loop = True
run = True
score = 0
music = 1

def displaymenu():
    global player
    player = Player()
    player.life = 3
    player.shield = 100
    all_sprites.add(player)
    for i in range (1, 8):
        makeenemy()
        
displaymenu()

if run:
    showmenu(score, play, player)
    music = player.music

while loop:
    if not run:
        showmenu(score, play, player)
        music = player.music
        run = True

    run = True
    player.life = 3
    player.shield = 100
    player.menu = False
    score = 0
    player.power = 2
    player.shieldon = True
    player.music = music
    player.power_time_shield = pygame.time.get_ticks()
                
    #game loop
    while run:
        keypressed = pygame.key.get_pressed()
        if keypressed[pygame.K_s]:
            pausethescreen()
        if keypressed[pygame.K_e]:
            music = player.music
            for bullet in playerbullets:
                bullet.kill()
            for enemy in mob:
                enemy.kill()
            for i in range (1, 8):
                makeenemy()
            run = False
        play = True
        if player.shieldon:
            for m in mob:
                m.shieldon = False
        else:
            for m in mob:
                m.shieldon = True
        clock.tick(fps)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        hits = pygame.sprite.groupcollide(mob, playerbullets, True, True)
        for i in hits:
            if player.music == 1:
                random.choice(exp_sound).play()
            k =  random.randrange(5, 10)
            score += k
            j = random.randrange(1, 100)
            if j <= 2:
                k = random.randrange(1, 50)
                if k <= 5:
                    drop(i.rect.center,'shield')
                elif k <= 10:
                    drop(i.rect.center, 'live')
            elif j <= 4:
                drop(i.rect.center,'shootup')
            elif j < 6:
                drop(i.rect.center, 'med')
                
            makeenemy()
            makeexplosion(i.rect.center, 'lg', '')
        win.blit(bk, (0,0))
        if not player.shieldon:
            hits = pygame.sprite.spritecollide(player, enemybullets, True, pygame.sprite.collide_circle)
            for i in hits:
                if player.music == 1:
                    random.choice(exp_sound).play()
                player.shield -= 20
                makeexplosion(i.rect.bottomright, 'sm', '-20')
        if not player.shieldon:
            hits = pygame.sprite.spritecollide(player, mob, True, pygame.sprite.collide_circle)
            for i in hits:
                makeenemy()
                player.shield -= 50
                makeexplosion(i.rect.center, 'player', '-50')

        #hits = pygame.sprite.groupcollide(playerbullets, powerups, True,  True)
        #for i in hits:
        #    makeexplosion(i.rect.center, 'sm', 'OOPS!')

        hits = pygame.sprite.spritecollide(player, powerups, True, pygame.sprite.collide_circle)
        for i in hits:
            if player.music == 1:
                random.choice(pow_sound).play()
            if i.image == shield:
                player.power = 2
                player.shieldon = True
                player.power_time_shield = pygame.time.get_ticks()
            elif i.image == shootup:
                player.power_time_shoot = pygame.time.get_ticks()
                player.power = 3
            elif i.image == live:
                player.life += 1
                if player.life > 4:
                    player.life = 4
                writeonscreen('1 Life Up!!', width/2, height/2 - 100, 30)
            else:
                writeonscreen('Health up!', width/2, height/2 + 50, 30)
                clock.tick(10)
                player.shield += 30
                
                if player.shield >= 100:
                    player.shield = 100
        if player.power == 3:
            print_time_elapsed(int((pygame.time.get_ticks() - player.power_time_shoot)/71),'Double Shoot', 77, 87, 69)
        if player.hidden:
            player.hide()

        if player.shieldon:
            time_elapsed = int((pygame.time.get_ticks() - player.power_time_shield)/71)
            print_time_elapsed(time_elapsed,'Shield', 48, 57, 48)

        if player.shieldon and pygame.time.get_ticks() - player.power_time_shield >=7000:
            player.shieldon = False
        
        all_sprites.update()
        all_sprites.draw(win)
        pygame.display.flip()
        writeonscreen(str(score),width/2, 30, 30)
        writeonscreen("Score", width/2, 54, 25)
        if displayhealth(player.shield):
            music = player.music
            if player.music == 1:
                playerexp_sound.play()
            player.life -= 1
            player.shield =100
            player.hidden = True
            player.hide_time = pygame.time.get_ticks()
        displaylives(player.life)
        pygame.display.update()

        if not player.alive():
            music = player.music
            pygame.quit()

        if player.menu:
            music = player.music
            run = False
