#рисовалка
import pygame
import random

#colors
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)
pink = (255, 102, 102)
colors = [red, green, blue, white, black, pink]


current_color = (255,255,255)
screen = pygame.display.set_mode((800,600))
grid = [[(0,0,0) for _ in range(8)] for _ in range(8)]
#если по 75 возьмем 1 квадрат, то:
#600 пикселей слева занято, 200 справа под худ
#короче 60 взяли и хватит
running  = True
while running:

    #events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #events updates
        mouse_x, mouse_y = pygame.mouse.get_pos()
        row = mouse_x // 60
        col = mouse_y // 60

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # левая кнопка
                if 0 <= col <= 7 and 0 <= row <= 7:
                    grid[row][col] = current_color
                elif 12 <= row <= 13 and 0 <= col  <= 5:
                    current_color = colors[col]
                pass
    # рисовать


    #screen and others

    #back
    screen.fill((0,35,100))
    #hud
    k = 0
    for row in grid:
        m = 0
        for el in row:

            pygame.draw.rect(screen, el, pygame.Rect(k*60, m*60, 60,60))
            m+=1
        k+=1
    #squares with color
    for k in range(6):
        pygame.draw.rect(screen, colors[k], pygame.Rect(800-60, k*60,60,60))
        pygame.draw.rect(screen, white, pygame.Rect(800-60, k*60, 60,60), 2)

    #clock etc.
    pygame.display.flip()
    clock = pygame.time.Clock()
    clock.tick(60)