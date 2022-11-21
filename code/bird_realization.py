import pygame
from constants import *

class Bird(pygame.sprite.Sprite):
	def __init__(self, groups, scale_factor):
		super().__init__(groups)

		surf = pygame.image.load('../help/bird.png').convert_alpha()
		self.image = pygame.transform.scale(surf, pygame.math.Vector2(surf.get_size()) * scale_factor)

		self.rect = self.image.get_rect(midleft=(kWindowWidth * kWidthShift, kWindowHeight * kHeightShift))
		self.pos = pygame.math.Vector2(self.rect.topleft)
		self.velocity = 0
		self.mask = pygame.mask.from_surface(self.image)

	def jump(self):
		self.velocity = -kVerticalVelocity

	def update(self, dt):
		self.velocity += kGravitation * dt
		self.pos.y += self.velocity * dt
		self.rect.y = round(self.pos.y)
