class Navigation:

    def __init__(self, cursor, keyboard, player):
        self.cursor = cursor
        self.kbd = keyboard
        self.player = player
        self.timer = 0


    def update(self):
        if self.timer > 7:
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
