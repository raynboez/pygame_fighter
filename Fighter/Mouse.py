#from Fighter import MultiplayerOrNo
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from Fighter.Vector import Vector
from Fighter import Master
from Fighter.Ai import Ai

class Mouse:

    screen = "null"
    multiNoSel = False
    levelSel = False

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
        elif Mouse.screen=="lvlSelect":
            Mouse.lvlSelect(click)
        else:
            pass

#######define buttons onS-screen buttons below#####

    def mainMenuButtons(click):
        radius = 36
        red = Vector(246, 74)
        yel = Vector(246, 157)
        gre = Vector(246, 240)

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
        #Red, yel and green correspond to the position of the buttons displayed during the game
            radius = 20
            red = Vector(30, 40)
            yel = Vector(80, 40)
            gre = Vector(130, 40)

            cenToClick = click.copy().subtract(red.copy())  # dist between centre of ball and click
            if (cenToClick.length() <= radius):  # check click is in ball
                quit(0)
            cenToClick = click.copy().subtract(yel.copy())  # dist between centre of ball and click
            if (cenToClick.length() <= radius):  # check click is in ball
                Master.instructions()
            cenToClick = click.copy().subtract(gre.copy())  # dist between centre of ball and click
            if (cenToClick.length() <= radius):  # check click is in ball
                # Master.gameLoop()
                Master.menu()  # todo change colors based on selection
        #exit to menu
        #pause
        #show instructions

    def multiplayer(click):
        multi = Vector(150, 235)
        solo = Vector(350, 235)
        if ((abs(click.getY()-235)) < 85):
            if abs(click.getX()-(multi.copy().getX())) < 60:
                Ai.level = 0
            elif abs(click.getX()-(solo.copy().getX())) < 60:
                Ai.level = 1
            Mouse.multiNoSel = True

    def lvlSelect(click):
        lvl1 = Vector(100, 235)
        lvl2 = Vector(200, 235)
        lvl3 = Vector(300, 235)
        lvl4 = Vector(400, 235)
        if ((abs(click.getY() - 235)) < 85):
            if abs(click.getX() - (lvl1.copy().getX())) < 50:
                Ai.level = 1
            elif abs(click.getX() - (lvl2.copy().getX())) < 50:
                Ai.level = 2
            elif abs(click.getX() - (lvl3.copy().getX())) < 50:
                Ai.level = 3
            elif abs(click.getX() - (lvl4.copy().getX())) < 50:
                Ai.level = 4
            Mouse.levelSel = True