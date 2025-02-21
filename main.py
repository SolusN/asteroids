# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")

	clock = pygame.time.Clock()
	dt = 0
	while True:
		print("start of loop")
		print("dt=clock.tick")
		dt = clock.tick(60) / 1000 # an error here somewhere
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		print("before screen.fill")
		screen.fill((0,0,0))
		print("after screen.fill")
		
		print("before display.flip")
		pygame.display.update()
		print("after display.flip")
		print("end of loop")
if __name__ == "__main__":
	main()
