from Fighter.Vector import Vector
from Fighter.Resource import Resource
from Fighter.Fireball import Fireball

GRAVITY = Vector(0, 2)
class Character:
    def __init__(self, sprite, start_position, vel, player_number, facing):
        self.sprite = sprite
        self.pos = start_position
        self.vel = vel
        self.p_number = player_number
        self.energy = Resource(0)#TODO
        self.health = Resource(100)#TODO
        self.lives = Resource(3)#TODO
        self.facing = facing
        self.blocking = False
        self.jumping = False
        self.ready = True
        self.fireBall = Fireball(player_number, (-50,-50), facing)

    #These methods define the bounds of the hurtbox
    def head(self):
        return self.pos.getY() - (self.sprite.spriteDim[1] / 2)

    def feet(self):
        return self.pos.getY() + (self.sprite.spriteDim[1] / 2)

    def left_edge(self):
        return self.pos.getX() - (self.sprite.spriteDim[0] / 2)

    def right_edge(self):
        return self.pos.getX() - (self.sprite.spriteDim[0] / 2)

    #Defines direction that the character faces
    def facing(self, other):
        if self.pos.getX() < other.pos.getX():
            self.facing = 'right'
        else:
            self.facing = 'left'

    #calculates damage when hit
    def hit(self, damage):
        if(self.blocking):
            damage = damage / 2
        self.health.remove(damage)
        self.energy.add(2)
        if self.health.value <= 0:
            self.die()

    #moves character position
    def move(self):
        self.pos = self.pos + self.vel

    #method to kill character (should be extended)
    def die(self):
        self.lives-=1

    #checks whether self is hit by other
    def check_hit(self, other):
        if self.left_edge() <= other.getX() <= self.right_edge():
            if self.head() <= other.getY() <= self.feet():
                return True
        else:
            return False

    #attack method
    def punch(self, other):
        if self.facing == 'left':
            fist = Vector(self.pos.getX() - 5, self.pos.getY)
        else:
            fist = Vector(self.pos.getX() + 5, self.pos.getY)
        if self.jumping:
            self.jump_kick(other)
        elif other.check_hit(fist):
                other.hit(10)

    #attack when jumping
    def jump_kick(self, other):
        if other.check_hit(self):
            other.hit(15)

    #blocking
    def blocking(self):
        self.blocking = True

    #stops blocking
    def not_blocking(self):
        self.blocking = False

    def fire(self):
        if self.energy.value > 10:
            self.fireBall.set_pos_and_fire(self.pos, (4, 0), self.facing)

    def stop_fall(self):
        self.vel = Vector()

    def update(self):
        global GRAVITY
        self.energy.add(1)
        if self.jumping:
            self.vel.add(GRAVITY)
        self.move()

    def draw(self, canvas):
        self.update()
        self.sprite.setDest(self.pos.getP())
        self.sprite.update(canvas)
        canvas.draw_circle(self.pos.getP(),
                           (self.sprite.spriteDim[0] /2),
                           1,
                           'Blue')


