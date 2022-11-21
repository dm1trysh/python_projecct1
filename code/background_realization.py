import pygame
from constants import *

class BackGround(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        bg_image = pygame.image.load('../help/background.png').convert()

        self.image = pygame.transform.scale(bg_image ,(kWindowWidth * kWindowWidthMultiplier ,kWindowHeight * kWindowHeightMultiplier))
        self.rect = self.image.get_rect(topleft = (0 ,0))
        self.pos = pygame.math.Vector2(self.rect.topleft)
