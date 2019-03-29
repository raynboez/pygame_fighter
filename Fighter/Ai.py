from Fighter.Interaction import Interaction
from Fighter.Character import Character
from random import random, randint

class Ai:#More an automaton, a real ai would be too slow
    #ai only works when player is pressing keyboard
    #put keys down at random to make moves?

    level = 1
    opponent = []

    def __init__(self, keyboard):
        self.keyboard = keyboard
        self.punchRange = (15, 45)
        self.loopsPerGo = 5  # when cur frame mod this = 0 then the ai plays, controls ai speed
        Ai.opponent = [self.lazyOpo, self.fistyFred, self.jumpyJermain,
                self.fanCFighter]#Order here deturmines level

    def move(self):
        self.distance = Character.distance(Interaction.characters[0], Interaction.characters[1])
        # distance between chars on x axis, positive means player is to right of cpu
        self.absDistance = abs(self.distance)
        self.opponent[self.level-1]()


###Actions list#########

        # keyboard.right[1] = True
        # keyboard.left[1] = True #
        # keyboard.up[1] = True#jump # jumps take ~ 36 frames
        # keyboard.down[1] = True#block
        # keyboard.attack[1] = True
        # keyboard.fire[1] = True

###opponants sorted by difficulty(best to worst)####

    def fanCFighter(self):#does all the things well
        if (self.keyboard.fire[0]):# avoids being hit umless impossible not-to
            if (self.absDistance < 60):#can't dodge
                if (self.moveChance(40)):  #instantanious so jump percent not used
                    self.keyboard.attack[1] = True
                    self.keyboard.up[1] = True
                    self.keyboard.left[1] = (self.distance > 0)
                    self.keyboard.right[1] = not self.keyboard.left[1]#else jump kick
                else:
                    self.keyboard.fire[1] = True
                    self.keyboard.up[1] = self.moveChance(30)
            else:
                self.dodgeFireball()
        elif self.attackInRange():  # if in attack range
            self.keyboard.attack[1] = True
            if self.movePercent(50):
                self.keyboard.up[1] = True
        elif (self.keyboard.attack[0] and self.keyboard.up[0]):# attacked with jump kick
            if self.absDistance < 130:#in range
                if self.movePercent(70):
                    self.keyboard.up[1] = True
                    self.keyboard.attack[1] = True
                else:
                    self.keyboard.down[1] = True
            else:
                self.keyboard.fire[1] = True
        elif self.storkOrShoot():
            pass
        else:#if player too close to punch
            self.tooCloseToHit()

    def jumpyJermain(self):#jumps too much
        if (self.keyboard.fire[0]):
            self.keyboard.up[1] = True
        elif self.attackInRange():
            self.keyboard.attack[1] = True
            if self.movePercent():  # attack with jump kick
                self.keyboard.up[1] = True
        elif (self.keyboard.attack[0] and self.keyboard.up[0]):
            self.keyboard.down[1] = True
        elif self.storkOrShoot(50,120):#if not close enought to punch
            pass
        else:#if player too close to punch
            self.tooCloseToHit(300)

    def fistyFred(self):#doesn't use fireballs
        if self.attackInRange(-10, -5):#gets closer than needs to and tries attacking too close
            self.keyboard.attack[1] = True
            if self.movePercent(140):  # attack with jump kick
                self.keyboard.up[1] = True
        else:
            self.goTowardsPlayer()
            if self.movePercent(80):  # jump right
                self.keyboard.up[1] = True

    def lazyOpo(self):#kills only by shooting no movement
        if self.attackInRange(0, -10):#doesn't reach far to attack
            self.keyboard.attack[1] = True
        elif self.keyboard.fire[0] or (self.keyboard.attack[0] and self.keyboard.up[0]):
            self.keyboard.down[1] = True#defend
        else:
            self.keyboard.fire[1] = True

########## Moves / move testers ###########

    def goTowardsPlayer(self):
        if self.distance > 0:  # to left of player
            self.keyboard.right[1] = True
        else:
            self.keyboard.left[1] = True

    def dodgeFireball(self):
        if (self.absDistance > 280):  #moving jump required to dodge
            self.keyboard.left[1] = (self.distance > 0)
            self.keyboard.right[1] = not self.keyboard.left[1]
        self.keyboard.up[1] = True

    def storkOrShoot(self, firePer = 50, jumpPer  = 70):
        if self.absDistance > self.punchRange[1]:  # Too far away to attack with a punch
            self.goTowardsPlayer()
            self.keyboard.fire[1] = self.movePercent(firePer)
            if self.movePercent(jumpPer):
                self.keyboard.up[1] = True
            return True
        return False

    def tooCloseToHit(self, jumPer = 80):
        self.keyboard.left[1] = self.movePercent()
        self.keyboard.right[1] = not self.keyboard.left[1]
        if self.movePercent(jumPer):
            self.keyboard.up[1] = True
            self.keyboard.attack[1] = True

    def attackInRange(self, minMod=0, maxMod=0):
        inRange = (self.absDistance >= self.punchRange[0] + minMod) and (self.absDistance <= self.punchRange[1]+ maxMod)
        return inRange

    def movePercent(self, percent = 100):#use for events like tracking player not in reaction to player moves
        #percent chance of doing a move if trying for 1 second
        chanceToGo = percent/(60/self.loopsPerGo)#jumps are about 36 frames with gravity =0.4
        return chanceToGo > (random() *100)

    def moveChance(self, percent = 50):#chance of an event happening instantaniously
        return percent > randint(0, 101)

