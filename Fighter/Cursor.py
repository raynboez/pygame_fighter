class Cursor:

    def __init__(self, coord1, coord2, coord3, coord4, colour):
        self.positions = [[], []]
        initialpos = [coord1, coord2, coord3, coord4]
        self.positions[0].append(initialpos)
        self.position = [0, 0]
        self.colour = colour
        self.selected = False

    def addPos(self, coord1, coord2, coord3, coord4, row):
        self.positions[row].append([coord1, coord2, coord3, coord4])

    def nextColumn(self):
        if self.position[0] >= len(self.positions[0]) - 1:
            self.position[0] = 0
        else:
            self.position[0] += 1

    def previousColumn(self):
        if self.position[0] <= 0:
            self.position[0] = len(self.positions[0]) - 1
        else:
            self.position[0] -= 1

    def nextRow(self):
        if self.position[1] >= len(self.positions[1]) - 1:
            self.position[1] = 0
        else:
            self.position[1] += 1

    def previousRow(self):
        if self.position[1] <= 0:
            self.position[1] = len(self.positions[1]) - 1
        else:
            self.position[1] -= 1

    def draw(self, canvas):
        coord1 = self.positions[self.position[1]][self.position[0]][0]
        coord2 = self.positions[self.position[1]][self.position[0]][1]
        coord3 = self.positions[self.position[1]][self.position[0]][2]
        coord4 = self.positions[self.position[1]][self.position[0]][3]
        #draw polygon from coordinates
        canvas.draw_polygon([coord1, coord2, coord3, coord4], 2, self.colour)


    def previewSelection(self):
        if self.position == [0, 0]:
            return 0
        if self.position == [0, 1]:
            return 1
        if self.position == [1,0]:
            return 2
        if self.position == [1,1]:
            return 3

    def getSelected(self):
        return self.selected

    def select(self):
        self.selected = True

    def deselect(self):
        self.selected = False

    def getSelection(self):
        if self.position == [0, 0]:
            return "Red"
        if self.position == [0, 1]:
            return "Blue"
        if self.position == [1,0]:
            return "Green"
        if self.position == [1,1]:
            return "Yellow"