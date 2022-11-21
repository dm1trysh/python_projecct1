import pygame, sys, time
from constants import *
from barrier_realization import Barrier
from background_realization import BackGround
from bird_realization import Bird

class Game:
	def __init__(self):
		pygame.init()
		self.display_surface = pygame.display.set_mode((kWindowWidth, kWindowHeight))
		pygame.display.set_caption('Flappy Bird')
		self.clock = pygame.time.Clock()
		self.active = True
		self.all_sprites = pygame.sprite.Group()
		self.collision_sprites = pygame.sprite.Group()

		bg_height = pygame.image.load('../help/background.png').get_height()
		self.scale_factor = kWindowHeight / bg_height

		BackGround(self.all_sprites)
		self.bird = Bird(self.all_sprites, self.scale_factor * kBirdScale)
		self.barrier_timer = pygame.USEREVENT + 1
		pygame.time.set_timer(self.barrier_timer, 1400)

		self.font = pygame.font.Font('../help/BD_Cartoon_Shout.ttf', 30)
		self.font_for_big_text = pygame.font.Font('../help/BD_Cartoon_Shout.ttf', 50)
		self.score = 0
		self.start_offset = 0

	def collisions(self):
		if pygame.sprite.spritecollide(self.bird, self.collision_sprites, False, pygame.sprite.collide_mask) \
			or self.bird.rect.top <= 0 or self.bird.rect.bottom >= kWindowHeight:
			for sprite in self.collision_sprites.sprites():
				if sprite.sprite_type == 'barrier':
					sprite.kill()
			self.active = False
			self.bird.kill()

	def display_score(self):
		y = kWindowHeight * kScoreMultiply
		if self.active:
			self.score = (pygame.time.get_ticks() - self.start_offset) // 1000

		score_surf = self.font.render(str(self.score), True, (0, 0, 0))
		score_rect = score_surf.get_rect(midtop=(kWindowWidth / 2, y))
		self.display_surface.blit(score_surf, score_rect)

	def display_final_score(self):
		y = kWindowHeight * kScoreMultiply * 2
		if self.active:
			self.score = (pygame.time.get_ticks() - self.start_offset) // 1000

		text_surf = self.font_for_big_text.render("Your score", True, (0, 0, 0))
		score_surf = self.font_for_big_text.render(str(self.score), True, (0, 0, 0))
		score_rect = score_surf.get_rect(midtop=(kWindowWidth / 2, y + kScoreShift))
		text_rect = text_surf.get_rect(midbottom=(kWindowWidth / 2, y))
		self.display_surface.blit(score_surf, score_rect)
		self.display_surface.blit(text_surf, text_rect)

	def run(self):
		last_time = time.time()
		while True:
			dt = time.time() - last_time
			last_time = time.time()

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				if event.type == pygame.MOUSEBUTTONDOWN:
					if self.active:
						self.bird.jump()
					else:
						self.bird = Bird(self.all_sprites, self.scale_factor * kBirdScale)
						self.active = True
						self.start_offset = pygame.time.get_ticks()

				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_SPACE:
						if self.active:
							self.bird.jump()
						else:
							self.bird = Bird(self.all_sprites, self.scale_factor * kBirdScale)
							self.active = True
							self.start_offset = pygame.time.get_ticks()

				if event.type == self.barrier_timer and self.active:
					Barrier([self.all_sprites, self.collision_sprites], self.scale_factor * 0.3)

			self.display_surface.fill((0, 0, 0))
			self.all_sprites.update(dt)
			self.all_sprites.draw(self.display_surface)

			if self.active:
				self.collisions()
				self.display_score()
			else:
				self.display_final_score()

			pygame.display.update()


game = Game()
game.run()