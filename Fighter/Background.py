try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random

class Background:
    def __init__(self):
        images = {
            1 : "https://i.ibb.co/c29yz1Q/backing-min.jpg",
            2 : "https://i.ibb.co/0szzKCt/road-bkg.png",
            3 : "https://i.ibb.co/7tnp72w/city-roads.jpg"
        }

        i = random.randint(1,3)
        self.image = simplegui.load_image(images[i])
        self.img_size = (self.image.get_width(), self.image.get_height())


    def draw(self, canvas):
        #Display the background
        canvas.draw_image(self.image, (self.img_size[0]//2, self.img_size[1]//2), self.img_size, (250,250), (500,500))

        #the buttons for the user so they can quit, read the instructions or restart the game during the game
        buttonRadius = 20
        canvas.draw_circle((25, 40), buttonRadius, 10, 'Red', 'Red')
        canvas.draw_text("Exit", (15, 40), 12, "White")

        canvas.draw_circle((80, 40), buttonRadius, 10, 'Orange', 'Orange')
        canvas.draw_text("Controls", (60, 40), 12, "White")

        canvas.draw_circle((135, 40), buttonRadius, 10, 'Green', 'Green')
        canvas.draw_text("Menu", (120, 40), 12, "White")


