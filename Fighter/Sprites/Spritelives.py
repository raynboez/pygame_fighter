try:
    import simplegui
except ImportError:
        import SimpleGUICS2Pygame as simplegui

class Spritelives:
    def __init__(self, pos, lives):
        self.image = simplegui.load_local_image('assets_gutenberg.jpg')
        self.pos = pos
        self.size = (90,30)
        self.dims = (3,1)
        self.window = (500, 500)
        self.current = [0,0]
        self.lives =  lives


    def draw(self, canvas):
        #canvas.draw_image(image, center_source,
        # width_height_source, center_dest, width_height_dest)
        x = self.current[0]
        y =
        canvas.draw(self.image, )
