try:
    import simplegui
except ImportError:
        import SimpleGUICS2Pygame as simplegui


class Keyboard:
    def __init__(self):
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.space = False

    def keyRight(self, key):
        if key == simplegui.KEY_MAP['right']:
            self.right = True

    def keyLeft(self, key):
        if key == simplegui.KEY_MAP['left']:
            self.left = True

    def keyUp(self, key):
        if key == simplegui.KEY_MAP['up']:
            self.right = True

    def keyDown(self, key):
        if key == simplegui.KEY_MAP['down']:
            self.left = True

    def keySpace(self, key):
        if key == simplegui.KEY_MP['space']:
            self.space = True


kdb = Keyboard()