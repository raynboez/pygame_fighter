try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from Fighter.Vector import Vector
from Fighter import Master
from Fighter.Ai import Ai



class Mouse:

    screen = "null"

    def handler(position):
        click = Vector(position[0], position[1])
        if (Mouse.screen=="splash"):#case statements don't exist in python
            Master.menu()
        elif (Mouse.screen=="menu"):
            Mouse.mainMenuButtons(click)
        elif (Mouse.screen=="instructions"):
            Master.menu()
        elif (Mouse.screen=="game"):
            Mouse.gameMenuButtons(click)
        elif (Mouse.screen=="MultOrNo"):
            Mouse.multiplayer(click)

#######define buttons onS-screen buttons below#####

    def mainMenuButtons(click):
        radius = 36
        red = Vector(243, 74)
        yel = Vector(243, 157)
        gre = Vector(243, 240)

        cenToClick = click.copy().subtract(red.copy())  # dist between centre of ball and click
        if (cenToClick.length() <= radius):  # check click is in ball
            quit(0)
        cenToClick = click.copy().subtract(yel.copy())  # dist between centre of ball and click
        if (cenToClick.length() <= radius):  # check click is in ball
            Master.instructions()
        cenToClick = click.copy().subtract(gre.copy())  # dist between centre of ball and click
        if (cenToClick.length() <= radius):  # check click is in ball
            # Master.gameLoop()
            Master.modeSelect()

    def gameMenuButtons(click):
        pass
        #exit to menu
        #pause
        #show instructions

    def multiplayer(click):
        if (click.getX()<250):
            Ai.leve1 = 0
        else:
            Ai.level = 1
        Master.gameLoop('Yellow', 'Red')
