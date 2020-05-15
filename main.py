import pygame, sys, os
from pygame.locals import *
from random import *

import ele

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
BULE = (0, 0, 50)

# 初始化元素
# 图片大小需要改变
image_size = 50
image_number = 14 * 10
def init_map():
	l_list = []
	map_list = []
	for i in range(0, image_number, 2):
		e = randint(1, 12)
		# 每次添加一对儿
		l_list.append(e)
		l_list.append(e)
	# 打乱顺序
	shuffle(l_list)
	# 构建完整图
	for i in range(10):
		temp = []
		for j in range(14):
			# temp.append(l_list.pop())
			temp.append(ele.ImageEle(screen, l_list.pop(), j, i))
		map_list.append(temp)

	return map_list

def draw_map(map_list):
	for l in map_list:
		for e in l:
			e.draw()

def check(map_list):
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == MOUSEBUTTONDOWN:
			pos = event.pos
			for l in map_list:
				for e in l:
					geo = e.geo()
					if geo[0] < pos[0] < geo[1] and geo[2] < pos[1] < geo[3]:
						e.check = not e.check


def main():
	clock = pygame.time.Clock()

	map_list = init_map()

	while True:
		
		check(map_list)
		screen.fill(BULE)
		# 绘所有图
		draw_map(map_list)		
		pygame.display.update()
		clock.tick(FPS)

if __name__ == "__main__":
	main()
