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

def print_text(font, x, y, text, color = WHITE):
	ti = font.render(text, True, color)
	screen.blit(ti, (x, y))

def v_scan(e1, e2):
	if e1.x == e2.x:
		return True

	return False

def h_scan(e1, e2):
	if e1.y == e2.y:
		return True

	return False

# 检查两个是否匹配
def can_clear(e1, e2):
	# 图片不一致不会消除
	if e1.img_index != e2.img_index:
		return False
	else:
		# 垂直扫描和水平扫描，一个成功即可
		if v_scan(e1, e2) or h_scan(e1, e2):
			return True
		else:
			return False

def check(map_list):
	global clicked, score, time
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
						if not e.hide:
							if e.check:
								e.check = False
								clicked = None
								break
							else:
								if clicked:
									if can_clear(clicked, e):
										link_sound.play()
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
	map_list = init_map()
	gameover = False

	while True:
		screen.fill(BLACK)
		if not gameover:
			check(map_list)
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
			print_text(font, 300, 200, "Game Over !")
			print_text(font, 300, 250, "Your Score: " + str(score))
			print_text(font, 280, 300, "Press R To Restart")	
	
		pygame.display.update()
		clock.tick(FPS)

if __name__ == "__main__":
	main()