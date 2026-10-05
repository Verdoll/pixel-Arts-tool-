import pygame
import Brush
import Animation
import rgb_window
import settings_new_frame as settings
import pallete as pl
import rgb_window as rgb
import conditions
import eyedropper
import filters

#for testing (пишет в консоль всю инфу)
DEBUG_MODE = False
FPS = 240

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
grid = [[(0,0,0) for _ in range(32)] for _ in range(32)]

#отступ направо - 15
#отступ вниз - 3

#КЛАССЫ
brush = Brush.Brush(1, white, 'brush')
canvas = Animation.Animation(grid, 'drawing')
setting = settings.Settings()
pallete = pl.Pallete()
program = conditions.Program()


screen = pygame.display.set_mode(screen_size)

active_button = 'colors'
size = 1

clock = pygame.time.Clock()
running  = True

#160-230  240-310
def print_version():
    screen.blit(main_font.render("art master v.1.2", True, white), (1100,692))


def print_quick_keys():
    screen.blit(main_font.render("БЫСТРЫЕ КЛАВИШИ", True, white), (1050,50))
    screen.blit(main_font.render("1, 2, 3  -  изменение", True, white), (1030, 80))
    screen.blit(main_font.render("размера кисти", True, white), (1067, 97))


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


def draw_size_window():
    pygame.draw.rect(screen, main_orange, (X_FOR_BUTTONS * 1 + 10, 0, cell_size * 5, cell_size * 2))
    pygame.draw.rect(screen, main_gray, (0, cell_size * 2, cell_size * 9, 450))
    # менюшка с размерами
    pygame.draw.rect(screen, main_gray, (10, cell_size * 4, cell_size * 4, cell_size * 4))
    if brush.size == 1:
        pygame.draw.rect(screen, main_orange, (10, cell_size * 4, cell_size * 4, cell_size * 4))
    pygame.draw.rect(screen, white, (10, cell_size * 4, cell_size * 4, cell_size * 4), 4)

    pygame.draw.rect(screen, main_gray, (10, cell_size * 10, cell_size * 4, cell_size * 4))
    if brush.size == 9:
        pygame.draw.rect(screen, main_orange, (10, cell_size * 10, cell_size * 4, cell_size * 4))
    pygame.draw.rect(screen, white, (10, cell_size * 10, cell_size * 4, cell_size * 4), 4)

    pygame.draw.rect(screen, main_gray, (10, cell_size * 16, cell_size * 4, cell_size * 4))
    if brush.size == 25:
        pygame.draw.rect(screen, main_orange, (10, cell_size * 16, cell_size * 4, cell_size * 4))
    pygame.draw.rect(screen, white, (10, cell_size * 16, cell_size * 4, cell_size * 4), 4)

    # 1 9 and 25
    screen.blit(font_for_sizes.render('1', True, white), (36, cell_size * 5 - 11))
    screen.blit(font_for_sizes.render('9', True, white), (36, cell_size * 11 - 11))
    screen.blit(font_for_sizes.render('25', True, white), (22, cell_size * 17 - 11))


def fill(x,y, last_color, new_color):
    if last_color == new_color:
        return grid
    stack = [(x,y)]
    while stack:
        cx, cy = stack.pop()

        if 0 > cx or cx >= 32 or 0 > cy or cy >= 32:
            continue

        if grid[cx][cy] != last_color:
            continue

        grid[cx][cy] = new_color

        stack.append((cx + 1, cy))
        stack.append((cx, cy + 1))
        stack.append((cx - 1, cy))
        stack.append((cx, cy - 1))

    return grid


def draw_change_color_window():
    pygame.draw.rect(screen, main_gray, (0, cell_size * 2, cell_size * 9, 720))
    pygame.draw.rect(screen, main_orange, (10, 0, cell_size * 5, cell_size * 2))
    #fill   X:10-130   Y:660-700
    if brush.mode == 'filler':
        pygame.draw.rect(screen, main_orange, (10, cell_size * 34, cell_size * 6, cell_size * 2))
    pygame.draw.rect(screen, white, (10, cell_size * 34, cell_size * 6, cell_size * 2),2)
    screen.blit(main_font.render('заливка', True, white), (30, cell_size * 33+27))

    eyedropper.draw(screen, main_font, brush.mode)

    #colors
    count = 1
    for _ in pallete.current_set:
        pygame.draw.rect(screen, _, (10, 75 + cell_size * count * 4, cell_size * 4, cell_size * 4))
        pygame.draw.rect(screen, main_gray, (10, 75 + cell_size * 4 * count, cell_size * 4, cell_size * 4), 4)
        if brush.color == _:
            pygame.draw.rect(screen, main_orange, (10, 75 + cell_size * 4 * count, cell_size * 4, cell_size * 4), 6)
        count += 1


