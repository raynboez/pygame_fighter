try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from Fighter.Platform import Platform
from Fighter.Sprite import Sprite

CANVAS_WIDTH = 500
CANVAS_HEIGHT = 500
NAME = 'TestFrame'


def init():
    frame.start()


def draw(canvas):
    platform_top.draw(canvas)
    platform_bottom.draw(canvas)
    #characterTest.update(canvas)


characterTest = Sprite("C:\\Users\\Ben\\Downloads\\sprites\\sprite.png", 1440, 1480, 5, 6, (250,250), 1)
platform_top = Platform(CANVAS_WIDTH, 100, 10, 'Grey')
platform_bottom = Platform(CANVAS_WIDTH, 400, 10, 'Grey')
frame = simplegui.create_frame(NAME, CANVAS_WIDTH, CANVAS_HEIGHT)
frame.set_draw_handler(draw)

