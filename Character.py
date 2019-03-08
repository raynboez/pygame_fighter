from Fighter.Vector import Vector
from Fighter.Resource import Resource

class Character:
    def __init__(self, start_position, player_number, facing):
        self.pos = start_position
        self.p_number = player_number
        self.energy = Resource(0)#TODO
        self.health = Resource(100)#TODO
        self.lives = Resource(3)#TODO
        self.facing = facing
        self.blocking = False
        self.jumping = False

    def facing(self, other):
        if(self.pos.getP[0] < other.pos.getP[0]):
            self.facing = 'right'
        else:
            self.facing = 'left'

    def hit(self, num):
        if(self.blocking):
            num = num / 2
        self.health.remove(num)
        if(self.health <= 0):
            self.die()

    def die(self):
        #TODO
        pass

    def check_hit(self, other):
        ##TODO - if other is in self, return true
        return False

    def punch(self, other):
        if(self.jumping):
            self.jump_kick(other)
        elif(self.check_hit(other)):
                other.hit(10)

    def jump_kick(self, other):
        if(self.check_hit(other)):
            other.hit(15)

    def blocking(self):
        if(self.jumping == False)
            self.blocking = True

    def not_blocking(self):
        self.blocking = False

    def fire(self):
        if(self.energy > 10):
            #TODO hadouken
            pass

    def jump(self):
        if(self.jumping == False):
            self.jumping = True
            #TODO jump movement


    def update(self, canvas):
        self.energy+=1
        self.draw(canvas)

    def draw(self, canvas):
