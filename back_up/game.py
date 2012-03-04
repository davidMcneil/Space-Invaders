import pygame
import random
from pygame.locals import *
import ship
import bullet
import enemies
import block
import text
import load_resources
from sys import exit
###
pygame.init()
pygame.key.set_repeat(10, 1)#sets keys to repeat keydown
###Start up variables            
clock = pygame.time.Clock()
width = 800
height = 600
caption = "Space Invaders"
running = True
screen_fill = (0, 0, 0)
linecolor = (255, 255, 255)
###Start up functions
pygame.display.Info
screen = pygame.display.set_mode((width, height), 0, 32)
pygame.display.set_caption(caption)
##Timers
spacebar_timer= pygame.time.get_ticks() + 450
enemy_move_distance = 2.5
enemy_shot_time= 1100
level = 0
enemy2_time = pygame.time.get_ticks() + random.randrange(10000, 30000)	
###Sound effects
###Create background and defines black images to blit over game objects
bg_image= pygame.image.load('/home/david/Programming/Python/space_invaders/graphics/bg.png').convert()
###Instance of ship
s_x= width/2
s_y= height- 70
s= ship.ship(s_x, s_y, screen, width, height)
###instance of score
score= text.score()
###Instance of lives
lives = text.lives()
###Instance of level
level = text.level()
###Sprite groups
sprites= pygame.sprite.RenderUpdates(s, score, lives, level)
blocks= pygame.sprite.Group()
bullets= pygame.sprite.Group()
bombs= pygame.sprite.RenderUpdates()
enemy_group = pygame.sprite.Group()
###Instances of blocks
block.make_wall(75, 450, sprites, blocks, width, height)
block.make_wall(275, 450, sprites, blocks, width, height)
block.make_wall(475, 450, sprites, blocks, width, height)
block.make_wall(675, 450, sprites, blocks, width, height)
###Variables for enemy
e_x= 50
e_y= 50
e_image1= load_resources.load_image("/home/david/Programming/Python/space_invaders/graphics/enemy1.png", -1)
e_image2= load_resources.load_image("/home/david/Programming/Python/space_invaders/graphics/enemy2.png", -1)
e_image3= load_resources.load_image("/home/david/Programming/Python/space_invaders/graphics/enemy3.png", -1)
###Draws start up images
screen.blit(bg_image, (0, 0))
pygame.display.flip()
###Main loop
while running:   	
    for event in pygame.event.get():
        keys_pressed = pygame.key.get_pressed()
        if event.type == QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:    
            if event.key== K_q:
                running = False
            elif event.key== K_ESCAPE:
                running = False
	    if event.key == K_LEFT or keys_pressed[K_LEFT]:
		s.moveL()
	    elif event.key== K_RIGHT or keys_pressed[K_RIGHT]:
		s.moveR()
	    if event.key== K_SPACE or keys_pressed[K_SPACE]:
		if spacebar_timer < pygame.time.get_ticks(): 		
			b= bullet.bullet(screen, -500, -500, width, height, True)
			b.shoot(s.x, s.y)
			sprites.add(b)
			bullets.add(b)
			spacebar_timer= pygame.time.get_ticks() + 450
###Creates UFO 
    if enemy2_time < pygame.time.get_ticks():
	e2 = enemies.enemy2(width, height)
	sprites.add(e2)
	enemy_group.add(e2)
	enemy2_time = pygame.time.get_ticks() + random.randrange(15000, 35000)
###Check for bullets to collide with enemies
    for hit_enemies in pygame.sprite.groupcollide(bullets, enemy_group, True, True).values():
	for e in hit_enemies:	
            score.add(e.get_points())
###Check for ship to collide with bombs    
    for x in pygame.sprite.spritecollide(s, bombs, False):
	print "Your score is %i" % (score.score)
	print "You made it to level %i" % (level.level)
	if lives.lives <= 1:
	    s.kill()
	    running = False
	elif lives.lives > 0:
	    x.kill()
	    lives.sub()		                                                           
###Checks if enemies are on the screen    
    if len(enemy_group) == 0 :
	level.add()
	lives.add()
	enemy_move_distance += 0.5
	if enemy_shot_time > 0:    
	    enemy_shot_time -= 100 
	for j in range(0, 5):
            for i in range(0, 11):
	        if j == 0:         	
	            e= enemies.enemy1(e_image1 , e_x + 50  * i, e_y+ j* 50, screen, width, height, enemy_group, bombs, sprites, 40, enemy_move_distance, enemy_shot_time)
	        elif j == 1 or j == 2:
	            e= enemies.enemy1(e_image2 , e_x + 50  * i, e_y+ j* 50, screen, width, height, enemy_group, bombs, sprites, 20, enemy_move_distance, enemy_shot_time)
	        elif j == 3 or j== 4:     
	            e= enemies.enemy1(e_image3 , e_x + 50  * i, e_y+ j* 50, screen, width, height, enemy_group, bombs, sprites, 10, enemy_move_distance, enemy_shot_time)		
		sprites.add(e)
                enemy_group.add(e)
                e.move()
###Checks if the blocks were hit
    for hit_block in pygame.sprite.groupcollide(blocks, bullets, False, True).keys():
	hit_block.hit()
    for hit_block in pygame.sprite.groupcollide(blocks, bombs, False, True).keys():
	hit_block.hit()
 ###Updates screen
    sprites.clear(screen, bg_image) 
    sprites.update()
    rectlist = sprites.draw(screen)
    pygame.display.update(rectlist)    
    clock.tick(15)
exit()
