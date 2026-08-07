class Program():
    def __init__(self):
        self.rgb_window = False
        self.self_color = False
        self.FPS_window = False
        self.animation_window = False


    def touch_rgb(self):
        self.rgb_window = not self.rgb_window

    def swap_self_color(self):
        self.self_color = not self.self_color

    def disable_self_color(self):
        self.self_color = False

    def swap_fps_window(self):
        self.FPS_window = not self.FPS_window

    def swap_animation_window(self):
        self.animation_window = not self.animation_window