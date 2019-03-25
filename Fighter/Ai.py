from Fighter.Interaction import Interaction
from Fighter.Character import Character
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

class Ai:#More an automaton, a real ai would be too slow

    level = 1
    distance = 300

    def move(self, keyboard):#Runs as soon as opponant moves
        self.distance = Character.distance(Interaction.characters[0], Interaction.characters[1])
        #distance between chars on x axis, positive means cpu is to right of player
        print(self.distance)
        self.levelSelect(self, keyboard)


    def levelSelect(self, keyboard):
         switcher = {
            1: self.testIng(keyboard),
            2: "interruptable",
            3: self.lazyOpo(keyboard),
            4: "interruptable",
            5: "interruptable",
         }
         return switcher.get(self.level, "Invalid level")

###Actions list#########

        # Interaction.keyboard.right[1] = True
        # Interaction.keyboard.left[1] = True #
        # Interaction.keyboard.up[1] = True#jump
        # Interaction.keyboard.down[1] = True#block
        # Interaction.keyboard.attack[1] = True
        # Interaction.keyboard.fire[1] = True

###opponants sorted by difficulty(best to worst)####

    def testIng(keyboard):
        if (keyboard.up[0]):  # need to makes things false again
            keyboard.fire[1] = True
        elif (keyboard.down[0]):
            keyboard.fire[1] = True
        elif (keyboard.attack[0] and keyboard.up[0]):  # flying kick
            keyboard.down[1] = True
        elif (keyboard.attack[0]):
            keyboard.down[1] = True
        elif (keyboard.fire[0]):
            keyboard.up[1] = True
        else:
            keyboard.attack[1] = True

    def fanCFighter(keyboard):#does all the things well
        pass

    def lazyOpo(keyboard):#kills only by shooting no movement
        #difficulty 6.5/10
        if (keyboard.up[0]):#need to makes things false again
            keyboard.fire[1] = True
        elif (keyboard.down[0]):
            keyboard.fire[1] = True
        elif (keyboard.attack[0] and keyboard.up[0]):
            keyboard.down[1] = True

    def jumpyJermain(keyboard):#moves to much
        pass

    def fistyFred(keyboard):#doesn't use ranged attacks
        pass