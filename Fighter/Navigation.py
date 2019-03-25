try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from Fighter.Platform import Platform
from Fighter.Sprite import Sprite
from Fighter.Character import Character
from Fighter.Keyboard import Keyboard
from Fighter.Interaction import Interaction
from Fighter.Vector import Vector
from Fighter.Wall import Wall
from Fighter import GameLoop
from Fighter.Cursor import Cursor

class Navigation:

    def __init__(self, cursor, keyboard, player):
        self.cursor = cursor
        self.kbd = keyboard
        self.player = player
        self.timer = 0
    def update(self):
        if self.timer > 4:
            if self.kbd.right[self.player] and not self.cursor.getSelected():
                self.timer = 0
                self.cursor.nextColumn()

            if self.kbd.left[self.player] and not self.cursor.getSelected():
                self.timer = 0
                self.cursor.previousColumn()

            if self.kbd.down[self.player] and not self.cursor.getSelected():
                self.timer = 0
                self.cursor.nextRow()

            if self.kbd.up[self.player] and not self.cursor.getSelected():
                self.timer = 0
                self.cursor.previousRow()

            if self.kbd.attack[self.player]:
                self.timer = 0
                self.cursor.select()

            if self.kbd.fire[self.player]:
                self.timer = 0
                self.cursor.deselect()
        self.timer+=1
