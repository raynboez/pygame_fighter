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

    def move(self):
        self.distance = Character.distance(Interaction.characters[0], Interaction.characters[1])
        # distance between chars on x axis, positive means player is to right of cpu
        self.absDistance = abs(self.distance)
        self.decider = randint(0,9)
        self.punchRange = (15, 45)#min(15) max(45) can be adjusted so opponant punches ineffectivly
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
        elif self.attackInRange():  # if in attack range
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
        elif self.AbsDistance > self.punchRange[1]:  # to left of player
            self.goTowardsPlayer()
            self.keyboard.fire[1] = (self.decider % 4) == 0
            if self.decider < 1:  # jump right
                self.keyboard.up[1] = True
        else:
            if self.decider < 7:  # jump left
                self.keyboard.left[1] = True
            else:
                self.keyboard.right[1] = True
            self.keyboard.up[1] = (self.decider % 3) == 0

    def jumpyJermain(self):#jumps too much
        if (self.keyboard.fire[0]):
            self.keyboard.up[1] = True
        elif self.attackInRange():
            self.keyboard.attack[1] = True
            if (self.decider < 4):  # attack with jump kick
                self.keyboard.up[1] = True
        elif (self.keyboard.attack[0] and self.keyboard.up[0]):
            self.keyboard.down[1] = True
        elif self.AbsDistance > 45:  # if player is far away outside of punch range
            self.goTowardsPlayer()
            self.keyboard.fire[1] = (self.decider % 4) == 0
            if (self.decider < 1):  # jump towards
                self.keyboard.up[1] = True
        else:
            if (self.decider < 4):  # jump left
                self.keyboard.left[1] = True
            else:
                self.keyboard.right[1] = True
            self.keyboard.up[1] = (self.decider % 3) == 0

    def fistyFred(self):#doesn't use fireballs
        if self.attackInRange(-10, -5):#gets closer than needs to and tries attacking too close
            self.keyboard.attack[1] = True
            if (self.decider < 4):  # attack with jump kick
                self.keyboard.up[1] = True
        else:
            self.goTowardsPlayer()
            if (self.decider < 1):  # jump right
                self.keyboard.up[1] = True

    def lazyOpo(self):#kills only by shooting no movement
        if self.attackInRange():
            self.keyboard.attack[1] = True
        elif self.keyboard.fire[0]:
            self.keyboard.down[1] = True
        elif (self.keyboard.up[0]):
            self.keyboard.fire[1] = True
        elif (self.keyboard.down[0]):
            self.keyboard.fire[1] = True
        elif (self.keyboard.attack[0] and self.keyboard.up[0]):
            self.keyboard.down[1] = True
        else:
            self.keyboard.fire[1] = True

    def attackInRange(self, minMod=0, maxMod=0):
        inRange = (self.absDistance >= self.punchRange[0] + minMod) and (self.absDistance <= self.punchRange[1]+ maxMod)
        return inRange

    def goTowardsPlayer(self):
        if self.distance > 0:  # to left of player
            self.keyboard.right[1] = True
        else:
            self.keyboard.left[1] = True