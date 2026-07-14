import pygame
pygame.init()
main_font = pygame.font.SysFont("Blazma", 20)

#colors
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)
pink = (255, 102, 102)
colors = [red, green, blue, white, black, pink]

#colors for hud
main_orange = (222, 179, 61)
main_black = (37, 48, 52)
main_blue = (59, 91, 138)
main_gray = (72, 72, 72)

cell_size = 20
#greed cords:
#x 15 to 46
#y 3 to 34
screen_size = (1280, 720)


#отступ направо - 15
#отступ вниз - 3
current_color = (255,255,255)
screen = pygame.display.set_mode(screen_size)
grid = [[(0,0,0) for _ in range(32)] for _ in range(32)]
active_button = 'colors'

clock = pygame.time.Clock()
running  = True

#160-230  240-310
def print_version():
    screen.blit(main_font.render("art master v.0.4", True, white), (10,692))


def draw(active_button):
    #полоска сверху
    pygame.draw.rect(screen, main_blue, (0, 0, 1280, 40))

    #кнопка "цвета"  X: p15-105    Y: 0-1
    pygame.draw.rect(screen, main_gray, (10, 0, cell_size*5, cell_size*2))
    if active_button == 'colors':
        pygame.draw.rect(screen, main_gray, (0, cell_size*2, cell_size*12, 720))
        pygame.draw.rect(screen, main_orange, (10, 0, cell_size*5, cell_size*2))
        count = 1
        for _ in colors:
            pygame.draw.rect(screen, _, (10, 75 + cell_size*count*4, cell_size*4, cell_size*4))
            pygame.draw.rect(screen, main_gray, (10, 75 + cell_size*4*count, cell_size*4, cell_size*4),4)
            if current_color == _:
                pygame.draw.rect(screen, main_orange, (10, 75 + cell_size * 4 * count, cell_size * 4, cell_size * 4), 6)
            count+=1
    pygame.draw.rect(screen, main_blue, (10, 0, cell_size*5, cell_size*2), 7)
    screen.blit(main_font.render('палитра', True, white), (20, 7))

while running:

    #events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #events updates
        mouse_x, mouse_y = pygame.mouse.get_pos()
        row = mouse_x // cell_size
        col = mouse_y // cell_size
        print(mouse_x, mouse_y, row, col)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # левая кнопка
                # перекраска пикселей в основном поле
                if 3 <= col <= 34 and 15 <= row <= 46:
                    grid[row-15][col-3] = current_color
                    #выбор цвета

                if 10 <= mouse_x <= 86 and 150 <= mouse_y <= 650:
                    k = 0
                    for _ in range(1, 7):
                        if 150+k <= mouse_y <= 230+k:
                            current_color = colors[_-1]
                        k+=80
                # взаимодействие с кнопкой "цвета"
                elif 15 <= mouse_x <= 105 and 0 <= row <= 1:
                    active_button = 'colors'
                pass
    #


    #screen and others

    #back
    screen.fill(main_black)
    #hud
    k = 15
    for row in grid:
        m = 3
        for el in row:

            pygame.draw.rect(screen, el, pygame.Rect(k*cell_size, m*cell_size, cell_size,cell_size))
            m+=1
        k+=1
    draw(active_button)
    #squares with color


    #selected color
    #61

    #version
    print_version()
    #clock etc.
    pygame.display.flip()
    clock.tick(cell_size)

