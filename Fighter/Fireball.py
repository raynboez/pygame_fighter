from Fighter.Sprite import Sprite
from Fighter.Vector import Vector
class Fireball:
    #initialises fireball with a player and a direction
    #if fireball is not being fired, it is stored off canvas

    def __init__(self, player, direction):
        self.character = player
        self.stoppedPos = Vector(-100, -100) #off canvas
        self.pos = self.stoppedPos
        self.direction = direction
        self.sprite = self.set_sprite() # gets correct sprite
        self.vel = Vector()

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
        self.vel = self.setvel(direction, 10)
        self.character.fireball_ready = False

    #stops fireball once a limit is reached
    def stop(self):
        self.pos = self.stoppedPos
        self.vel = Vector()
        self.character.fireball_ready = True

    #sets fireball sprite
    def set_sprite(self):
        if self.character.p_number == '1':
            img = Sprite(".\\Sprites\\PlaceHolder.png", 180, 350, 7, 6, (400, 300), 1)
        else:
            img = Sprite(".\\Sprites\\PlaceHolder.png", 180, 350, 7, 6, (400, 300), 1)
        return img

    #draws the sprite on the canvas
    def draw(self, canvas):
        #self.sprite.update(canvas)
        #currently we have no sprite for this, circle used as placeholder
        #simple spritesheet needed, 4 frames to cycle through
        canvas.draw_circle(
                            self.pos.getP(),
                            10,
                            1,
                            'Red'
        )

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