import pygame
import sliders
import colors as cl
pygame.init()
main_orange = (222, 179, 61)

#R
r_slider = sliders.Slider((140, 160, 5, 120, 20, 10, 0, 255))
r_slider.change_texts('R', r_slider.value)
r_slider.change_set_values(0, 255)
r_slider.change_colors(cl.white, cl.red)
#G
g_slider = sliders.Slider((140, 190, 5, 120, 20, 10, 0, 255))
g_slider.change_texts('G', r_slider.value)
g_slider.change_set_values(0, 255)
g_slider.change_colors(cl.white, cl.green)
#B
b_slider = sliders.Slider((140, 220, 5, 120, 20, 10, 0, 255))
b_slider.change_texts('B', r_slider.value)
b_slider.change_set_values(0, 255)
b_slider.change_colors(cl.white, cl.blue)


def draw_button(screen, font, boolean, self_color):
    if boolean:
        pygame.draw.rect(screen, main_orange, (18, 100, 145, 40))
        pygame.draw.rect(screen, cl.main_gray, (110, 140, 180, 240))
        pygame.draw.rect(screen, cl.white, (110, 140, 180, 240), 2)
        r_slider.change_texts('R', int(r_slider.value))
        r_slider.draw(screen, font, (119,150), (250,150))
        g_slider.change_texts('G', int(g_slider.value))
        g_slider.draw(screen, font, (119,180), (250,180))
        b_slider.change_texts('B', int(b_slider.value))
        b_slider.draw(screen, font, (119,210), (250,210))

        pygame.draw.rect(screen, (r_slider.value, g_slider.value, b_slider.value), (120, 240, 160, 80))

        if self_color:
            pygame.draw.rect(screen, cl.main_orange, (120, 330, 160, 40))
        pygame.draw.rect(screen, cl.white, (120, 330, 160, 40),2)
        screen.blit(font.render('выбрать цвет', True, cl.white), (130, 337))
    pygame.draw.rect(screen, cl.white, (18,100, 145,40), 2)
    screen.blit(font.render('СВОЙ ЦВЕТ', True, cl.white), (39, 108))


def change_sliders_value(x, y):
    sliders.control_movement(r_slider, x, y)
    sliders.control_movement(g_slider, x, y)
    sliders.control_movement(b_slider, x, y)


def touch_button(x, y, boolean):
    if 18 <= x <= 163 and 100 <= y <= 140:
        return True
    return False

def decide_color(x, y):
    if 120 <= x <= 280 and 330 <= y <= 370:
        return True
    return False