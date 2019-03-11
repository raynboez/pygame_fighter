from Fighter.Sprite import Sprite
from Fighter.Vector import Vector
class Fireball:
    def __init__(self, player, direction):
        self.player_number = player
        self.pos = Vector(-100,-100)
        self.direction = direction
        self.sprite = self.set_sprite()
        self.vel = Vector(0,0)

    def setvel(self, direction, x=0):
        if direction == 'left':
            vel = Vector(-x, self.vel.getY())
        else:
            vel = Vector(x, self.vel.getY())
        return vel

    def move(self):
        self.pos = self.pos + self.vel

    def shoot(self, starting, direction):
        self.pos = starting
        self.vel = self.setvel(direction, 10)

    def stop(self):
        self.pos = Vector(-50,-50)
        self.vel = Vector()

    def set_sprite(self):
        if self.player_number == '1':
            img = Sprite(".\\Sprites\\PlaceHolder.png", 180, 350, 7, 6, (400, 300), 1)
        else:
            img = Sprite(".\\Sprites\\PlaceHolder.png", 180, 350, 7, 6, (400, 300), 1)
        return img

    def draw(self, canvas):
        #self.sprite.update(canvas)
        canvas.draw_circle(
                            self.pos.getP(),
                            10,
                            1,
                            'Red'
        )
    def update(self, canvas, enemy):
        self.draw(canvas)
        self.move()
        if enemy.check_hit(self.pos):
            print("hit")
            enemy.hit(15)
            self.stop()
        if self.off_screen(canvas):
            self.stop()

    def off_screen(self, canvas):
        return self.pos.x < 0 or self.pos.x > 500