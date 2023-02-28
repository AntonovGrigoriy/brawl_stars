import pygame
from tileimages import player_image


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, vars):
        super().__init__(vars['player_group'], vars['all_sprites'])
        self.image = player_image
        self.rect = self.image.get_rect().move(
            vars['TILE_WIDTH'] * pos_x + (vars['TILE_WIDTH'] - self.image.get_width()) // 2,
            vars['TILE_HEIGHT'] * pos_y + (vars['TILE_HEIGHT'] - self.image.get_height()) // 2
        )

    def move_ip(self, dx, dy, walls_group = None):
        old_rect = self.rect.copy()
        self.rect.move_ip(dx, dy)
        if walls_group is not None and pygame.sprite.spritecollideany(self, walls_group):
            self.rect = old_rect
