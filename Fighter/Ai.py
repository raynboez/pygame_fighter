from Fighter.Interaction import Interaction
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

class Ai:#More an automaton, a real ai would be too slow

    leve1 = 1

    def move(keyboard):#Runs as soon as opponant moves
        Ai.lazyOpo(keyboard)

        #
        # if (keyboard.up[0]):#need to makes things false again
        #     keyboard.fire[1] = True
        # elif (keyboard.down[0]):
        #     keyboard.fire[1] = True
        # elif (keyboard.attack[0] and keyboard.up[0]):#flying kick
        #     keyboard.down[1] = True
        # elif (keyboard.attack[0]):
        #     keyboard.down[1] = True
        # elif (keyboard.fire[0]):
        #     keyboard.up[1] = True
        # else:
        #     keyboard.attack[1]= True

        # Interaction.keyboard.right[1] = True
        # Interaction.keyboard.left[1] = True #
        #
        # Interaction.keyboard.up[1] = True#jump
        #
        # Interaction.keyboard.down[1] = True#block
        # Interaction.keyboard.attack[1] = True
        #
        # Interaction.keyboard.fire[1] = True

###opponants sorted by difficulty(best to worst)####

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