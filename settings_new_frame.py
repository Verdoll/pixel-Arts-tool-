import pygame

class Settings():
    def __init__(self):
        self.is_window_open = False
        self.coppyng = False


    def swap_mode(self):
        self.is_window_open = not self.is_window_open


    def swap_set_copy_frame(self):
        self.coppyng = not self.coppyng



def swap_set_mode(x, y):
    if 1195 <= x <= 1235 and 272 <= y <= 312:
        return True
    else:
        return False


def is_delete(x,y):
    if 1025 <= x <= 1225 and 385 <= y <= 430:
        return True
    else:
        return False


def is_coppyng(x, y, setting):
    if 1185 <= x <= 1225 and 325 <= y <= 367 and setting.is_window_open:
        setting.swap_set_copy_frame()


def draw_setting_unlock(cell_size, main_font, main_gray, white, orange, screen, setting):
    pygame.draw.rect(screen, main_gray, (1195, 270, cell_size * 2, cell_size * 2))
    pygame.draw.rect(screen, white, (1195, 270, cell_size * 2, cell_size * 2), 1)
    if setting.is_window_open:
        pygame.draw.rect(screen, orange, (1195, 270, cell_size * 2, cell_size * 2))
        pygame.draw.rect(screen, white, (1195, 270, cell_size * 2, cell_size * 2), 1)
        screen.blit(main_font.render('v', True, white),(1209, 278))
    else:
        screen.blit(main_font.render('^', True, white),(1209, 281))

    if setting.is_window_open:
        pygame.draw.rect(screen, main_gray, (1015, 315, cell_size * 11, cell_size * 8))
        pygame.draw.rect(screen, main_gray, (1015, 315, cell_size * 11, cell_size * 8), 1)
        screen.blit(main_font.render('дублировать', True, white),(1025, 320))
        screen.blit(main_font.render('пред. кадр', True, white), (1025, 320 + cell_size ))
        pygame.draw.rect(screen, main_gray, (1185, 325, cell_size * 2, cell_size * 2))
        if setting.coppyng:
            pygame.draw.rect(screen, orange, (1185, 325, cell_size * 2, cell_size * 2))
            screen.blit(main_font.render('x', True, white),(1199, 332))
        pygame.draw.rect(screen, white, (1185, 325, cell_size * 2, cell_size * 2), 1)
        #1025 1225      385 430
        pygame.draw.rect(screen, white, (1025, 385, cell_size * 10, cell_size * 2), 1)
        screen.blit(main_font.render('удалить кадр', True, white), (1055, 392))


def main():
    pass
if __name__ == '__main__':
    main()