import pygame
from constants import *
import random

class Barrier(pygame.sprite.Sprite):
    def __init__(self, groups, scale_factor):
        super().__init__(groups)
        self.sprite_type = 'barrier'
        surf = pygame.image.load('../help/barrier.png').convert_alpha()
        self.image = pygame.transform.scale(surf, pygame.math.Vector2(surf.get_size()) * scale_factor)

        generated_values = self.generate_parametres()
        self.creating_rect(generated_values)
        self.pos = pygame.math.Vector2(self.rect.topleft)
        self.mask = pygame.mask.from_surface(self.image)

    def generate_parametres(self):
        direction = 0 if random.uniform(0, 1) < 0.5 else 1
        x_value = int(random.uniform(kMinWidthTube, kMaxWidthTube))
        y_value = int(random.uniform(kMinHeightTube, kMaxHeightTube))
        initialized_values = (direction, x_value, y_value)
        return initialized_values

    def creating_rect(self, generated_values):
        x_coord = kWindowWidth + generated_values[1]
        direction_tube = generated_values[0]
        if direction_tube == 1:
            y_coord = generated_values[2] * (-1)
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect = self.image.get_rect(midtop=(x_coord, y_coord))
        else:
            y_coord = kWindowHeight + generated_values[2]
            self.rect = self.image.get_rect(midbottom=(x_coord, y_coord))


    def update(self, dt):
        self.pos.x -= kHorizontalVelocity * dt
        self.rect.x = round(self.pos.x)
        if self.rect.right <= kEndedOnScreen:
            self.kill()
