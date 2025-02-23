# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import player
from constants import *

def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")

	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)


	clock = pygame.time.Clock()
	dt = 0
	try:
		while True:
			dt = clock.tick(60) / 1000 # an error here somewhere
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					return
			screen.fill((0,0,0))
			
			player.draw(screen)
			pygame.display.update()
	except KeyboardInterrupt:
		print("Game loop interrupted. Quitting...")
	finally:
		pygame.quit()

if __name__ == "__main__":
	main()
