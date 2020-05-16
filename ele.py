import pygame

class ImageEle():

	# 图片大小设置
	__image_size = 50

	def __init__(self, screen, img_index, x, y):
		self.screen = screen
		self.img_index = img_index
		self.image = pygame.image.load('images/element_%s.png' % str(img_index))
		# 图片要进行缩放
		self.image = pygame.transform.scale(self.image, (self.__image_size, self.__image_size))
		self.rect = self.image.get_rect()
		self.x = x
		self.y = y
		self.rect.left = x * self.__image_size
		self.rect.top = y * self.__image_size + 50 
		self.check = False
		self.hide = False

	def draw(self):
		if not self.hide:	
			if self.check:
				pygame.draw.rect(self.image, (0,255,0), (0,0,self.image.get_width()-1,self.image.get_height()-1), 2)
			else:
				pygame.draw.rect(self.image, (0,0,0), (0,0,self.image.get_width()-1,self.image.get_height()-1), 2)
			self.screen.blit(self.image, (self.rect.left, self.rect.top))
		else:
			self.image = pygame.image.load('images/element_0.png')
			self.screen.blit(self.image, (self.rect.left, self.rect.top))
		
	def geo(self):
		return (self.rect.left, self.rect.right, self.rect.top, self.rect.bottom)


