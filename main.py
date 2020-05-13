import pygame, sys, os
from pygame.locals import *
from random import *

# 设置窗口打开位置
os.environ['SDL_VIDEO_WINDOW_POS'] = "400, 100"

# 初始化
pygame.init()
pygame.mixer.init()
size = w, h = 800, 600
screen = pygame.display.set_mode(size, 0, 32)
pygame.display.set_caption("连连看")
font = pygame.font.SysFont("impact", 24)
FPS = 30
running = False

# 定义颜色
WHITE1 = (255, 255, 255)
WHITE2 = (75, 75, 75)
BLACK = (0, 0, 0)
BULE = (0, 0, 80)

def main():
	clock = pygame.time.Clock()

	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

		screen.fill(BULE)
		pygame.display.update()
		clock.tick(FPS)

if __name__ == "__main__":
	main()
