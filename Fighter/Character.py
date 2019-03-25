from Fighter.Vector import Vector
from Fighter.Resource import Resource
from Fighter.Fireball import Fireball
from Fighter.Spritelives import Spritelives

GRAVITY = Vector(0, 0.4) #Tuned to get jumps looking correct - dont touch

states = {
    "idle" : "interruptable",
    "walk" : "interruptable",
    "punch" : "non",
    "jump"  : "interruptable",
    "kick"  : "interruptable",
    "fire" : "non",
    "hit" : "non",
    "block" : "non",
    "die" : "non"
}

class Character:
    def __init__(self, sprite, start_position, player_number, facing):
        self.sprite = sprite
        self.startpos = start_position
        self.startvel = Vector()
        self.newLife()
        self.dead = False
        self.p_number = player_number
        ##these numbers need balancing
        self.lives = Resource(3,3)
        self.lifespritex = 350
        if self.p_number == 1:
            self.lifespritex = 150
        self.lifeSprite = Spritelives((self.lifespritex, 485), self.lives.value)
        #used in calculations for punches and fireballs
        self.facing = facing
        self.currentState = "idle"
        #used as states
        self.block = False
        self.jumping = False
        self.jumpTime = 0
        self.fireball_ready = True
        self.punch_cooldown = 0
        self.punch_cooldown_max = 20
        self.punch_ready = True
        self.stateTimer = 0

        #creates a fireball object bound to this character
        self.fireBall = Fireball(self, self.facing)

        #sets collision boundaries
        self.head = self.getHead()
        self.feet = self.getFeet()
        self.left_edge = self.getLeftEdge()
        self.right_edge = self.getRightEdge()


    #These methods define the bounds of the hurtbox, uses dimensions of sprite, subject to change
    def update_boundaries(self):
        self.head = self.getHead()
        self.feet = self.getFeet()
        self.left_edge = self.getLeftEdge()
        self.right_edge = self.getRightEdge()

    def getHead(self):
        return (self.pos.getY() - (self.sprite.scaling * (self.sprite.spriteDim[1] / 2)))

    def getFeet(self):
        return (self.pos.getY() + (self.sprite.scaling * (self.sprite.spriteDim[1] / 2)))

    def getLeftEdge(self):
        return (self.pos.getX() - (self.sprite.scaling * (self.sprite.spriteDim[0] / 2)))

    def getRightEdge(self):
        return (self.pos.getX() + (self.sprite.scaling * (self.sprite.spriteDim[0] / 2)))


    def setSprite(self, sprite, fireballcolour):
        self.sprite = sprite
        self.fireBall.set_sprite(fireballcolour)

    #Defines direction that the character faces
    def setfacing(self, other):
        if self.pos.x < other.pos.x:
            self.facing = 'right'
            self.sprite.setFacing(self.facing)
        else:
            self.facing = 'left'
        self.sprite.setFacing(self.facing)
        self.fireBall.setFacing(self.facing)

    #calculates damage when hit, blocking halves the damage
    def hit(self, damage):
        self.setState("hit")
        if(self.block):
            damage = damage / 2
        self.health.remove(damage)
        self.energy.add(2)
        if self.health.value <= 0:
            self.die()

    #moves character position
    def move(self):
        self.pos = self.pos + self.vel

    #method to kill character (needs to be extended to incorporate round system
    def die(self):
        if not self.dead:
            self.lives.remove(1)
            self.setState("die")
            self.dead = True

    def distance(self, other):
        return (self.pos.getX() - other.pos.getX())

    def newLife(self):
        self.energy = Resource(0, 100)#TODO
        self.energycounter = 0
        self.health = Resource(100, 100)#TODO
        self.pos = self.startpos
        self.vel = self.startvel
        self.dead = False

    #checks whether self is hit by other
    def check_hit(self, other):
        xcoord = other.x
        ycoord = other.y
        if self.left_edge + 15 <= xcoord:
            if xcoord <= self.right_edge - 15:
                if self.head <= ycoord:
                    if ycoord <= self.feet:
                        #character hit
                        self.setState("hit")
                        return True
        else:
            #missed
            return False

    #attack method
    def punch(self, other):
        if self.punch_ready:
            self.punch_ready = False
            self.punch_cooldown = self.punch_cooldown_max
            if self.jumping:
                #use jump_kick method instead
                self.jump_kick(other)
            else:
                self.setState("punch")
                if self.facing == 'left':
                    #punch left (change distance - currently 5 pixels
                    fist = Vector(self.left_edge, self.pos.getY())
                else:
                    #punch right
                    fist = Vector(self.right_edge, self.pos.getY())
                if other.check_hit(fist):
                    other.hit(10)



    #attack when jumping
    def jump_kick(self, other):
        self.setState("kick")
        if(self.facing == 'left'):
            #kick left (currently 10 pixels
            leg = Vector(self.left_edge, self.pos.getY())
        else:
            #kick right
            leg = Vector(self.right_edge, self.pos.getY())
        if other.check_hit(leg):
                other.hit(15)

    #blocking
    def blocking(self):
        self.block = True

    #stops blocking
    def not_blocking(self):
        self.block = False

    def fire(self,other):
        if self.fireball_ready: #if a fireball is not already flying
            if self.energy.value > (self.energy.max / 4) : #if character has enough energy
                self.setState("fire")
                self.fireBall.shoot(self.pos, self.facing) # fire a fireball
                self.energy.remove(self.energy.max /4) # remove energy

    #stops a fall
    def stop_fall(self):
        self.vel = Vector()
        self.jumping = False

    #adds gravity to velocity
    def fall(self):
        self.vel.add(GRAVITY)

    #sees if character can jump (possibly redundant, could be incorporated into interaction class
    def attemptJump(self):
        if not self.jumping:
            self.jump()

    #makes character jump
    def jump(self):
        self.vel.add(Vector(0, -4))
        self.jumping = True
        self.jumpTime = 0

    def update(self):
        if(self.energycounter % 5 == 0): #increases energy at a steady rate - can be adjusted
            self.energy.add(1)
        self.energycounter+=1
        if not self.punch_ready:
            if self.punch_cooldown == 0:
                self.punch_ready = True
            else:
                self.punch_cooldown-= 1

        if self.jumping and self.jumpTime < 5: #jumptime used to calculate height
            self.setState("jump")
            self.vel.add(Vector(0,-.5))
            self.jumpTime += 1

        #moves self and updates boundaries based on movement
        self.move()
        self.update_boundaries()
        self.stateTimer += 1

    #draw function
    def draw(self, canvas, enemy):
        self.fireBall.update(canvas, enemy)
        self.update()
        self.lifeSprite.update(self.lives.value, canvas)
        #moves sprite
        #self.sprite.setDest(self.pos.getP())
        self.sprite.update(canvas, self.pos.getP())
        #circle used as placeholder marker - to be removed
        self.energy.draw(canvas, self.p_number, 'Blue')
        self.health.draw(canvas, self.p_number, 'Red')

    #setting states for sprite
    def setState(self, state):
        global states
        if self.dead:
            self.sprite.changeState("die")
            self.currentState = "die"
        elif states[self.currentState] == "interruptable" or self.stateTimer > 20:
            self.stateTimer = 0
            self.sprite.changeState(state)
            self.currentState = state


