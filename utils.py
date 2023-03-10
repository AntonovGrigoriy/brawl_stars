import os
import sys
from typing import List

import pygame

def terminate():
    pygame.quit()
    sys.exit()


def load_image(name, colorkey=None):
    fullname = os.path.join('data', 'images', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        terminate()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def load_level(filename):
    filename = os.path.join('data', 'levels', filename)
    if not os.path.isfile(filename):
        print(f"Файл с уровнем '{filename}' не найден")
        terminate()
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]
    max_width = max(map(len, level_map))
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


def generate_level(level: List[str], vars):
    from tiles.tiles import Tile
    from tiles.player import Player

    new_player = None
    h = len(level)
    w = len(level[0])
    for y in range(h):
        for x in range(w):
            if level[y][x] == '.':
                Tile('empty', x, y, vars)
            elif level[y][x] == '#':
                Tile('wall', x, y, vars)
            elif level[y][x] == '+':
                Tile('moneta', x, y, vars)
            elif level[y][x] == '@':
                Tile('empty', x, y, vars)
                new_player = Player(x, y, vars)
    return new_player, w, h
