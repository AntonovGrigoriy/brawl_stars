import pygame

from utils import terminate, generate_level, load_level
from startscreen import start_screen
import sys

TIMER_SPEED = 1000
SIZE = WIDTH, HEIGHT = 1200, 600
BACKGROUND = 'black'
FPS = 60
TILE_WIDTH = TILE_HEIGHT = 50
pygame.init()
color = (255, 255, 255)
color_light = (170, 170, 170)
color_dark = (100, 100, 100)
smallfont = pygame.font.SysFont('Corbel', 40)
textb = smallfont.render('выход', True, color)
text_new1 = smallfont.render('продол-', True, color)
text_new2 = smallfont.render('жить игру', True, color)
timer_timer = smallfont.render('таймер:', True, color)
timer_counter, timer_text = 30, '30'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, TIMER_SPEED) # как быстро идёт время
timer_font = pygame.font.SysFont('Consolas', 50)
timer_color = (0, 0, 0)
end = pygame.image.load('end.jpg')
end2 = pygame.image.load('end2.jpg')
endX = end2X = 0
endY = end2Y = 100
speed = speed2 = 50
prx = 50
pry = 500
prx2 = 0
pry2 = 0

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption('Лабиринт Бравл Старс')
    start_screen(screen)
    player = None
    all_sprites = pygame.sprite.Group()
    tiles_group = pygame.sprite.Group()
    player_group = pygame.sprite.Group()
    walls_group = pygame.sprite.Group()
    filename = input('Введите название файла с уровнем(1,2,3,4):')
    diffic = input('Введите уровень сложности(1,2,3):')
    if diffic != '1' and diffic != '2' and diffic != '3':
        print('Неверный уровень сложности')
        diffic = '2'
    if diffic == '2':
        TIME = 2
    elif diffic == '1':
        TIME = 1
    else:
        TIME = 3
    player, level_x, level_y = generate_level(load_level(filename), globals())

    clock = pygame.time.Clock()
    running = True
    screen.fill(BACKGROUND)
    while running:
        pygame.time.delay(30)
        for event in pygame.event.get():
            mouse = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.move_ip(-TILE_WIDTH, 0, walls_group)
                    prx -= 50
                elif event.key == pygame.K_RIGHT:
                    player.move_ip(TILE_WIDTH, 0, walls_group)
                    prx += 50
                elif event.key == pygame.K_UP:
                    player.move_ip(0, -TILE_HEIGHT, walls_group)
                    pry -= 50
                elif event.key == pygame.K_DOWN:
                    player.move_ip(0, TILE_HEIGHT, walls_group)
                    pry += 50
            elif prx == 250 and pry == 0:
                prx2 = 1
                pry2 = 1
                pass
            elif event.type == pygame.USEREVENT and (prx != 250 or pry != 0) \
                    and (prx != 50 or pry != 500) and prx2 != 1 and pry2 != 1:
                timer_counter -= TIME
                if timer_counter > 0:
                    timer_text = str(timer_counter).rjust(3)
                else:
                    timer_text = ''
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 1000 <= mouse[0] <= 1200 and 0 <= mouse[1] <= 50:
                    terminate()
                if 795 <= mouse[0] <= 995 and 0 <= mouse[1] <= 100:
                    prx2 = 0
                    pry2 = 0
                    timer_counter, timer_text = 30, '30'.rjust(3)
                    endX = 0
                    endY = 100
                    pygame.draw.rect(screen, timer_color, [600, 100, 600, 600])
            if 1000 <= mouse[0] <= 1200 and 0 <= mouse[1] <= 50:
                pygame.draw.rect(screen, color_light, [1000, 0, 250, 50])
            else:
                pygame.draw.rect(screen, color_dark, [1000, 0, 250, 50])
            if 795 <= mouse[0] <= 995 and 0 <= mouse[1] <= 100:
                pygame.draw.rect(screen, color_light, [795, 0, 200, 100])
            else:
                pygame.draw.rect(screen, color_dark, [795, 0, 200, 100])
            screen.blit(textb, (1050, 3))
            screen.blit(text_new1, (825, 3))
            screen.blit(text_new2, (815, 53))
            screen.blit(timer_timer, (1040, 53))
        screen.blit(end, (endX, endY))
        screen.blit(end2, (end2X, end2Y))
        pygame.draw.rect(screen, timer_color, [1000, 100, 250, 50])
        screen.blit(timer_font.render(timer_text, True, (255, 255, 255)), (1050, 110))
        tiles_group.draw(screen)
        player_group.draw(screen)
        if timer_counter > 0 and end2X <= 550:
            pygame.display.flip()
        else:
            if endX <= 600:
                endX += speed
                pygame.display.flip()
        if prx == 250 and pry == 0 and end2X <= 550:
            end2X += speed2
            pygame.display.flip()
        clock.tick(FPS)
    terminate()