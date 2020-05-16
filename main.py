import pygame, sys, os
from pygame.locals import *
from random import *

import ele

# 设置窗口打开位置
os.environ['SDL_VIDEO_WINDOW_POS'] = "300, 100"

# 初始化
pygame.init()
pygame.mixer.init()
size = w, h = 800, 600
screen = pygame.display.set_mode(size, 0, 32)
pygame.display.set_caption("连连看")
font = pygame.font.SysFont("impact", 32)
FPS = 30
clicked = None
score = 0
time = 60000

# 定义颜色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

link_sound = pygame.mixer.Sound('sound/link.WAV')
link_sound.set_volume(1)

# 初始化元素
# 图片大小需要改变
image_size = 50
image_number = 14 * 10
def init_map():
	l_list = []
	map_list = []
	map_index = []
	for i in range(0, image_number, 2):
		e = randint(1, 12)
		# 每次添加一对儿
		l_list.append(e)
		l_list.append(e)
	# 打乱顺序
	shuffle(l_list)
	# 构建完整图
	for i in range(10):
		temp1 = []
		temp2 = []
		for j in range(14):
			# temp.append(l_list.pop())
			temp1.append(ele.ImageEle(screen, l_list.pop(), j, i))
			temp2.append(True)
		map_list.append(temp1)
		map_index.append(temp2)

	return map_list, map_index

def draw_map(map_list):
	for l in map_list:
		for e in l:
			e.draw()

def print_text(font, x, y, text, color = WHITE):
	ti = font.render(text, True, color)
	screen.blit(ti, (x, y))

def scan(e1, e2, map_index):
	goal = []
	# 向右探索
	for i in range(e2.x + 1, 14):
		if map_index[e2.y][i] == True:
			break
		else:
			goal.append((i, e2.y))
	# 向左
	for i in range(e2.x - 1, -1, -1):
		if map_index[e2.y][i] == True:
			break
		else:
			goal.append((i, e2.y))
	# 向上
	for i in range(e2.y - 1, -1, - 1):
		if map_index[i][e2.x] == True:
			break
		else:
			goal.append((e2.x, i))
	# 向下
	for i in range(e2.y + 1, 10):
		if map_index[i][e2.x] == True:
			break
		else:
			goal.append((e2.x, i))
	# 扫描原点
	# 向右探索
	for i in range(e1.x + 1, 14):
		if map_index[e1.y][i] == True:
			break
		elif (i, e1.y) in goal:
			return True
		else:
			continue
	# 向左
	for i in range(e1.x - 1, -1, -1):
		if map_index[e1.y][i] == True:
			break
		elif (i, e1.y) in goal:
			return True
		else:
			continue
	# 向上
	for i in range(e1.y - 1, -1, -1):
		if map_index[i][e1.x] == True:
			break
		elif (e1.x, i) in goal:
			return True
		else:
			continue
	# 向下
	for i in range(e1.y + 1, 10):
		if map_index[i][e1.x] == True:
			break
		elif (e1.x, i) in goal:
			return True
		else:
			continue

	if e1.x == e2.x and abs(e1.y - e2.y) == 1:
		return True
	elif e1.y == e2.y and abs(e1.x - e2.x) == 1:
		return True
	return False

# 检查两个是否匹配

def can_clear(e1, e2, map_index):
	# 图片不一致不会消除
	if e1.img_index != e2.img_index:
		return False
	else:
		if scan(e1, e2, map_index):
			return True
		else:
			return False

def check(map_list, map_index):
	global clicked, score, time
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				pygame.quit()
				sys.exit()				
		elif event.type == MOUSEBUTTONDOWN:
			pos = event.pos
			for l in map_list:
				for e in l:
					geo = e.geo()
					if geo[0] < pos[0] < geo[1] and geo[2] < pos[1] < geo[3]:
						if not e.hide:
							if e.check:
								e.check = False
								clicked = None
								break
							else:
								if clicked:
									if can_clear(clicked, e, map_index):
										link_sound.play()
										#标记位置清除
										map_index[e.y][e.x] = False
										map_index[clicked.y][clicked.x] = False
										clicked.hide = True
										e.hide = True
										clicked = None
										score += 100
										time += 2000
									else:
										clicked.check = False
										clicked = None
								else:
									e.check = True
									clicked = e
								break

# 初始化数据
def init():
	global clicked, score, time
	clicked = None
	score = 0
	time = 60000

def main():
	global time
	clock = pygame.time.Clock()
	map_list, map_index = init_map()
	gameover = False

	while True:
		screen.fill(BLACK)
		if not gameover:
			check(map_list, map_index)
			print_text(font, 50, 0, "Score: " + str(score))
			print_text(font, 600, 0, "Time: " + str(time // 1000))
			# 绘所有图
			draw_map(map_list)
			if score == 7000:
				gameover = True
			time -= 30
			if time <= 0:
				gameover = True
		else:
			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.exit()
				elif event.type == KEYDOWN:
					if event.key == K_r:
						init()
						main()
				elif event.type == KEYDOWN:
					if event.key == K_ESCAPE:
						pygame.quit()
						sys.exit()
			print_text(font, 300, 200, "Game Over !")
			print_text(font, 300, 250, "Your Score: " + str(score))
			print_text(font, 280, 300, "Press R To Restart")	
	
		pygame.display.update()
		clock.tick(FPS)

if __name__ == "__main__":
	main()