import pygame
class lives(pygame.sprite.Sprite):
	def __init__(self):
	    pygame.sprite.Sprite.__init__(self)
	    self.lives= 2
	    self.font = pygame.font.Font(None, 24)
	    self.text = "LIVES: %i" % (self.lives)
	    self.image = self.font.render(self.text, False, (255, 255, 255))
	    self.rect = 715, 573
	def update(self):	
	    self.image = self.font.render("LIVES: %i" % (self.lives), False, (255, 255, 255))
	def sub(self):    
	    self.lives -=  1
	    self.text = "LIVES: %i" % (self.lives)
	def add(self):    
	    self.lives +=  1
	    self.text = "LIVES: %i" % (self.lives)

class score(pygame.sprite.Sprite):
	def __init__(self):
	    pygame.sprite.Sprite.__init__(self)
	    self.score= 0
	    self.font = pygame.font.Font(None, 24)
	    self.text = "SCORE: %i" % (self.score)
	    self.image = self.font.render(self.text, False, (255, 255, 255))
	    self.rect = 100, 573
	def update(self):	
	    self.image = self.font.render("SCORE: %i" % (self.score), False, (255, 255, 255))
	def add(self, points):    
	    self.score += points
	    self.text = "SCORE: %i" % (self.score)

class level(pygame.sprite.Sprite):
	def __init__(self):
	    pygame.sprite.Sprite.__init__(self)
	    self.level= 0
	    self.font = pygame.font.Font(None, 24)
	    self.text = "LEVEL: %i" % (self.level)
	    self.image = self.font.render(self.text, False, (255, 255, 255))
	    self.rect = 15, 573
	def update(self):	
	    self.image = self.font.render("LEVEL: %i" % (self.level), False, (255, 255, 255))
	def add(self):    
	    self.level +=  1
	    self.text = "LEVEL: %i" % (self.level)



