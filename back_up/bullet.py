import pygame
import random
from load_resources import *
class bullet(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, width, height, up):
	pygame.sprite.Sprite.__init__(self)          
	self.image, self.rect= load_image_rect('/home/david/Programming/Python/space_invaders/graphics/bullet.png', None)	
	self.screen= screen
        self.x= x
        self.y= y
	self.width= width
	self.height= height	
	self.rect.center= self.x, self.y
        self.speed= 0
        self.shooting= False
        self.update_time= pygame.time.get_ticks()+ 50
	self.up= up
    def shoot(self, ship_x, ship_y):
        if not self.shooting:
	    self.x= ship_x
	    self.y= ship_y - 15            
	    self.rect.center= self.x, self.y
            self.shooting= True 
    def update(self):       
	if self.y > 1 and self.update_time < pygame.time.get_ticks() and self.shooting:
           if self.up: 
		self.speed = -20	        
		self.y = self.y + self.speed	 
	        self.rect.center= self.x, self.y
                self.update_time= pygame.time.get_ticks() + 50
	   elif not self.up:
		self.speed = 20		
		self.y = self.y + self.speed	 
	        self.rect.center= self.x, self.y
                self.update_time= pygame.time.get_ticks() + 50
	if self.up:	    
	    if self.y < 1:    
	        self.shooting= False
	        self.kill()
	elif not self.up:
	    if self.y > self.width:    
	        self.shooting= False
	        self.kill() 
