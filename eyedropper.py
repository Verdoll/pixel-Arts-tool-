import pygame
import colors as cl
pygame.init()


def draw(screen, font, mode, cell_size=20):
    if mode == 'eyedropper':
        pygame.draw.rect(screen, cl.main_orange, (10, cell_size * 32-5, cell_size * 6, cell_size * 2))
    pygame.draw.rect(screen, cl.white, (10, cell_size * 32-5, cell_size * 6, cell_size * 2),2)
    screen.blit(font.render('пипетка', True, cl.white), (30, cell_size * 33-18))


def swap_modes(x,y, brush):
    if 10 <= x <= 130 and 638 <= y <= 673:
        if brush.mode == 'eyedropper' or brush.mode == 'brush':
            brush.swap_mode('eyedropper', 'brush')
        elif brush.mode == 'filler':
            brush.swap_mode('filler', 'eyedropper')
