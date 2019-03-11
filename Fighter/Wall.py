class Wall:

    #requires x position, canvas height, colour
    def __init__(self, xpos, height, width,colour):
        self.x = xpos
        self.y = height
        self.line_width = width
        self.colour = colour
        self.lEdge = xpos - (width / 2)
        self.rEdge = xpos + (width / 2)

    def touch(self, character):
        if character.left_edge > self.lEdge and character.left_edge < self.rEdge:
            return 'left'
        if character.right_edge > self.lEdge and character.right_edge < self.rEdge:
            return 'right'

    def draw(self, canvas):
        canvas.draw_line((self.x, 0), (self.x, self.y), self.line_width, self.colour )