import pygame
pygame.init()
main_font = pygame.font.SysFont("Blazma", 20)
font_for_sizes = pygame.font.SysFont("Blazma", 50)

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
X_FOR_BUTTONS = 110


#отступ направо - 15
#отступ вниз - 3
current_color = (255,255,255)
current_size = 1
screen = pygame.display.set_mode(screen_size)
grid = [[(0,0,0) for _ in range(32)] for _ in range(32)]
active_button = 'colors'
size = 1

clock = pygame.time.Clock()
running  = True

#160-230  240-310
def print_version():
    screen.blit(main_font.render("art master v.0.6", True, white), (1100,692))

#ЗАРИСОВКА 3Х3 И 5Х5
def draw_more(size, color, row, col, grid):
    row -= 15
    col -= 3
    if size == 9:
        size = 3
        offset = 1

    elif size == 25:
        size = 5
        offset = 2

    for rows in range(row - offset, row + size - offset):
        for cols in range(col - offset, col + size - offset):
            if 0 <= rows < 32 and 0 <= cols < 32:
                grid[rows][cols] = color


    return grid


def fill_grid(color):
    return [[color for _ in range(32)] for _ in range(32)]


def draw_size_window():
    pygame.draw.rect(screen, main_orange, (X_FOR_BUTTONS * 1 + 10, 0, cell_size * 5, cell_size * 2))
    pygame.draw.rect(screen, main_gray, (0, cell_size * 2, cell_size * 9, 450))
    # менюшка с размерами
    pygame.draw.rect(screen, main_gray, (10, cell_size * 4, cell_size * 4, cell_size * 4))
    if current_size == 1:
        pygame.draw.rect(screen, main_orange, (10, cell_size * 4, cell_size * 4, cell_size * 4))
    pygame.draw.rect(screen, white, (10, cell_size * 4, cell_size * 4, cell_size * 4), 4)

    pygame.draw.rect(screen, main_gray, (10, cell_size * 10, cell_size * 4, cell_size * 4))
    if current_size == 9:
        pygame.draw.rect(screen, main_orange, (10, cell_size * 10, cell_size * 4, cell_size * 4))
    pygame.draw.rect(screen, white, (10, cell_size * 10, cell_size * 4, cell_size * 4), 4)

    pygame.draw.rect(screen, main_gray, (10, cell_size * 16, cell_size * 4, cell_size * 4))
    if current_size == 25:
        pygame.draw.rect(screen, main_orange, (10, cell_size * 16, cell_size * 4, cell_size * 4))
    pygame.draw.rect(screen, white, (10, cell_size * 16, cell_size * 4, cell_size * 4), 4)

    # 1 9 and 25
    screen.blit(font_for_sizes.render('1', True, white), (36, cell_size * 5 - 11))
    screen.blit(font_for_sizes.render('9', True, white), (36, cell_size * 11 - 11))
    screen.blit(font_for_sizes.render('25', True, white), (22, cell_size * 17 - 11))


def draw_change_color_window():
    pygame.draw.rect(screen, main_gray, (0, cell_size * 2, cell_size * 9, 720))
    pygame.draw.rect(screen, main_orange, (10, 0, cell_size * 5, cell_size * 2))
    #fill   X:10-130   Y:660-700
    pygame.draw.rect(screen, white, (10, cell_size * 33, cell_size * 6, cell_size * 2),3)
    screen.blit(main_font.render('заливка', True, white), (30, cell_size * 33+7))
    #colors
    count = 1
    for _ in colors:
        pygame.draw.rect(screen, _, (10, 75 + cell_size * count * 4, cell_size * 4, cell_size * 4))
        pygame.draw.rect(screen, main_gray, (10, 75 + cell_size * 4 * count, cell_size * 4, cell_size * 4), 4)
        if current_color == _:
            pygame.draw.rect(screen, main_orange, (10, 75 + cell_size * 4 * count, cell_size * 4, cell_size * 4), 6)
        count += 1


def draw(active_button):
    #полоска сверху
    pygame.draw.rect(screen, main_blue, (0, 0, 1280, 40))

    #кнопка "цвета"  X: p15-105    Y: 0-1
    pygame.draw.rect(screen, main_gray, (X_FOR_BUTTONS*0 + 10, 0, cell_size*5, cell_size*2))
    if active_button == 'colors':
        draw_change_color_window()
    pygame.draw.rect(screen, main_blue, (X_FOR_BUTTONS*0 + 10, 0, cell_size*5, cell_size*2), 7)
    screen.blit(main_font.render('палитра', True, white), (20, 7))

    #кнопка "Размер кисти"   X: p125-210   Y: 0-1
    pygame.draw.rect(screen, main_gray, (X_FOR_BUTTONS*1 + 10, 0, cell_size*5, cell_size*2))
    if active_button == 'size':
        draw_size_window()

    pygame.draw.rect(screen, main_blue, (X_FOR_BUTTONS*1 + 10, 0, cell_size*5, cell_size*2), 7)
    screen.blit(main_font.render("размер", True, white), (X_FOR_BUTTONS*1+24,7))

while running:

    #events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #events updates
        mouse_x, mouse_y = pygame.mouse.get_pos()
        row = mouse_x // cell_size
        col = mouse_y // cell_size
        print(mouse_x, mouse_y, row, col, active_button)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # левая кнопка

                # взаимодействие с кнопкой "цвета"
                if 15 <= mouse_x <= 105 and 0 <= mouse_y <= cell_size*2:
                    active_button = 'colors'
                elif 125 <= mouse_x <= 210 and 0 <= mouse_y <= cell_size*2:
                    active_button = 'size'

                # перекраска пикселей в основном поле
                if 3 <= col <= 34 and 15 <= row <= 46:
                    grid[row-15][col-3] = current_color
                    if current_size != 1:
                        grid = draw_more(current_size, current_color, row, col, grid)

                    #выбор цвета
                elif active_button == 'colors':
                    if 10 <= mouse_x <= 86 and 150 <= mouse_y <= 650:
                        k = 0
                        for _ in range(1, 7):
                            if 150+k <= mouse_y <= 230+k:
                                current_color = colors[_-1]
                            k+=80

                    elif 10 <= mouse_x <= 130 and 660 <= mouse_y <= 700:
                        grid = fill_grid(current_color)

                # взаимодействие с кнопкой "цвета"
                elif 15 <= mouse_x <= 105 and 0 <= mouse_y <= cell_size*2:
                    active_button = 'colors'
                elif 125 <= mouse_x <= 210 and 0 <= mouse_y <= cell_size*2:
                    active_button = 'size'

                #sizes
                elif active_button == 'size' and 10 <= mouse_x <= 90:
                    if 80 <= mouse_y <= 160:
                        current_size = 1
                    elif 200 <= mouse_y <= 280:
                        current_size = 9
                    elif 320 <= mouse_y <= 400:
                        current_size = 25
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

