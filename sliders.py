##ползунки
import pygame


class Slider():
    def __init__(self, position=(0,0), width_slider=5, height_slider=100, width_button=20, height_button=10, min_value=0, max_value=100,
                 color_main=(255,255,255), color_button=(255,255,255)):
        self.position = position
        self.width_slider = width_slider
        self.height_slider = height_slider
        self.width_button = width_button
        self.height_button = height_button
        self.min_value = min_value
        self.max_value = max_value
        self.color_main = color_main
        self.color_button = color_button
        self.left_text = ''
        self.right_text = ''
        self.value = min_value

        #value per pixel
        self.VpP = (max_value - min_value) / self.height_slider #сколько пикселей приходится на 1 значение +-
        self.center_slider = position[1] + width_slider / 2
        self.x_button = position[0] - height_button / 2
        self.y_button = self.center_slider - width_button / 2

    def count_VpP(self):
        self.VpP = (self.max_value - self.min_value) / self.height_slider


    def draw(self, screen, font, left_font_pos, right_font_pos):
        pygame.draw.rect(screen, self.color_main, (self.position[0], self.position[1], self.height_slider, self.width_slider))
        pygame.draw.rect(screen, self.color_button, (self.x_button, self.y_button, self.height_button, self.width_button))
        screen.blit(font.render(str(self.right_text), True, self.color_main), (right_font_pos[0], right_font_pos[1]))
        screen.blit(font.render(str(self.left_text), True, self.color_main), (left_font_pos[0], left_font_pos[1]))


    def slide_button(self, x):
        if self.position[0] <= x <= self.position[0] + self.height_slider:
            self.x_button = x
            self.value = (x - self.position[0]) * self.VpP + self.min_value


    def change_colors(self, color_main, color_button):
        self.color_main = color_main
        self.color_button = color_button


    def change_set_values(self, minimum, maximum):
        if minimum < maximum:
            self.min_value = minimum
            self.max_value = maximum
            self.count_VpP()


    def change_texts(self, left_txt="", right_txt=""):
        self.left_text = left_txt
        self.right_text = right_txt


def control_movement(slider, mouse_x, mouse_y):
    if slider.x_button - slider.height_button <= mouse_x <= slider.x_button + slider.height_button:
        if slider.y_button <= mouse_y <= slider.y_button + slider.width_button:
            slider.slide_button(mouse_x)



if __name__ == '__main__':
    pygame.init()
    main_font = pygame.font.SysFont('Calibri', 30)
    clock = pygame.time.Clock()
    slider = Slider((100,100))
    slider.right_text = "право"
    slider.left_text = 'Лево'
    screen = pygame.display.set_mode((800, 600))
    Test = True
    while Test:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Test = False
        screen = pygame.display.set_mode((800, 600))
        left, middle, right = pygame.mouse.get_pressed()
        if left:
            x, y = pygame.mouse.get_pos()
            control_movement(slider, x, y)
        print(slider.value)


        slider.draw(screen, main_font, (200,200), (300,200))
        pygame.display.flip()
        screen.fill((0,0,0))
        clock.tick(60)
    print(slider.position)