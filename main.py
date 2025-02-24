# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from player import Player
from constants import *
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")

	
	clock = pygame.time.Clock()
	dt = 0

	
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroid_container = pygame.sprite.Group()

	Player.containers = (updatable, drawable)
	Asteroid.containers = (updatable, drawable, asteroid_container)
	AsteroidField.containers = (updatable)

	my_player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	game_asteroid_field = AsteroidField()

	try:
		while True:
			dt = clock.tick(60) / 1000 # an error here somewhere
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					return
			screen.fill((0,0,0))
			updatable.update(dt)
			for ast in asteroid_container:
			    if ast.check_collision(my_player):
				print("Game OVER!")
				pygame.quit()
			for sprite in drawable:
				sprite.draw(screen)
			pygame.display.update()
	except KeyboardInterrupt:
		print("Game loop interrupted. Quitting...")
	finally:
		pygame.quit()

if __name__ == "__main__":
	main()
