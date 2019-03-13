from Fighter.Vector import Vector
from Fighter.Resource import Resource
from Fighter.Fireball import Fireball

GRAVITY = Vector(0, 0.4)
class Character:
    def __init__(self, sprite, start_position, vel, player_number, facing):
        self.sprite = sprite
        self.pos = start_position
        self.vel = vel
        self.p_number = player_number
        self.energy = Resource(0, 20)#TODO
        self.health = Resource(100, 100)#TODO
        self.lives = Resource(3, 3)#TODO
        self.facing = facing
        self.block = False
        self.jumping = False
        self.jumpTime = 0
        self.ready = True
        self.fireBall = Fireball(player_number, facing)
        self.head = self.getHead()
        self.feet = self.getFeet()
        self.left_edge = self.getLeftEdge()
        self.right_edge = self.getRightEdge()

    #These methods define the bounds of the hurtbox
    def update_boundaries(self):
        self.head = self.getHead()
        self.feet = self.getFeet()
        self.left_edge = self.getLeftEdge()
        self.right_edge = self.getRightEdge()

    def getHead(self):
        return (self.pos.getY() - (self.sprite.spriteDim[1] / 2))

    def getFeet(self):
        return (self.pos.getY() + (self.sprite.spriteDim[1] / 2))

    def getLeftEdge(self):
        return (self.pos.getX() - (self.sprite.spriteDim[0] / 2))

    def getRightEdge(self):
        return (self.pos.getX() + (self.sprite.spriteDim[0] / 2))

    #Defines direction that the character faces
    def setfacing(self, other):
        if self.pos.x < other.pos.x:
            self.facing = 'right'
        else:
            self.facing = 'left'

    #calculates damage when hit
    def hit(self, damage):
        if(self.block):
            damage = damage / 2
        self.health.remove(damage)
        print(damage)
        self.energy.add(2)
        if self.health.value <= 0:
            self.die()

    #moves character position
    def move(self):
        self.pos = self.pos + self.vel

    #method to kill character (should be extended)ee
    def die(self):
        self.lives.remove(1)
        self.health.restore()
        print(self.lives.value)
        if(self.lives.value == 0):
            print(self.p_number)
            print("has died")
            quit()

    #checks whether self is hit by other
    def check_hit(self, other):
        xcoord = other.x
        ycoord = other.y
        #print(xcoord)
        #print(ycoord)
        if self.left_edge <= xcoord:
            if xcoord <= self.right_edge:
                if self.head <= ycoord:
                    if ycoord <= self.feet:
                        #print("hit")
                        return True
        else:
            #print("miss")
            return False

    #attack method
    def punch(self, other):
        if self.jumping:
            self.jump_kick(other)
        else:
            if self.facing == 'left':
                fist = Vector(self.left_edge - 5, self.pos.getY())
            else:
                fist = Vector(self.right_edge + 5, self.pos.getY())
            if other.check_hit(fist):
                other.hit(10)

    #attack when jumping
    def jump_kick(self, other):
        if(self.facing == 'left'):
            leg = Vector(self.left_edge - 10, self.pos.getY())
        else:
            leg = Vector(self.right_edge + 10, self.pos.getY())
        if other.check_hit(leg):
            other.hit(15)

    #blocking
    def blocking(self):
        self.block = True

    #stops blocking
    def not_blocking(self):
        self.block = False

    def fire(self,other):
        if self.energy.value > 10:
            self.fireBall.shoot(self.pos, self.facing)

    def stop_fall(self):
        self.vel = Vector()
        self.jumping = False


    def fall(self):
        self.vel.add(GRAVITY)

    def attemptJump(self):
        if self.jumping:
           #print("jumping")
            pass
        else:
            #print("attempted jump")
            self.jump()

    def jump(self):
        self.vel.add(Vector(0, -4))
        self.jumping = True
        self.jumpTime = 0

    def update(self):
        self.energy.add(1)
        if self.jumping and self.jumpTime < 5:
            self.vel.add(Vector(0,-.6))
            self.jumpTime += 1
        elif not self.jumping and self.jumpTime >= 5:
            self.vel = Vector(self.vel.getX(), 0)
        self.move()
        self.update_boundaries()

    def draw(self, canvas, enemy):
        self.fireBall.update(canvas, enemy)
        self.update()
        self.sprite.setDest(self.pos.getP())
        self.sprite.update(canvas)
        canvas.draw_circle(self.pos.getP(),
                           (self.sprite.spriteDim[0] /2),
                           1,
                           'Blue')


