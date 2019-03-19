try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from Fighter.Keyboard import Keyboard
class Frame:

    def __init__(self, NAME, CANVAS_WIDTH, CANVAS_HEIGHT):
        self.frame = simplegui.create_frame(NAME, CANVAS_WIDTH, CANVAS_HEIGHT)

    def setDrawHandler(self, draw):
        self.frame.set_draw_handler(draw)

    def setKeydownHandler(self, kbd):
        self.frame.set_keydown_handler(kbd.key_down)

    def setKeyupHandler(self, kbd):
        self.frame.set_keyup_handler(kbd.key_up)

    def start(self):
        self.frame.start()
