try:
    import simplegui
except ImportError:
        import SimpleGUICS2Pygame.simpleguics2pygame as simplegui


class Spritelives:
    def __init__(self, pos, lives, scale = 1):
        self.image = simplegui._load_local_image('.\\Sprites\\lives_sprite.png')
        self.pos = pos
        self.size = (90,30)
        self.dims = (3,1) #columns x rows
        self.window = (30, 30)
        self.current = [2,0]
        self.lives = lives


    def draw(self, canvas):
        self.framewidth = 30 # can change this to self.window[0]
        self.frameheight = 30
        self.frameCentreX = (self.lives * self.framewidth/2)
        self.frameCentreY = (self.frameheight/2)
        #self.dims = self.size / 2
        #canvas.draw_image(image, center_source, width_height_source, center_dest, width_height_dest)
        canvas.draw_image(self.image, (self.frameCentreX, self.frameCentreY), self.size, self.pos, (90,30))
        #canvas.draw_image(self.image, (150, 100), self.window, (200, 200), self.window)
        #canvas.draw_image(self.image, (self.size[0]/2, self.size[1]/2), self.size, (200,200), (90, 30))

sprite1 = Spritelives((150, 150), 3)


def draw(canvas):
    sprite1.draw(canvas)

frame = simplegui.create_frame("Lives", 500, 500)
#frame.set_canvas_background('#0000ff')
frame.set_draw_handler(draw)
frame.start()