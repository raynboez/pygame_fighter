try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

class Background:
    def __init__(self):
        pass

    def draw(self, canvas):
        canvas.draw_line((0, 50), (500, 50), 100,'rgb(0,191,255)') #sky
        canvas.draw_line((0, 250), (500, 250), 300,'White') #middle
        canvas.draw_line((0, 450), (500, 450), 100, 'rgb(205,201,201)') #platform and below

    #frame = simplegui.create_frame("Background", 500, 500)
    #frame.set_draw_handler(draw)
    #frame.start()