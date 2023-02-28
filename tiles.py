import pygame
from tileimages import tile_images, tile_walls


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y, vars):
        super().__init__(vars['tiles_group'], vars['all_sprites'])
        if tile_type in tile_walls:
            vars['walls_group'].add(self)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(
            vars['TILE_WIDTH'] * pos_x, vars['TILE_HEIGHT'] * pos_y)
