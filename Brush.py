class Brush():
    def __init__(self, size, color, mode):
        self.size = size
        self.color = color
        self.mode = mode


    def change_color(self, new_color):
        self.color = new_color


    def change_size(self, new_size):
        self.size = new_size


    def change_mode(self, new_mode):
        self.mode = new_mode


#test func
def main():
    brush = Brush(1, (11,12,21))


if __name__ == '__main__':
    main()
