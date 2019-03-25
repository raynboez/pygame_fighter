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
    distance = -300
    absDistance = abs(distance)#otherwise distance is abs'd in ints
    decider = 5

    def move(self, keyboard):#Runs as soon as opponant moves
        self.distance = Character.distance(Interaction.characters[0], Interaction.characters[1])
        self.absDistance = abs(self.distance)
        self.decider = randint(0,9)
        #distance between chars on x axis, positive means player is to right of cpu
        print(self.distance)
        self.levelSelect(self, keyboard)


    def levelSelect(self, keyboard):
         switcher = {
            1: self.testIng(self, keyboard),
            2: "interruptable",
            3: self.lazyOpo(self, keyboard),
            4: "interruptable",
            5: "interruptable",
         }
         return switcher.get(self.level, "Invalid level")

###Actions list#########

        # keyboard.right[1] = True
        # keyboard.left[1] = True #
        # keyboard.up[1] = True#jump
        # keyboard.down[1] = True#block
        # keyboard.attack[1] = True
        # keyboard.fire[1] = True

###opponants sorted by difficulty(best to worst)####

    def testIng(self, keyboard):#fiesty fred#need to do things when player not moving
        print("test")
        print(self.distance)
        if ((self.absDistance>= 15) and (self.absDistance<=45)):#if in attack range
            keyboard.attack[1] = True
            if (self.decider <4):#attack with jump kick
                keyboard.up[1] = True
        elif self.distance > 45:#to left of player
            keyboard.right[1] = True
            if (self.decider <2):#jump left
                keyboard.up[1] = True
            pass#go left, run or jump
        elif((self.distance < -45)):
            keyboard.left[1] = True
            if (self.decider <1):#jump right
                keyboard.up[1] = True
        #else:
            #pass#go left or right jump and attack
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


    def fanCFighter(self, keyboard):#does all the things well
        pass

    def lazyOpo(self, keyboard):#kills only by shooting no movement
        print("opo")
        #difficulty 6.5/10
        if (keyboard.up[0]):#need to makes things false again
            keyboard.fire[1] = True
        elif (keyboard.down[0]):
            keyboard.fire[1] = True
        elif (keyboard.attack[0] and keyboard.up[0]):
            keyboard.down[1] = True

    def jumpyJermain(self, keyboard):#moves to much
        pass

    def fistyFred(self, keyboard):#doesn't use ranged attacks
        pass