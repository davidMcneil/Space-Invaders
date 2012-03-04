import pygame
from load_resources import *
class block(pygame.sprite.Sprite):
    def __init__(self, image, x, y, width, height):
	pygame.sprite.Sprite.__init__(self) 
	self.image= image	
	self.rect= self.image.get_rect()
	self.x = x
	self.y= y
	self.width= width
	self.height = height
	self.hits = 4
    def update(self):
	self.rect.center = self.x, self.y
    def hit(self):
	self.hits -= 1
	if self.hits == 3:
	    self.image, self.rect = load_image_rect("graphics/Blocks/block2.png")
	elif self.hits == 2:
	    self.image, self.rect = load_image_rect("graphics/Blocks/block3.png")
	elif self.hits == 1:
	    self.image, self.rect = load_image_rect("graphics/Blocks/block4.png")
	elif self.hits == 0:
	    self.kill()

def make_wall(x, y, sprites, blocks, width, height):
     image = load_image("graphics/Blocks/block.png")
     image_top_left = load_image("graphics/Blocks/block_top_left.png")
     image_top_right = load_image("graphics/Blocks/block_top_right.png")
     image_bottom_left = load_image("graphics/Blocks/block_bottom_left.png")
     image_bottom_right = load_image("graphics/Blocks/block_bottom_right.png")
     for j in range(0, 3):###Rows
	for i in range(0, 4):###Columns        	
	    if (i==1 or i==2) and j == 2:
		pass
	    elif i == 0 and j == 0:
		b= block(image_top_left, x + i * 13, y + j * 13, width, height)    		
		sprites.add(b)
		blocks.add(b)
	    elif i == 3 and j == 0:
		b= block(image_top_right, x + i * 13, y + j * 13, width, height)    		
		sprites.add(b)
		blocks.add(b)
	    elif i == 1 and j == 1:
		b= block(image_bottom_left, x + i * 13, y + j * 13, width, height)    		
		sprites.add(b)
		blocks.add(b)
	    elif i == 2 and j == 1:
		b= block(image_bottom_right, x + i * 13, y + j * 13, width, height)    		
		sprites.add(b)
		blocks.add(b)
	    else:
		b= block(image, x + i * 13, y + j * 13, width, height)    		
		sprites.add(b)
		blocks.add(b)
