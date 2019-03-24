try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui


class Background:
    def __init__(self):
        #self.image = simplegui.load_image('https://i.ibb.co/ZmbB0Jr/backing.png') #option 1
        #self.image = simplegui.load_image('https://i.ibb.co/c29yz1Q/backing-min.jpg') #option 1 compressed image
       # self.image = simplegui.load_image('https://i.ibb.co/0szzKCt/road-bkg.png') #option 2
        self.image = simplegui.load_image('https://i.ibb.co/7tnp72w/city-roads.jpg') #option 3
       # self.img_size = (640, 253) option 1
        #self.img_size = (640,308) #option 2
        self.img_size = (626, 375) #option 3

    def draw(self, canvas):
        canvas.draw_image(self.image, (self.img_size[0]//2, self.img_size[1]//2), self.img_size, (250,250), (500,500))


