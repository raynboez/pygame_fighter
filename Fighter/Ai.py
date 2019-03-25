from Fighter.Interaction import Interaction
from Fighter.Character import Character
from random import randint
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

class Ai:#More an automaton, a real ai would be too slow
    #ai only works when player is pressing keyboard
    #put keys down at random to make moves?

    level = 1
    opponent = []

    def __init__(self, keyboard):
        self.keyboard = keyboard
        Ai.opponent = [self.testIng, self.jumpyJermain, self.lazyOpo,
                self.fanCFighter]#todo change testing to fisty, also runs this won init

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

    def testIng(self):#fiesty fred#need to do things when player not moving
        print("test")
        print(self.distance)
        if ((self.absDistance>= 15) and (self.absDistance<=45)):#if in attack range
            self.keyboard.attack[1] = True
            if (self.decider <4):#attack with jump kick
                self.keyboard.up[1] = True
        elif self.distance > 45:#to left of player
            self.keyboard.right[1] = True
            if (self.decider <2):#jump left
                self.keyboard.up[1] = True
            pass#go left, run or jump
        elif((self.distance < -45)):
            self.keyboard.left[1] = True
            if (self.decider <1):#jump right
                self.keyboard.up[1] = True
        else:
            if (self.decider < 4):  # jump left
                self.keyboard.left[1] = True
            else:
                self.keyboard.right[1] = True
            self.keyboard.up[1] = (self.decider % 3)==0


    def fanCFighter(self):#does all the things well
        print("fanc")

    def lazyOpo(self):#kills only by shooting no movement
        print("opo")
        #difficulty 6.5/10
        if (self.keyboard.up[0]):#need to makes things false again
            self.keyboard.fire[1] = True
        elif (self.keyboard.down[0]):
            self.keyboard.fire[1] = True
        elif (self.keyboard.attack[0] and self.keyboard.up[0]):
            self.keyboard.down[1] = True

    def jumpyJermain(self):#moves to much
        print("jermain")
    # if (keyboard.up[0]):  # need to makes things false again
    #     keyboard.fire[1] = True
    # elif (keyboard.down[0]):
    #     keyboard.fire[1] = True
    # elif (keyboard.attack[0] and keyboard.up[0]):  # flying kick
    #     keyboard.down[1] = True
    # elif (keyboard.attack[0]):
    #     keyboard.down[1] = True
    # elif (keyboard.fire[0]):
    #     keyboard.up[1] = True
    # else:
    #     keyboard.attack[1] = True

    def fistyFred(self):#doesn't use ranged attacks
        print("fred")