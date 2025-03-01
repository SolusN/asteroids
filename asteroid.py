import pygame
from circleshape import CircleShape
from constants import *
import random


class Asteroid(CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)

	def draw(self, screen):
		pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2)
	
	def update(self, dt):
		self.position += (self.velocity * dt)
	def split(self):
		self.kill()
		if self.radius <= ASTEROID_MIN_RADIUS:
			return
		rand_angle = random.uniform(20,50)
		first_new_angle = (self.velocity * rand_angle)
		second_new_angle = (self.velocity * -rand_angle)
		new_radius = self.radius - ASTEROID_MIN_RADIUS

		ast_one = Asteroid(self.position.x, self.position.y, new_radius)
		ast_two = Asteroid(self.position.x, self.position.y, new_radius)

		ast_one.velocity = (first_new_angle * 0.8)
		ast_two.velocity = (second_new_angle * 0.8)

