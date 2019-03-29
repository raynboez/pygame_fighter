from Fighter.Interaction import Interaction
from Fighter.Character import Character
from random import random, randint

class Ai:#More an automaton, a real ai would be too slow
    #ai only works when player is pressing keyboard
    #put keys down at random to make moves?

    level = 1
    opponent = []
    aiCharNum = 1#same as keyboard number
    playerCharNum = 0

    def __init__(self, keyboard):
        self.keyboard = keyboard
        self.punchRange = (15, 45)
        self.loopsPerGo = 5  # when cur frame mod this = 0 then the ai plays, controls ai speed
        Ai.opponent = [self.lazyOpo, self.fistyFred, self.jumpyJermain,
                self.fanCFighter]#Order here deturmines level

    def move(self):
        self.distance = Character.distance(Interaction.characters[Ai.playerCharNum], Interaction.characters[Ai.aiCharNum])
        # distance between chars on x axis, positive means player is to right of cpu
        self.absDistance = abs(self.distance)
        self.opponent[self.level-1]()

###opponants sorted by difficulty(best to worst)####

    def fanCFighter(self):#does all the things well
        if self.beingFireballed():# avoids being hit umless impossible not-to
            self.fireballHandler()
        elif self.attackInRange():  # if in attack range
            self.attackHandler()
        elif self.beingJumpKicked():
            self.jumpKickHandler()
        elif self.storkOrShoot():
            self.storkOrShootHandler()
        else:#if player too close to punch
            self.tooCloseToHitHandler()

    def jumpyJermain(self):#jumps too much
        if self.beingFireballed():
            self.jump()
        elif self.attackInRange():
            self.attackHandler(140)
        elif self.beingJumpKicked():
            self.jumpKickHandler(130, 0)
        elif self.storkOrShoot():#if not close enought to punch
            self.storkOrShootHandler(50,120)
        else:#if player too close to punch
            self.tooCloseToHitHandler(300)

    def fistyFred(self):#doesn't use fireballs
        if self.attackInRange(-10, -5):#gets closer than needs to and tries attacking too close
            self.attackHandler(80)
        else:
            self.followPlayerHandler(80)

    def lazyOpo(self):#kills only by shooting no movement
        if self.attackInRange(0, -10):#doesn't reach far to attack
            self.attackHandler(0)
        elif (self.beingFireballed() or self.beingJumpKicked()):
            self.defend()
        else:
            self.fireball()

################################# Moves #######################################
    
    def attack(self):
        self.keyboard.attack[Ai.aiCharNum] = True
    
    def defend(self):
        self.keyboard.down[Ai.aiCharNum] = True
        
    def fireball(self):
        self.keyboard.fire[Ai.aiCharNum] = True
        
    def jump(self):
        self.keyboard.up[Ai.aiCharNum] = True
        
    def moveLeft(self):
        self.keyboard.left[Ai.aiCharNum] = True
        
    def moveRight(self):
        self.keyboard.right[Ai.aiCharNum] = True

########## Move testers(decided if an action should be done or not) ###########

    def attackInRange(self, minMod=0, maxMod=0):
        inRange = (self.absDistance >= self.punchRange[0] + minMod) and (
                    self.absDistance <= self.punchRange[1] + maxMod)
        return inRange

    def beingFireballed(self):
        return self.keyboard.fire[Ai.playerCharNum]

    def beingJumpKicked(self):
        return (self.keyboard.attack[Ai.playerCharNum] and self.keyboard.up[Ai.playerCharNum])  # attacked with jump kick

    def storkOrShoot(self):
        return self.absDistance > self.punchRange[1]  # Too far away to attack with a punch


########## Moves series (carry out moves for events based on chance) ###########

    def attackHandler(self, jumPer = 50):
        self.attack()
        if self.movePercent(jumPer):
            self.jump()

    def jumpKickHandler(self, range=130, counterAtt = 50):
        if self.absDistance < range:  # in range
            if self.moveChance(counterAtt):
                self.jump()
                self.attack()
            else:
                self.defend()
        else:
            self.fireball()

    def followPlayerHandler(self, jumPer = 0):
        if self.distance > 0:  # to left of player
            self.moveRight()
        else:
            self.moveLeft()
        if self.movePercent(jumPer):
            self.jump()

    def storkOrShootHandler(self, firePer=50, jumpPer=70):
            self.followPlayerHandler(jumpPer)
            if self.movePercent(firePer):
                self.fireball()

    def fireballHandler(self, attackInRChance = 40):
        tooCloseToDodge = 60
        if(self.absDistance < tooCloseToDodge):  # can't dodge
            if (self.moveChance(attackInRChance)):  # instantanious so jump percent not used
                self.attack()
                self.followPlayerHandler(100)
            else:
                self.fireball()
                if self.moveChance(30):
                    self.jump()
        else:
            self.fireballDodgeHandler()

    def fireballDodgeHandler(self):
        distaceToLand = 280
        if (self.absDistance > distaceToLand):  #moving jump required to dodge
            self.followPlayerHandler()
        self.jump()

    def tooCloseToHitHandler(self, jumPer = 80):
        if self.movePercent():
            self.moveRight()
        else:
            self.moveLeft()
        if self.movePercent(jumPer):
            self.jump()
            self.attack()

    ########## Randoms, (introduce randomness into choosen move ##########

    def movePercent(self, percent = 100):#use for events like tracking player not in reaction to player moves
        #percent chance of doing a move if trying for 1 second
        chanceToGo = percent/(60/self.loopsPerGo)#jumps are about 36 frames with gravity =0.4
        return chanceToGo > (random() *100)

    def moveChance(self, percent = 50):#chance of an event happening instantaniously
        return percent > randint(0, 101)

