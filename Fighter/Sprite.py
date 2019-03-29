try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui


states = {
        "idle"  : [0, 2],
        "walk"  : [2, 2],
        "jump"  : [12, 1],
        "kick"  : [13, 1],
        "hit"   : [11, 1],
        "punch" : [4, 2],
        "fire"  : [6, 2],
        "block" : [10, 1],
        "die"   : [8, 2],
        "fireball" : [0, 4],
        "off" : [0, 1],
        "on"    : [1, 1]
    }


class Sprite:

    #initialises sprite from local path, with spritesheet height and width, number of rows and columns, destination and size
    def __init__(self, path, rows, columns, destination, scale, state, facing):
        self.img = simplegui.load_image(path)
        self.spriteDim = [(self.img.get_width() / columns), self.img.get_height() / rows]
        self.dest = destination
        self.scaling = scale
        self.scale = (self.spriteDim[0] * scale, self.spriteDim[1] * scale)
        self.columns = columns
        self.rows = rows
        self.frameIndex = [0, 0]
        self.currentState = states[state]
        self.timer = 0
        self.facing = facing

    #sets destination of sprite (used in character class to update position
    def setDest(self, dest):
        self.dest = dest

    def changeState(self, state):
        self.currentState = states[state]

    def setFacing(self, direction):
        self.facing = direction

    def updateDirection(self):
        if self.facing == 'left':
            self.frameIndex[1] = 1
        else:
            self.frameIndex[1] = 0

    #moves to nextSprite
    def nextSprite(self):
        self.frameIndex[0] = self.currentState[0] + (self.frameIndex[0] + 1) % self.currentState[1]


    #draws sprite on canvas
    def draw(self, canvas):
        canvas.draw_image(self.img,
                                   (self.spriteDim[0] * self.frameIndex[0] + self.spriteDim[0] / 2,
                                   self.spriteDim[1] * self.frameIndex[1] + self.spriteDim[1] / 2),
                                   (self.spriteDim[0], self.spriteDim[1]),
                                    self.dest,
                                    self.scale
                                   )

    #draws sprite and cycles to next
    def update(self, canvas, position):
        self.updateDirection()
        self.setDest(position)
        self.draw(canvas)
        if self.timer % 10 == 0:
            self.nextSprite()
        self.timer += 1

    def updateStatic(self, canvas):
        self.updateDirection()
        self.draw(canvas)
        if self.timer % 10 == 0:
            self.nextSprite()
        self.timer += 1


class StaticSprite:

    def __init__(self, path, destination, scale):
        self.img = simplegui.load_image(path)
        self.spriteDim = [self.img.get_width(), self.img.get_height()]
        self.dest = destination
        self.scaling = scale
        self.scale = (self.spriteDim[0] * scale, self.spriteDim[1] * scale)
        self.columns = 1
        self.rows = 1
        self.frameIndex = [0, 0]
        self.timer = 0

    # sets destination of sprite (used in character class to update position
    def setDest(self, dest):
        self.dest = dest

    # draws sprite on canvas
    def draw(self, canvas):
        canvas.draw_image(self.img,
                          (self.spriteDim[0] * self.frameIndex[0] + self.spriteDim[0] / 2,
                           self.spriteDim[1] * self.frameIndex[1] + self.spriteDim[1] / 2),
                          (self.spriteDim[0], self.spriteDim[1]),
                          self.dest,
                          self.scale
                          )

    # draws sprite and cycles to next
    def update(self, canvas, position):
        self.setDest(position)
        self.draw(canvas)
        self.timer += 1
