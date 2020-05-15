import pygame

class ImageEle(pygame.sprite.Sprite):

	# 图片大小设置
	__image_size = 50

	def __init__(self, screen, img_index, x, y):
		super().__init__()
		self.screen = screen
		self.img_index = img_index
		self.image = pygame.image.load('images/element_%s.png' % str(img_index))
		# 图片要进行缩放
		self.image = pygame.transform.scale(self.image, (self.__image_size, self.__image_size))
		self.rect = self.image.get_rect()
		self.x = x
		self.y = y
		self.rect.left = x * self.__image_size + 50 
		self.rect.top = y * self.__image_size + 50 
		self.check = False
		self.hide = False

	def draw(self):
		if self.check:
			pygame.draw.rect(self.image, (50, 50, 50), (0, 0, self.__image_size - 1,self.__image_size - 1), 2)
		
		self.screen.blit(self.image, (self.rect.left, self.rect.top))
		

	def geo(self):
		return (self.rect.left, self.rect.right, self.rect.top, self.rect.bottom)


