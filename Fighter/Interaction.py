from Fighter.Vector import Vector


class Interaction:
    def __init__(self, keyboard):
        self.characters = []
        self.platforms = []
        self.walls = []
        self.keyboard = keyboard

    #add a character to the interaction class
    def addCharacter(self, character):
        self.characters.append(character)

    #add a platform to the interaction class
    def addPlatform(self, platform):
        self.platforms.append(platform)

    def addWall(self,wall):
        self.walls.append(wall)

    #process keyboard input and translate into character movement
    def movements(self,character, other, bool):
        if not self.keyboard.down[bool]:
            character.not_blocking()
            if self.keyboard.left[bool] and not character.jumping:
                character.vel = Vector(-1, character.vel.getY())
            if self.keyboard.right[bool] and not character.jumping:
                character.vel = Vector(1, character.vel.getY())
            if self.keyboard.up[bool] and not character.jumping:
                character.attemptJump()
            if self.keyboard.attack[bool]:
                character.punch(other)
            if self.keyboard.fire[bool] and not character.jumping:
                character.fire(other)
        if self.keyboard.down[bool] and not character.jumping:
            character.blocking()
        character.move()
        character.setfacing(other)



    def update(self):
        self.movements(self.characters[0], self.characters[1], 0)
        self.movements(self.characters[1], self.characters[0], 1)
        for wall in self.walls:
            for character in self.characters:
                if wall.touch(character) == 'right':
                    character.pos = Vector(wall.lEdge - (character.sprite.spriteDim[0] / 2), character.pos.getY())
                elif wall.touch(character) == 'left':
                    character.pos = Vector(wall.rEdge + (character.sprite.spriteDim[0] / 2), character.pos.getY())
                else:
                    pass
        for platform in self.platforms:
            for character in self.characters:
                if platform.touch(character):
                    character.stop_fall()
                else:
                    character.fall()



