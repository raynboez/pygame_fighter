try:
    import simplegui
except ImportError:
        import SimpleGUICS2Pygame as simplegui

class Spritelives:
    def __init__(self, pos, lives):
        self.image = simplegui._load_local_image('spritelives.jpg')
        #self.image = simplegui.image._load_local_image('spritelives.jpg')
        self.pos = pos
        self.size = (90,30)
        self.dims = (3,1) #columns x rows
        self.window = (30, 30)
        self.current = [2,0]
        self.lives =  lives


    def draw(self, canvas):
        self.framewidth = 30 # can change this to self.window[0]
        self.frameheight = 30
        self.frameCentreX = (self.framewidth/2) + (self.lives * self.framewidth)
        self.frameCentreY = (self.frameheight/2) + (self.lives * self.frameheight)
        #canvas.draw_image(image, center_source, width_height_source, center_dest, width_height_dest)
        canvas.draw(self.image, (self.frameCentreX, self.frameCentreY), self.window, self.pos, self.window)

def drawing(canvas):
    sprite1 = Spritelives((150, 150), 3)
    sprite1.draw(canvas)


frame = simplegui.create_frame("Lives", 500, 500)
frame.set_canvas_background('#0000ff')
frame.set_draw_handler(drawing())


frame.start()