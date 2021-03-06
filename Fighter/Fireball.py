from Fighter.Sprite import Sprite
from Fighter.Vector import Vector

sprites = {
    "Red": "https://i.ibb.co/fFDh4Fq/full-fireball-red.png",
    "Green": "https://i.ibb.co/3pY8Bwh/full-fireball-green.png",
    "Blue": "https://i.ibb.co/8c3T7t5/full-fireball-blue.png",
    "Yellow": "https://i.ibb.co/sFMx6rF/full-fireball-yellow.png",
    "Base" : "https://i.ibb.co/gWrSnR7/full-fireball-base.png"
}


class Fireball:
    #initialises fireball with a player and a direction
    #if fireball is not being fired, it is stored off canvas (-100,-100)


    def __init__(self, player, direction):
        self.character = player
        self.stoppedPos = Vector(-100, -100) #off canvas
        self.pos = self.stoppedPos
        self.direction = direction
        #self.sprite = self.set_sprite() # gets correct sprite
        self.vel = Vector()
        self.sprite = self.set_sprite("Red")

    #sets velocity depending on direction
    def setvel(self, direction, x=0):
        if direction == 'left':
            vel = Vector(-x, self.vel.getY())
        else:
            vel = Vector(x, self.vel.getY())
        return vel

    #moves fireball
    def move(self):
        self.pos = self.pos + self.vel

    #fires a fireball from a position
    def shoot(self, starting, direction):
        self.pos = starting
        self.direction = direction
        self.vel = self.setvel(self.direction, 10)
        self.character.fireball_ready = False

    #stops fireball once a limit is reached
    def stop(self):
        self.pos = self.stoppedPos
        self.vel = Vector()
        self.character.fireball_ready = True

    #sets fireball sprite
    def set_sprite(self, colour):
        self.sprite = Sprite(sprites[colour], 2, 4, self.pos, 1, "fireball", self.direction)

    def setFacing(self, facing):
        self.direction = facing
        self.sprite.setFacing(self.direction)
        self.sprite.updateDirection()


    #draws the sprite on the canvas
    def draw(self, canvas):
        self.sprite.update(canvas, self.pos.getP())

    #looping method
    def update(self, canvas, enemy):
        self.draw(canvas)
        self.move()

        #bounds for stopping fireball
        if enemy.check_hit(self.pos):
            enemy.hit(15)
            self.stop()
        if self.off_screen():
            self.stop()

    #boundary for screen
    def off_screen(self):
        return self.pos.x < 0 or self.pos.x > 500