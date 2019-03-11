try:
    import simplegui
except ImportError:
        import SimpleGUICS2Pygame as simplegui

class Resources:
    def __init__(self, resource):
        self.resource = resource

    def remove(self, num):
        self.resource = self.resource - num

    def add(self, num):
        self.resource = self.resource + num

    def lifeBar(self):
        draw()

    def getRes(self):
        return self

    def draw(canvas, point1, point2):
        canvas.draw_line(point1, point2, 15, 'Red')

    def update(self):
        pass

test = Resources()


def draw():
    test.lifeBar().update()


frame = simplegui.create_frame('Fight', 200, 200)
frame.set_draw_handler(draw)
frame.start()