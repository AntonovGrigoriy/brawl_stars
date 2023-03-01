import pygame
from utils import terminate, load_image


def start_screen(screen: pygame.Surface) -> None:
    intro_text = ["ЛАБИРИНТ БРАВЛ СТАРС", "",
                  "Правила игры:",
                  "Нужно выбраться из лабиринта за отведённое время,",
                  "Выход находится там, где куб усиления"]
    fon = pygame.transform.scale(load_image('fon.jpg'), screen.get_size())
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    clock = pygame.time.Clock()
    FPS = 10
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return  # начинаем игру
        clock.tick(FPS)