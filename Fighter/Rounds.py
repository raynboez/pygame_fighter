try:
    import simplegui
except ImportError:
        import SimpleGUICS2Pygame as simplegui

from Fighter import Resource
from Fighter import Vector
from Fighter import Spritelives


class Rounds:
    player1_start = Vector() #TODO
    player2_start = Vector()
    text_pos = 150,100

    def __init__(self, player1, player2):
        global player1_start, player2_start
        player1.health = Resource.lifeBar(100)  # TODO - not sure how to
        player2.health = Resource.lifeBar(100)  # TODO - not sure how to
        player1.pos = player1_start
        player2.pos = player2_start
        self.gameend = False

    def draw(self,  canvas, text):
        global text_pos
        if (self.gameend == True):
            canvas.draw_text(text, text_pos, 12, 'Blue')

    def lifedraw(self, canvas, player):
        if (player == 1):
            Spritelives() ## get the method here
            canvas.draw_image(image, center_source, width_height_source, center_dest, width_height_dest)
        if (player ==2):
            canvas.draw_image(image, center_source, width_height_source, center_dest, width_height_dest)



    def end(canvas, text):
        canvas.draw_text(text + "has won!", text_pos, 12, 'Blue')

    def gameend(self):
        if (self.lives == 0):
            self.gameend = True
        #go to main menu


frame = simplegui.create_frame('Rounds', 1000, 1000)
frame.set_draw_handler(draw("New Round"))
frame.start()