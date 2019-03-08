from Fighter.Sprite import Sprite
from Fighter.Vector import Vector
class Fireball:
    def __init__(self, player, initial, direction):
        self.player_number = player
        self.pos = initial
        self.vel = Vector(0,0)
        self.direction = direction
        self.sprite = self.set_sprite()

    def set_pos_and_fire(self, position, velocity, direction):
        self.pos = position
        self.vel = velocity
        self.direction = direction

    def stop(self):
        self.pos = Vector(-50,-50)
        self.vel = Vector(0,0)

    def set_sprite(self):
        if self.player_number == '1':
            img = Sprite(".\\Sprites\\PlaceHolder.png", 180, 350, 7, 6, (400, 300), 1)
        else:
            img = Sprite(".\\Sprites\\PlaceHolder.png", 180, 350, 7, 6, (400, 300), 1)
        return img

    def draw(self, canvas):
        self.sprite.update(canvas)

    def update(self, other, canvas):
        self.draw(canvas)
        if(self.direction == 'right'):
            self.pos.add(self.vel)
        else:
            self.pos.subtract(self.vel)
        if other.checkhit(self):
            other.hit(15)
            self.stop()