import pygame
from load_resources import *
import os, sys
class ship(pygame.sprite.Sprite):
    def __init__(self, x, y, screen, width, height):
	pygame.sprite.Sprite.__init__(self)        
	self.image, self.rect= load_image_rect('graphics/ship.png', -1)	
	self.x= x
	self.y= y
	self.rect.center= self.x, self.y
	self.screen= screen
	self.width= width
	self.height= height
	self.direc= 10
	self.x_time = 0
	self.sound = load_sound('sound/s_crash.wav')
	self.sound.set_volume(.75)
    def update(self):
	self.rect.center= (self.x, self.y)
	if self.x_time < pygame.time.get_ticks() and self.x_time > 0:  
	    self.image= load_image('graphics/ship.png', -1)
	    self.rect.center = self.x, self.y
    def moveL(self):
        if self.x <= 20:
            self.direc= 0
        else:
            self.direc= -10
        self.x= self.x + self.direc
    def moveR(self):
        if self.x >= self.width- 20:
            self.direc= 0
        else:
            self.direc= 10
        self.x= self.x + self.direc
    def my_kill(self, lives):
	self.sound.play()
	if lives >= 1:
	    self.x_time = pygame.time.get_ticks() + 500
	    self.image= load_image('graphics/ship_explosion.png', -1)
	elif lives < 1:
	    self.image= load_image('graphics/ship_explosion.png', -1)
	    self.kill()
	    
