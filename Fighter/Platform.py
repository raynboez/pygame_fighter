class Platform:
    #initialise platform with length, y-placement, width and colour
    def __init__(self, canvas_width, desired_height, line_width, colour):
        self.width = canvas_width
        self.y_pos = desired_height
        self.colour = colour
        self.line_width = line_width
        self.edge_top = desired_height - (line_width / 2) + 1
        self.edge_bottom = desired_height + (line_width / 2) - 1

    #draw line on canvas
    def draw(self, canvas):
        canvas.draw_line((0, self.y_pos),(self.width, self.y_pos), self.line_width, self.colour)

    #checks if a character is touching a platform
    def touch(self, character):
        return (character.feet >= self.edge_top)


