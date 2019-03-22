try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

class Background:
    def __init__(self):
        self.image = simplegui.load_image('https://i.ibb.co/ZmbB0Jr/backing.png')
        self.img_size = (640, 253)


    def draw(self, canvas):
        #canvas.draw_line((0, 50), (500, 50), 100,'rgb(0,191,255)') #sky
        #canvas.draw_line((0, 250), (500, 250), 300,'White') #middle
        #canvas.draw_line((0, 450), (500, 450), 100, 'rgb(205,201,201)') #platform and below
        canvas.draw_image(self.image, (self.img_size[0]//2, self.img_size[1]//2), self.img_size, (250,250), (500,500))

