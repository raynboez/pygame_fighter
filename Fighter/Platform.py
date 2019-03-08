class Platform:
    def __init__(self, canvas_width, desired_height, line_width, colour):
        self.width = canvas_width
        self.y_pos = desired_height
        self.colour = colour
        self.line_width = line_width
        self.edge_top = desired_height - 1 - (line_width / 2)
        self.edge_bottom = desired_height + 1 + (line_width / 2)

    def draw(self, canvas):
        canvas.draw_line((0, self.y_pos),(self.width, self.y_pos), self.line_width, self.colour)

    def touch(self, character):
        hit_top = (character.feet() >= self.edge_top)
        hit_bottom = (character.head() <= self.edge_bottom)
        if hit_top:
            return True
        return False