def draw(active_button):
    #полоска сверху
    pygame.draw.rect(screen, main_blue, (0, 0, 1280, 40))

    #кнопка "цвета"  X: p15-105    Y: 0-1
    pygame.draw.rect(screen, main_gray, (X_FOR_BUTTONS*0 + 10, 0, cell_size*5, cell_size*2))
    if active_button == 'colors':
        draw_change_color_window()
        rgb.draw_button(screen,main_font, program.rgb_window, program.self_color)
        if program.self_color and brush.mode == 'eyedropper':
            brush.change_mode('brush')
        pl.draw_pallete(cell_size, main_font, main_gray, white, main_orange, screen, pallete)
    pygame.draw.rect(screen, main_blue, (X_FOR_BUTTONS*0 + 10, 0, cell_size*5, cell_size*2), 7)
    screen.blit(main_font.render('палитра', True, white), (20, 7))

    #кнопка "Размер кисти"   X: p125-210   Y: 0-1
    pygame.draw.rect(screen, main_gray, (X_FOR_BUTTONS*1 + 10, 0, cell_size*5, cell_size*2))
    if active_button == 'size':
        draw_size_window()

    pygame.draw.rect(screen, main_blue, (X_FOR_BUTTONS*1 + 10, 0, cell_size*5, cell_size*2), 7)
    screen.blit(main_font.render("размер", True, white), (X_FOR_BUTTONS*1+24,7))

    #кнопка фильтров
    filters.draw_button(screen, main_font, cell_size, X_FOR_BUTTONS, active_button)

    #анимация
    pygame.draw.rect(screen, main_gray, (1035, 200, cell_size*10, cell_size*3))
    pygame.draw.rect(screen, white, (1035, 200, cell_size * 10, cell_size * 3), 1)

    pygame.draw.rect(screen, white, (1095, 200, cell_size * 4, cell_size * 3), 1)
    screen.blit(font_for_sizes.render('<', True, white), (1050, 201))
    if canvas.current_frame_index <= 8:
        screen.blit(font_for_sizes.render(str(canvas.current_frame_index + 1), True, white), (1122, 201))
    if canvas.current_frame_index >= 9:
        screen.blit(font_for_sizes.render(str(canvas.current_frame_index + 1), True, white), (1109, 201))
    screen.blit(font_for_sizes.render('>', True, white), (1190, 201))



    pygame.draw.rect(screen, main_gray, (1035, 270, cell_size * 7, cell_size * 2))
    pygame.draw.rect(screen, white, (1035, 270, cell_size * 7, cell_size * 2), 1)
    screen.blit(main_font.render('новый кадр', True, white), (1047, 276))

    pygame.draw.rect(screen, main_gray, (1035, 320, cell_size * 5, cell_size * 2))
    if canvas.mode == 'animation':
        pygame.draw.rect(screen, main_orange, (1035, 320, cell_size * 5, cell_size * 2))
    Animation.draw(screen, main_font, 20, program.FPS_window)
    #настройки нового кадра
    settings.draw_setting_unlock(cell_size, main_font, main_gray, white, main_orange, screen, setting)





