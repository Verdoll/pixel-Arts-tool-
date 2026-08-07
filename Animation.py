import copy
import pygame
import colors as cl
import sliders

class Animation():
    def __init__(self, frame, mode):
        self.frame = frame
        self.list_of_canvas = [frame]
        self.current_frame_index = 0
        self.FPS = 8
        self.mode = mode

    def new_frame(self, setting):
        if setting.coppyng:
            new_grid = copy.deepcopy(self.list_of_canvas[-1])
            self.list_of_canvas.append(new_grid)
        else:
            empty_grid = [[(0,0,0) for _ in range(32)] for _ in range(32)]
            self.list_of_canvas.append(empty_grid)


    def change_FPS(self, num):
        self.FPS = num


    def delete_frame(self):
        if self.current_frame_index != 0:
            self.list_of_canvas.pop(self.current_frame_index)
            self.current_frame_index -= 1
        elif self.current_frame_index == 0 and len(self.list_of_canvas) == 1:
            empty_grid = [[(0,0,0) for _ in range(32)] for _ in range(32)]
            self.list_of_canvas[self.current_frame_index] = empty_grid
        else:
            self.list_of_canvas.pop(self.current_frame_index)

    def change_frame(self, num):
        if num > 0:
            if self.current_frame_index + 2 <= len(self.list_of_canvas):
                self.current_frame_index += 1
                return self.list_of_canvas[self.current_frame_index]

        if num < 0 and self.current_frame_index != 0:
            self.current_frame_index -= 1
            return self.list_of_canvas[self.current_frame_index]
        return None


    def next_frame(self):
        if self.current_frame_index + 1 < len(self.list_of_canvas):
            self.current_frame_index += 1
        else:
            self.current_frame_index = 0
        return self.list_of_canvas[self.current_frame_index]


    def swap_mode(self):
        if self.mode == 'drawing':
            self.mode = 'animation'
        elif self.mode == 'animation':
            self.mode = 'drawing'

slider = sliders.Slider((1050,400), 3, 140, 20, 10, 3, 24, cl.white, cl.white)
slider.change_texts('', int(slider.value))

def draw(screen, main_font, cell_size, boolean):
    pygame.draw.rect(screen, cl.white, (1035, 320, cell_size * 5, cell_size * 2), 1)
    screen.blit(main_font.render('анимация', True, cl.white), (1037, 326))

    pygame.draw.rect(screen, cl.main_gray, (1145, 320, cell_size * 5-10, cell_size * 2))
    if boolean:
        slider.change_texts('', int(slider.value))
        pygame.draw.rect(screen, cl.main_orange, (1145, 320, cell_size * 5 - 10, cell_size * 2))
        pygame.draw.rect(screen, cl.main_gray, (1145-110, 370, cell_size * 10, cell_size * 3))
        pygame.draw.rect(screen, cl.white, (1145 - 110, 370, cell_size * 10, cell_size * 3), 2)

        slider.draw(screen, main_font, (1050, 400), (1203,387))

    pygame.draw.rect(screen, cl.white, (1145, 320, cell_size * 5-10, cell_size * 2), 1)
    screen.blit(main_font.render('FPS', True, cl.white), (1172, 328))


def touch_button(x, y):
    if 1144 <= x <= 1233 and 320 <= y <= 360:
        return True
    return False

def change_FPS_value(x, y, canvas):
    sliders.control_movement(slider, x, y)
    canvas.change_FPS(slider.value)


def main():
    pass

if __name__ == '__main__':
    main()