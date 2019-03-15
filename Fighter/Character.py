from Fighter.Vector import Vector
from Fighter.Resource import Resource
from Fighter.Fireball import Fireball
from Fighter.Spritelives import Spritelives
from Fighter import Rounds

GRAVITY = Vector(0, 0.4)


class Character:
    def __init__(self, sprite, start_position, vel, player_number, facing):
        self.sprite = sprite
        self.startpos = start_position
        self.startvel = vel
        self.newLife()

        self.p_number = player_number
        ##these numbers need balancing
        lifespritex = 350
        if self.p_number == 1:
            lifespritex = 150
        self.lifeSprite = Spritelives((lifespritex, 485), self.lives.value)
        #used in calculations for punches and fireballs
        self.facing = facing

        #used as states
        self.block = False
        self.jumping = False
        self.jumpTime = 0
        self.fireball_ready = True
        self.punch_cooldown = 0
        self.punch_cooldown_max = 30
        self.punch_ready = True

        #creates a fireball object bound to this character
        self.fireBall = Fireball(self, self.facing)

        #sets collision boundaries
        self.head = self.getHead()
        self.feet = self.getFeet()
        self.left_edge = self.getLeftEdge()
        self.right_edge = self.getRightEdge()


    def setLives(self, lives):
        self.lives = Resource(lives, lives)

    #These methods define the bounds of the hurtbox, uses dimensions of sprite, subject to change
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

    #calculates damage when hit, blocking halves the damage
    def hit(self, damage):
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
        self.lives.remove(1)
        Rounds.over()

    def newLife(self):
        self.energy = Resource(0, 100)#TODO
        self.energycounter = 0
        self.health = Resource(100, 100)#TODO
        self.pos = self.startpos
        self.vel = self.startvel

    #checks whether self is hit by other
    def check_hit(self, other):
        xcoord = other.x
        ycoord = other.y
        if self.left_edge <= xcoord:
            if xcoord <= self.right_edge:
                if self.head <= ycoord:
                    if ycoord <= self.feet:
                        #character hit
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
                if self.facing == 'left':
                    #punch left (change distance - currently 5 pixels
                    fist = Vector(self.left_edge - 5, self.pos.getY())
                else:
                    #punch right
                    fist = Vector(self.right_edge + 5, self.pos.getY())
                if other.check_hit(fist):
                    other.hit(10)



    #attack when jumping
    def jump_kick(self, other):
        if(self.facing == 'left'):
            #kick left (currently 10 pixels
            leg = Vector(self.left_edge - 10, self.pos.getY())
        else:
            #kick right
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
        if self.fireball_ready: #if a fireball is not already flying
            if self.energy.value > (self.energy.max / 4) : #if character has enough energy
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
        if self.jumping:
           #print("jumping")
            pass
        else:
            #print("attempted jump")
            self.jump()

    #makes character jump
    def jump(self):
        self.vel.add(Vector(0, -4))
        self.jumping = True
        self.jumpTime = 0

    def update(self):
        if(self.energycounter % 5 == 0):
            self.energy.add(1)
        self.energycounter+=1
        if not self.punch_ready:
            if self.punch_cooldown == 0:
                self.punch_ready = True
            else:
                self.punch_cooldown-= 1



        if self.jumping and self.jumpTime < 5: #jumptime used to calculate height
            self.vel.add(Vector(0,-.6))
            self.jumpTime += 1
        elif not self.jumping and self.jumpTime >= 5: #makes sure there is no y movement if not jumping
            self.vel = Vector(self.vel.getX(), 0)

        #moves self and updates boundaries based on movement
        self.move()
        self.update_boundaries()

    #draw function
    def draw(self, canvas, enemy):
        self.fireBall.update(canvas, enemy)
        self.update()
        #moves sprite
        self.sprite.setDest(self.pos.getP())
        self.sprite.update(canvas)
        #circle used as placeholder marker
        canvas.draw_circle(self.pos.getP(),
                           (self.sprite.spriteDim[0] /2),
                           1,
                           'Blue')
        self.energy.draw(canvas, self.p_number, 'Blue')
        self.health.draw(canvas, self.p_number, 'Red')
        self.lifeSprite.draw(canvas)

        #Pass it character number



