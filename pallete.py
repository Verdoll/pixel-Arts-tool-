import pygame

#colors sets
#1
red = (255, 50, 50)
green = (50, 255, 50)
blue = (50, 50, 255)
white = (255, 255, 255)
black = (0, 0, 0)
pink = (255, 80, 180)
standart_colors = [red, green, blue, white, black, pink]
#3
red = (225, 150, 150)
green = (150, 225, 150)
blue = (150, 150, 225)
white = (255, 255, 255)
black = (80, 80, 80)
pink = (255, 180, 220)
colors_3 = [red, green, blue, white, black, pink]
#2
red = (180, 30, 30)
green = (30, 180, 30)
blue = (30, 30, 180)
white = (255, 255, 255)
black = (140, 140, 140)
pink = (200, 60, 120)
colors_2 = [red, green, blue, white, black, pink]

class Pallete():
    def __init__(self):
        self.current_pallete = 0
        self.set_1 = standart_colors
        self.set_2 = colors_2
        self.set_3 = colors_3
        self.sets = [self.set_1, self.set_2, self.set_3]
        self.current_set = self.sets[self.current_pallete]


    def change_pallete(self, num):
        self.current_pallete = num
        self.current_set = self.sets[self.current_pallete]


def draw_pallete(cell_size, main_font, main_gray, white, orange, screen, pallete):
    pygame.draw.rect(screen, white, (18, 50, cell_size * 2.2, cell_size * 2.2), 2)
    pygame.draw.rect(screen, white, (18+10 + cell_size*2, 50, cell_size * 2.2, cell_size * 2.2), 2)
    pygame.draw.rect(screen, white, (18+20 + cell_size*4, 50, cell_size * 2.2, cell_size * 2.2), 2)

    if pallete.current_pallete == 0:
        pygame.draw.rect(screen, orange, (18, 50, cell_size * 2.2, cell_size * 2.2))
    screen.blit(main_font.render('1', True, white), (34, 60))
    if pallete.current_pallete == 1:
        pygame.draw.rect(screen, orange, (18 + 10 + cell_size * 2, 50, cell_size * 2.2, cell_size * 2.2))
    screen.blit(main_font.render('2', True, white), (33+10+cell_size*2, 60))
    if pallete.current_pallete == 2:
        pygame.draw.rect(screen, orange, (18 + 20 + cell_size * 4, 50, cell_size * 2.2, cell_size * 2.2))
    screen.blit(main_font.render('3', True, white), (34+cell_size*5, 60))


def choice_pallete(x, y, pallete):
    if 20 <= x <= 60 and 50 <= y <= 90:
        pallete.change_pallete(0)
    elif 70 <= x <= 110 and 50 <= y <= 90:
        pallete.change_pallete(1)
    elif 120 <= x <= 160 and 50 <= y <= 90:
        pallete.change_pallete(2)