frame_counter = 0
while running:

    if canvas.mode == 'animation':
        frame_counter += 1
        if frame_counter >= 120 / canvas.FPS:
            frame_counter = 0
            grid = canvas.next_frame()

    if program.self_color:
        brush.color = (rgb.r_slider.value, rgb.g_slider.value, rgb.b_slider.value)


    #зажатая клавиша
    left, middle, right = pygame.mouse.get_pressed()
    if left:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        row = mouse_x // cell_size
        col = mouse_y // cell_size
        if program.FPS_window:
            Animation.change_FPS_value(mouse_x, mouse_y, canvas)
        if program.rgb_window:
            rgb.change_sliders_value(mouse_x, mouse_y)
        if 3 <= col <= 34 and 15 <= row <= 46 and brush.mode == 'brush':
            grid[row - 15][col - 3] = brush.color
            if brush.size != 1:
                grid = draw_more(brush.size, brush.color, row, col, grid)

    #events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #events updates
        mouse_x, mouse_y = pygame.mouse.get_pos()
        row = mouse_x // cell_size
        col = mouse_y // cell_size
        if DEBUG_MODE:
            print(mouse_x, mouse_y, row, col, active_button, program.self_color, brush.mode)


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                brush.size = 1
            elif event.key == pygame.K_2:
                brush.size = 9
            elif event.key == pygame.K_3:
                brush.size = 25
            elif event.key == pygame.K_e:
                brush.swap_mode('eyedropper', 'brush')
                if program.self_color:
                    program.self_color = False
            elif event.key == pygame.K_m:
                print(grid)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # левая кнопка

                # взаимодействие с кнопкой "цвета"
                if 15 <= mouse_x <= 105 and 0 <= mouse_y <= cell_size*2:
                    active_button = 'colors'
                elif 125 <= mouse_x <= 210 and 0 <= mouse_y <= cell_size*2:
                    active_button = 'size'
                elif filters.active_filters(mouse_x, mouse_y):
                    active_button = 'filters'

                #animation
                elif 1035 <= mouse_x <= 1174 and 270 <= mouse_y <= 310:
                    canvas.new_frame(setting)
                elif 1030 <= mouse_x <= 1100 and 200 <= mouse_y <= 260:
                    if canvas.current_frame_index != 0:
                        grid = canvas.change_frame(-1)
                elif 1175 <= mouse_x <= 1236 and 200 <= mouse_y <= 260:
                    if canvas.current_frame_index + 1 < len(canvas.list_of_canvas):
                        grid = canvas.change_frame(1)
                elif 1035 <= mouse_x <= 1135 and 320 <= mouse_y <= 360:
                    canvas.swap_mode()
                elif settings.swap_set_mode(mouse_x, mouse_y):
                    setting.swap_mode()
                elif settings.is_delete(mouse_x, mouse_y) and setting.is_window_open:
                    canvas.delete_frame()
                    grid = canvas.list_of_canvas[canvas.current_frame_index]

                settings.is_coppyng(mouse_x, mouse_y, setting)

                if Animation.touch_button(mouse_x, mouse_y):
                    program.swap_fps_window()

                #pallete
                pl.choice_pallete(mouse_x, mouse_y, pallete)

                #окно цветов
                if rgb_window.touch_button(mouse_x, mouse_y, program.rgb_window):
                    program.touch_rgb()
                if program.rgb_window:
                    if rgb.decide_color(mouse_x, mouse_y):
                        program.swap_self_color()
                        if brush.mode == 'eyedropper':
                            brush.change_mode('brush')

                        # перекраска пикселей в основном поле
                if 3 <= col <= 34 and 15 <= row <= 46:
                    if brush.mode == 'brush':
                        grid[row-15][col-3] = brush.color
                        if brush.size != 1:
                            grid = draw_more(brush.size, brush.color, row, col, grid)

                    elif brush.mode == 'filler':
                        x = row - 15
                        y = col - 3
                        grid = fill(x, y, grid[x][y], brush.color)

                    elif brush.mode == 'eyedropper':
                        brush.change_color(grid[row-15][col-3])

                    #выбор цвета
                elif active_button == 'colors':
                    if 10 <= mouse_x <= 86 and 150 <= mouse_y <= 650:
                        k = 0
                        for _ in range(1, 7):
                            if 150+k <= mouse_y <= 230+k:
                                brush.color = pallete.current_set[_-1]
                                program.disable_self_color()
                            k+=80

                    elif 10 <= mouse_x <= 130 and 680 <= mouse_y <= 720:
                        if brush.mode == 'brush':
                            brush.change_mode('filler')
                        else:
                            brush.change_mode('brush')

                    eyedropper.swap_modes(mouse_x, mouse_y, brush)
                    if program.self_color and brush.mode == 'eyedropper':
                        program.swap_self_color()





                # взаимодействие с кнопкой "цвета"
                elif 15 <= mouse_x <= 105 and 0 <= mouse_y <= cell_size*2:
                    active_button = 'colors'
                elif 125 <= mouse_x <= 210 and 0 <= mouse_y <= cell_size*2:
                    active_button = 'size'

                #sizes
                elif active_button == 'size' and 10 <= mouse_x <= 90:
                    if 80 <= mouse_y <= 160:
                        brush.size = 1
                    elif 200 <= mouse_y <= 280:
                        brush.size = 9
                    elif 320 <= mouse_y <= 400:
                        brush.size = 25
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
            mouse_x, mouse_y = pygame.mouse.get_pos()
            x = mouse_x // cell_size
            y = mouse_y // cell_size
            pygame.draw.rect(screen, el, pygame.Rect(k*cell_size, m*cell_size, cell_size,cell_size))
            if 3 <= y <= 34 and 15 <= x <= 46 and brush.mode=='eyedropper':
                help_color = white
                if grid[x-15][y-3][0] > 210 and grid[x-15][y-3][1] > 210 and grid[x-15][y-3][2] > 210:
                    help_color = main_black
                pygame.draw.rect(screen, help_color, pygame.Rect(x * cell_size, y * cell_size, cell_size, cell_size), 2)

            m+=1
        k+=1
    draw(active_button)
    if active_button == 'filters':
        filters.draw_ui(screen, cell_size, main_font)

    #version
    print_version()

    #quick keys
    print_quick_keys()

    #clock etc.
    pygame.display.flip()
    clock.tick(FPS)

