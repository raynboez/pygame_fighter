try:
    import simplegui
except ImportError:
        import SimpleGUICS2Pygame as simplegui

from Fighter.Resources import Resources
from Fighter import Vector


class Rounds:
    player1_start = Vector() #TODO
    player2_start = Vector()
    text_pos = Vector()

    def __init__(self, player1, player2):
        global player1_start, player2_start
        player1.health = Resource.lifeBar(100)  # TODO - not sure how to
        player2.health = Resource.lifeBar(100)  # TODO - not sure how to
        player1.pos = player1_start
        player2.pos = player2_start

    def draw(canvas, text):
        global text_pos
        canvas.draw_text(text, text_pos, 12, 'Blue')

    def end(canvas, text):
        canvas.draw_text(text + "has won!", text_pos, 12, 'Blue')


frame = simplegui.create_frame('Rounds', 1000, 1000)
frame.set_draw_handler(draw("New Round"))
frame.start()