try:
    import simplegui
except ImportError:
        import SimpleGUICS2Pygame.simpleguics2pygame as simplegui


class Spritelives:
    def __init__(self, pos, lives, scale = 1):
        self.image = simplegui.load_image('https://i.ibb.co/pr8MjQj/lives-sprite.png')
        self.pos = pos
        self.size = (self.image.get_width(),self.image.get_height())
        self.window = (30, 30)
        self.current = [0,0]
        self.center = [self.window[0]/2, self.window[1]/2]
        self.lives = lives

    def update(self, lives, canvas):
        self.lives = lives
        self.draw(canvas)

    def draw(self, canvas):
         canvas.draw_image(self.image, ((self.center[0] * self.lives), self.center[1]), (self.window[0]*self.lives, self.window[1]), self.pos, (self.window[0]*self.lives, self.window[1]))

