import pygame
import os
import pkg_resources
from textures import *
from maps import *

pList = sorted(["%s==%s" % (i.key, i.version) for i in pkg_resources.working_set])
if 'pygame==2.1.2' not in pList:
	os.system('pip install pygame')

pygame.init()
sc_width, sc_height = 832, 672
row, coulumn = int(sc_width / 32), int(sc_height / 32)
sc = pygame.display.set_mode((sc_width, sc_height))
pygame.display.set_caption("Texture Renderer Test [ESC or Quit Button to Quit]")

def render_test_map():
	for i in range(coulumn):
		for j in range(row):
			pos = (j*32, i*32)

			if(test_map[i][j] == 0):
				sc.blit(grass, pos)

			elif(test_map[i][j] == 1):
				sc.blit(dirt, pos)

			elif(test_map[i][j] == 2):
				sc.blit(snow, pos)

			elif(test_map[i][j] == 3):
				sc.blit(water, pos)

			elif(test_map[i][j] == 4):
				sc.blit(cobble, pos)

			elif(test_map[i][j] == 5):
				sc.blit(stone_brick, pos)

			elif(test_map[i][j] == 6):
				sc.blit(dead_grass, pos)

			elif(test_map[i][j] == 7):
				sc.blit(plank, pos)

			elif(test_map[i][j] == 8):
				sc.blit(brick, pos)

	pygame.display.update()

def main():
	while 1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				os._exit(0)

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					pygame.quit()
					os._exit(0)

		render_test_map()

if __name__ == '__main__':
	main()