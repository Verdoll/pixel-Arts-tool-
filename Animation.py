
class Animation():
    def __init__(self, frame, mode):
        self.frame = frame
        self.list_of_canvas = [frame]
        self.current_frame_index = 0
        self.FPS = 8
        self.mode = mode


    def new_frame(self):
        empty_grid = [[(0,0,0) for _ in range(32)] for _ in range(32)]
        self.list_of_canvas.append(empty_grid)


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


def main():
    pass

if __name__ == '__main__':
    main()