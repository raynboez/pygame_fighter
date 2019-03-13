try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui


class Keyboard:
    def __init__(self):
        self.right = [False,False]
        self.left = [False,False]
        self.up = [False,False]
        self.down = [False,False]
        self.attack = [False,False]
        self.fire = [False,False]
        self.key_binds = ['w','a','s','d','q','e','i','j','k','l','u','o']

    def key_down(self, key):
        if key == simplegui.KEY_MAP[self.key_binds[3]]:
            self.right[0] = True
        if key == simplegui.KEY_MAP[self.key_binds[1]]:
            self.left[0] = True
        if key == simplegui.KEY_MAP[self.key_binds[0]]:
            self.up[0] = True
        if key == simplegui.KEY_MAP[self.key_binds[2]]:
            self.down[0] = True
        if key == simplegui.KEY_MAP[self.key_binds[5]]:
            self.attack[0] = True
        if key == simplegui.KEY_MAP[self.key_binds[4]]:
            self.fire[0] = True
        if key == simplegui.KEY_MAP[self.key_binds[9]]:
            self.right[1] = True
        if key == simplegui.KEY_MAP[self.key_binds[7]]:
            self.left[1] = True
        if key == simplegui.KEY_MAP[self.key_binds[6]]:
            self.up[1] = True
        if key == simplegui.KEY_MAP[self.key_binds[8]]:
            self.down[1] = True
        if key == simplegui.KEY_MAP[self.key_binds[11]]:
            self.attack[1] = True
        if key == simplegui.KEY_MAP[self.key_binds[10]]:
            self.fire[1] = True

    def key_up(self, key):
        if key == simplegui.KEY_MAP[self.key_binds[3]]:
            self.right[0] = False
        if key == simplegui.KEY_MAP[self.key_binds[1]]:
            self.left[0] = False
        if key == simplegui.KEY_MAP[self.key_binds[0]]:
            self.up[0] = False
        if key == simplegui.KEY_MAP[self.key_binds[2]]:
            self.down[0] = False
        if key == simplegui.KEY_MAP[self.key_binds[5]]:
            self.attack[0] = False
        if key == simplegui.KEY_MAP[self.key_binds[4]]:
            self.fire[0] = False
        if key == simplegui.KEY_MAP[self.key_binds[9]]:
            self.right[1] = False
        if key == simplegui.KEY_MAP[self.key_binds[7]]:
            self.left[1] = False
        if key == simplegui.KEY_MAP[self.key_binds[6]]:
            self.up[1] = False
        if key == simplegui.KEY_MAP[self.key_binds[8]]:
            self.down[1] = False
        if key == simplegui.KEY_MAP[self.key_binds[11]]:
            self.attack[1] = False
        if key == simplegui.KEY_MAP[self.key_binds[10]]:
            self.fire[1] = False