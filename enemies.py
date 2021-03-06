import pygame
import random
import bullet
from load_resources import *
class enemy1(pygame.sprite.Sprite):
    def __init__(self,image1, image2, x, y, screen, width, height, group, bomb_group, sprite_group, points, move_distance, shots_time):
	pygame.sprite.Sprite.__init__(self)
	self.image1 = image1
	self.image2= image2
	self.image= image1
	self.move_time = pygame.time.get_ticks() + 400
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
	self.x_time = 0
	self.sound = load_sound('sound/e_shooting.wav')
    def move(self):        
	if not self.moving:
            self.moving= True
            self.update_time= pygame.time.get_ticks()+ 50 
    def update(self):
	if self.moving and self.update_time < pygame.time.get_ticks():
	    if self.move_time < pygame.time.get_ticks() and self.x_time == 0:
		if self.image == self.image1:
		    self.image = self.image2
		else:
		    self.image = self.image1
		self.move_time = pygame.time.get_ticks() + 400    
	    if self.x >= self.width- 30:
                self.reverse_all()
            elif self.x <= 20:
                self.reverse_all()
            self.x= self.x + self.move_distance
            self.rect.center= self.x, self.y
            self.update_time= pygame.time.get_ticks()+ 50
	    x = random.randrange(0, self.shots_time)
	    if x == 1:
                self.sound.play()
		image1 = 'graphics/enemy_bullet1.png'
		image2 = 'graphics/enemy_bullet2.png'
		image = random.choice([image1, image2])
		b1 = load_image(image, -1)
		bomb = bullet.bullet(b1, self.screen, -500, -500, self.width, self.height, False)
                bomb.shoot(self.x, self.y)
                self.sprite_group.add(bomb)
                self.bomb_group.add(bomb)
	    if self.x_time < pygame.time.get_ticks() and self.x_time > 0:  
		self.kill()
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
    def my_kill(self):
	self.x_time = pygame.time.get_ticks() + 175
	self.image = load_image('graphics/enemy_explosion.png', -1)  
	
class enemy2(pygame.sprite.Sprite):
    def __init__(self, width, height):
	pygame.sprite.Sprite.__init__(self)
	self.image, self.rect = load_image_rect("graphics/enemy4.png", -1)
	self.speed = random.choice([7, -7])
	self.points = random.randrange(100, 300, 50)
	self.font = pygame.font.Font(None, 24)
	self.text = "%i" % (self.points)
	self.width = width
	if self.speed == 7:
	      self.x = 0
	elif self.speed == -7:
	      self.x = self.width
	self.y = 25
	self.rect.center= self.x, self.y
	self.update_time = pygame.time.get_ticks() + 50
	self.x_time = 0
	self.sound = load_sound('sound/ufo.wav')
	self.sound.set_volume(.2)
    def update(self):
	if self.update_time < pygame.time.get_ticks():
	    self.sound.play()
	    self.x = self.x + self.speed
            self.rect.center= self.x, self.y
            self.update_time= pygame.time.get_ticks()+ 50
	    if self.x >= self.width or self.x <= 0:
	      self.sound.stop()
	      self.kill()
	    if self.x_time < pygame.time.get_ticks() and self.x_time > 0:  
		self.sound.stop()
		self.kill()
    def reverse(self):
      pass
    def get_points(self):
	return self.points
    def my_kill(self):
	self.sound.stop()
	self.x_time = pygame.time.get_ticks() + 250
	self.image = self.font.render(self.text, False, (255, 255, 255)) 
	


