class Button:
    instances = []
    def __init__(self, light, dark, pos, size, display, message=None):
        self.__class__.instances.append(self)
        self.pos = pos
        self.size = size
        self.light = light
        self.dark = dark
        self.display = display
        self.message = message
        self.press = False

    def is_in(self, coords):
        return self.pos[0] <= coords[0] <= self.pos[0] + self.size[0] and self.pos[1] <= coords[1] <= self.pos[1] + self.size[1]

    def __repr__(self):
        return 'Button'



class Square(Button):
    def __init__(self, pos):
        self.__class__.instances.append(self)
        self.pos = pos
        self.size = (250, 247)
        self.light = (255, 255, 255)
        self.dark = (185, 185, 185)
        self.press = False
        self.img = None

    def __repr__(self):
        return 'Square'

