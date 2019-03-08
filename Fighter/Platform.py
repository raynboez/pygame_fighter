class Platform:
    def __init__(self, canvas_width, desired_height, line_width, colour):
        self.width = canvas_width
        self.y_pos = desired_height
        self.colour = colour
        self.line_width = line_width

    def draw(self, canvas):
        canvas.draw_line((0, self.y_pos),(self.width, self.y_pos), self.line_width, self.colour)

