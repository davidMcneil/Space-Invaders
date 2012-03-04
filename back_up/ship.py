import pygame
from load_resources import *
class ship(pygame.sprite.Sprite):
    def __init__(self, x, y, screen, width, height):
	pygame.sprite.Sprite.__init__(self)        
	self.image, self.rect= load_image_rect('/home/david/Programming/Python/space_invaders/graphics/ship.png', -1)	
	self.x= x
	self.y= y
	self.rect.center= self.x, self.y
	self.screen= screen
	self.width= width
	self.height= height
	self.direc= 10  
    def update(self):
	self.rect.center= (self.x, self.y)
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

