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
        #Display the background
        canvas.draw_image(self.image, (self.img_size[0]//2, self.img_size[1]//2), self.img_size, (250,250), (500,500))

        #the buttons for the user so they can quit, read the instructions or restart the game during the game
        canvas.draw_circle((30, 40), 20, 10, 'Red', 'Red')
        canvas.draw_text("Exit", (15, 75), 13, "Black")

        canvas.draw_circle((80, 40), 20, 10, 'Orange', 'Orange')
        canvas.draw_text("Instructions", (40, 74), 13, "Black")

        canvas.draw_circle((130, 40), 20, 10, 'Green', 'Green')
        canvas.draw_text("Restart", (120, 74), 13, "Black")


