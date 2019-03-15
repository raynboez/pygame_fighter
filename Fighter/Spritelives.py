try:
    import simplegui
except ImportError:
        import SimpleGUICS2Pygame.simpleguics2pygame as simplegui


class Spritelives:
    def __init__(self, pos, lives, scale = 1):
        self.image = simplegui._load_local_image('.\\Sprites\\lives_sprite.png')
        self.pos = pos
        self.size = (90,30)
        self.window = (30, 30)
        self.current = [0,0]
        self.center = [self.window[0]/2, self.window[1]/2]
        self.lives = lives

    def draw(self, canvas):
         canvas.draw_image(self.image, ((self.center[0] * self.lives), self.center[1]), (self.window[0]*self.lives, self.window[1]), self.pos, (self.window[0]*self.lives, self.window[1]))

