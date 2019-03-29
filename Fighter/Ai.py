from Fighter.Interaction import Interaction
from Fighter.Character import Character
from random import randint

class Ai:#More an automaton, a real ai would be too slow
    #ai only works when player is pressing keyboard
    #put keys down at random to make moves?

    level = 1
    opponent = []

    def __init__(self, keyboard):
        self.keyboard = keyboard
        Ai.opponent = [self.lazyOpo, self.fistyFred, self.jumpyJermain,
                self.fanCFighter]#Order here deturmines level

    def move(self):#Runs as soon as opponant moves
        self.distance = Character.distance(Interaction.characters[0], Interaction.characters[1])
        # distance between chars on x axis, positive means player is to right of cpu
        self.absDistance = abs(self.distance)
        self.decider = randint(0,9)
        self.opponent[self.level-1]()


###Actions list#########

        # keyboard.right[1] = True
        # keyboard.left[1] = True #
        # keyboard.up[1] = True#jump
        # keyboard.down[1] = True#block
        # keyboard.attack[1] = True
        # keyboard.fire[1] = True

###opponants sorted by difficulty(best to worst)####

    def fanCFighter(self):#does all the things well
        if (self.keyboard.fire[0]):# avoids being hit umless impossible not-to
            if (self.absDistance < 60):#can't dodge
                if (self.decider < 4):  #jump kick
                    self.keyboard.attack[1] = True
                    self.keyboard.up[1] = True
                    self.keyboard.left[1] = (self.distance > 0)
                    self.keyboard.right[1] = not self.keyboard.left[1]#else jump kick
                else:
                    self.keyboard.fire[1] = True
                self.keyboard.up[1] = (self.decider % 3) == 0
            elif (self.absDistance > 280):#jump forward to dodge
                self.keyboard.up[1] = True
                self.keyboard.left[1] = (self.distance > 0)
                self.keyboard.right[1] = not self.keyboard.left[1]
            else:#jumping will dodge fine
                self.keyboard.up[1] = True
        elif ((self.absDistance >= 15) and (self.absDistance <= 45)):  # if in attack range
            self.keyboard.attack[1] = True
            if (self.decider < 2):  # attack with jump kick
                self.keyboard.up[1] = True
        elif (self.keyboard.attack[0] and self.keyboard.up[0]):# attacked with jump kick
            if self.absDistance < 130:#in range
                if (self.decider < 2):
                    self.keyboard.up[1] = True
                    self.keyboard.attack[1] = True
                else:
                    self.keyboard.down[1] = True
            else:
                self.keyboard.fire[1] = True
        elif self.distance > 45:  # to left of player
            self.keyboard.right[1] = True
            self.keyboard.fire[1] = (self.decider % 4) == 0
            if (self.decider < 1):  # jump left
                self.keyboard.up[1] = True
        elif ((self.distance < -45)):
            self.keyboard.left[1] = True
            self.keyboard.fire[1] = (self.decider % 4) == 0
            if (self.decider < 1):  # jump right
                self.keyboard.up[1] = True
        else:
            if (self.decider < 7):  # jump left
                self.keyboard.left[1] = True
            else:
                self.keyboard.right[1] = True
            self.keyboard.up[1] = (self.decider % 3) == 0

    def jumpyJermain(self):#moves to much
        if (self.keyboard.fire[0]):
            self.keyboard.up[1] = True
        elif ((self.absDistance >= 15) and (self.absDistance <= 45)):  # if in attack range
            self.keyboard.attack[1] = True
            if (self.decider < 4):  # attack with jump kick
                self.keyboard.up[1] = True
        elif (self.keyboard.attack[0] and self.keyboard.up[0]):
            self.keyboard.down[1] = True
        elif self.distance > 45:  # to left of player
            self.keyboard.right[1] = True
            self.keyboard.fire[1] = (self.decider % 4) == 0
            if (self.decider < 2):  # jump left
                self.keyboard.up[1] = True
        elif ((self.distance < -45)):
            self.keyboard.left[1] = True
            self.keyboard.fire[1] = (self.decider % 4) == 0
            if (self.decider < 1):  # jump right
                self.keyboard.up[1] = True
        else:
            if (self.decider < 4):  # jump left
                self.keyboard.left[1] = True
            else:
                self.keyboard.right[1] = True
            self.keyboard.up[1] = (self.decider % 3) == 0

    def fistyFred(self):#doesn't use ranged attacks
        if ((self.absDistance >= 15) and (self.absDistance <= 45)):  # if in attack range
            self.keyboard.attack[1] = True
            if (self.decider < 4):  # attack with jump kick
                self.keyboard.up[1] = True
        elif self.distance > 45:  # to left of player
            self.keyboard.right[1] = True
            if (self.decider < 2):  # jump left
                self.keyboard.up[1] = True
        elif ((self.distance < -45)):
            self.keyboard.left[1] = True
            if (self.decider < 1):  # jump right
                self.keyboard.up[1] = True
        else:
            if (self.decider < 4):  # jump left
                self.keyboard.left[1] = True
            else:
                self.keyboard.right[1] = True
            self.keyboard.up[1] = (self.decider % 3) == 0

    def lazyOpo(self):#kills only by shooting no movement
        if ((self.absDistance >= 15) and (self.absDistance <= 45)):  # if in attack range
            self.keyboard.attack[1] = True
        elif (self.keyboard.up[0]):#need to makes things false again
            self.keyboard.fire[1] = True
        elif (self.keyboard.down[0]):
            self.keyboard.fire[1] = True
        elif (self.keyboard.attack[0] and self.keyboard.up[0]):
            self.keyboard.down[1] = True
        else:
            self.keyboard.fire[1] = True