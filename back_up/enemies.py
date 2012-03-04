import pygame
import random
import bullet
from load_resources import *
class enemy1(pygame.sprite.Sprite):
    def __init__(self,image, x, y, screen, width, height, group, bomb_group, sprite_group, points, move_distance, shots_time):
	pygame.sprite.Sprite.__init__(self)
	self.image= image	
	self.rect= self.image.get_rect()	
	self.x= x
	self.y= y
	self.rect.center= self.x, self.y
	self.width= width
	self.height= height	
	self.moving= False	
	self.group= group
	self.reverse_time= 0
	self.bomb_group= bomb_group
	self.sprite_group= sprite_group
	self.screen= screen
	self.points= points
	self.move_distance= move_distance
	self.shots_time= shots_time	
    def move(self):        
	if not self.moving:
            self.moving= True
            self.update_time= pygame.time.get_ticks()+ 50 
    def update(self):
	if self.moving and self.update_time < pygame.time.get_ticks():
            if self.x >= self.width- 30:
                self.reverse_all()
            elif self.x <= 20:
                self.reverse_all()
            self.x= self.x + self.move_distance
            self.rect.center= self.x, self.y
            self.update_time= pygame.time.get_ticks()+ 50
	    x = random.randrange(0, self.shots_time)
	    if x == 1:
                bomb = bullet.bullet(self.screen, -500, -500, self.width, self.height, False)
                bomb.shoot(self.x, self.y)
                self.sprite_group.add(bomb)
                self.bomb_group.add(bomb)
    def reverse_all(self):
	if self.reverse_time < pygame.time.get_ticks():		
	    for x in self.group:
	        x.reverse()
    def reverse(self):
	self.move_distance= -self.move_distance
	self.y += 20
	self.reverse_time= pygame.time.get_ticks()+ 100
    def get_points(self):
	return self.points

class enemy2(pygame.sprite.Sprite):
    def __init__(self, width, height):
	pygame.sprite.Sprite.__init__(self)
	self.image, self.rect = load_image_rect("/home/david/Programming/Python/space_invaders/graphics/enemy4.png", -1)
	self.speed = random.choice([7, -7])
	self.speed = -7
	self.points = random.randrange(100, 300, 50)
	self.width = width
	if self.speed == 7:
	      self.x = 0
	elif self.speed == -7:
	      self.x = self.width
	self.y = 25
	self.rect.center= self.x, self.y
	self.update_time = pygame.time.get_ticks() + 50
    def update(self):
	if self.update_time < pygame.time.get_ticks():
	    self.x = self.x + self.speed
            self.rect.center= self.x, self.y
            self.update_time= pygame.time.get_ticks()+ 50
	    if self.x >= self.width or self.x <= 0:
	      self.kill()
    def reverse(self):
      pass
    def get_points(self):
	return self.points

