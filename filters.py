import pygame
import colors

def draw_button(screen, font, cell_size, X_FOR_BUTTONS, active_button):
    pygame.draw.rect(screen, colors.main_gray, (X_FOR_BUTTONS*2 + 10, 0, cell_size*5.7, cell_size*2))
    if active_button == 'filters':
        pygame.draw.rect(screen, colors.main_orange, (X_FOR_BUTTONS * 2 + 10, 0, cell_size * 5.7, cell_size * 2))
    pygame.draw.rect(screen, colors.main_blue, (X_FOR_BUTTONS * 2 + 10, 0, cell_size * 5.7, cell_size * 2), 7)
    screen.blit(font.render('фильтры', True, colors.white), (X_FOR_BUTTONS * 2 + 24, 7))


#240 340         6 36
def active_filters(x, y):
    if 240 <= x <= 340 and 6 <= y <= 36:
        return True
    return False


def draw_ui(screen, cell_size, font):
    pygame.draw.rect(screen, colors.main_gray, (0, cell_size*2, cell_size*12, cell_size*25))
