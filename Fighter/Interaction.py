from Fighter.Vector import Vector


class Interaction:
    def __init__(self, keyboard):
        self.characters = []
        self.platforms = []
        self.keyboard = keyboard

    def addCharacter(self, character):
        self.characters.append(character)

    def addPlatform(self, platform):
        self.platforms.append(platform)

    def movements(self,character, other):
        if self.keyboard.down:
            character.not_blocking()
            if self.keyboard.left:
                character.vel = Vector(-1, character.vel.getY())
            if self.keyboard.right:
                character.vel = Vector(1, character.vel.getY())
            if self.keyboard.up and not character.jumping:
                character.vel = Vector(character.vel.getX(), -10)
            if self.keyboard.attack:
                character.punch(other)
            if self.keyboard.fire and not character.jumping:
                character.fire()
        if self.keyboard.down and not character.jumping:
            character.blocking()

    def update(self):
        self.movements(self.characters[0], self.characters[1])
        self.movements(self.characters[1], self.characters[0])
        for platform in self.platforms:
            for character in self.characters:
                if platform.touch(character):
                    character.stop_fall()
                    character.jumping = False
                else:
                    character.jumping = True



