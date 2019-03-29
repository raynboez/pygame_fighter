from Fighter.Vector import Vector
from Fighter import Master
from Fighter.Ai import Ai

class Mouse:

    screen = "null"
    multiNoSel = False
    levelSel = False
    spriteSel1 = False
    spriteSel2 = False
    spriteSelection = [0,0]

    def handler(position):
        click = Vector(position[0], position[1])
        if Mouse.screen=="splash":#todo change to dict
            Master.menu()
        elif Mouse.screen=="menu":
            Mouse.mainMenuButtons(click)
        elif Mouse.screen=="instructions":
            Master.menu()
        elif Mouse.screen=="game":
            Mouse.gameMenuButtons(click)
        elif Mouse.screen=="MultOrNo":
            Mouse.multiplayer(click)
        elif Mouse.screen=="lvlSelect":
            Mouse.lvlSelect(click)
        elif Mouse.screen=="spriteSelect":
            Mouse.spriSel(click)
        else:
            pass

#######define on-screen buttons below#####

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
                Master.menu()
        #exit to menu
        #pause
        #show instructions

    def multiplayer(click):
        centerY = 235
        buttonWidth = 120
        multi = Vector(150, centerY)
        solo = Vector(350, centerY)
        if ((abs(click.getY()-centerY)) < 85):
            if abs(click.getX()-(multi.copy().getX())) < buttonWidth/2:
                Ai.level = 0
                Mouse.multiNoSel = True
            elif abs(click.getX()-(solo.copy().getX())) < buttonWidth/2:
                Ai.level = 1
                Mouse.multiNoSel = True

    def lvlSelect(click):
        spriteWidth = 100
        spriteHeight = 170
        centerY = 235
        lvl1 = Vector(1 * spriteWidth, centerY)
        lvl2 = Vector(2 * spriteWidth, centerY)
        lvl3 = Vector(3 * spriteWidth, centerY)
        lvl4 = Vector(4 * spriteWidth, centerY)
        if ((abs(click.getY() - centerY)) < spriteHeight/2):
            if abs(click.getX() - (lvl1.copy().getX())) < spriteWidth/2:
                Ai.level = 1
                Mouse.levelSel = True
            elif abs(click.getX() - (lvl2.copy().getX())) < spriteWidth/2:
                Ai.level = 2
                Mouse.levelSel = True
            elif abs(click.getX() - (lvl3.copy().getX())) < spriteWidth/2:
                Ai.level = 3
                Mouse.levelSel = True
            elif abs(click.getX() - (lvl4.copy().getX())) < spriteWidth/2:
                Ai.level = 4
                Mouse.levelSel = True

    def spriSel(click):
        rows = (180, 260)
        columns = (187.5, 312.5)
        red = Vector(columns[0], rows[0])
        green = Vector(columns[1], rows[0])
        blue = Vector(columns[0], rows[1])
        yell = Vector(columns[1], rows[1])
        imgWidth = 125
        imgHeight = 160
        if (abs(click.getY() - rows[0])) < imgHeight/2:
            if abs(click.getX() - (red.copy().getX())) < imgWidth/2:
                Mouse.spriteSel2 = Mouse.spriteSel1
                Mouse.spriteSel1 = True
                Mouse.spriteSelection = [0,0]
            elif abs(click.getX() - (green.copy().getX())) < imgWidth/2:
                Mouse.spriteSel2 = Mouse.spriteSel1
                Mouse.spriteSel1 = True
                Mouse.spriteSelection = [1, 0]
        elif(abs(click.getY() - rows[1])) < imgHeight/2:
            if abs(click.getX() - (blue.copy().getX())) < imgWidth/2:
                Mouse.spriteSel2 = Mouse.spriteSel1
                Mouse.spriteSel1 = True
                Mouse.spriteSelection = [0, 1]
            elif abs(click.getX() - (yell.copy().getX())) < imgWidth/2:
                Mouse.spriteSel2 = Mouse.spriteSel1
                Mouse.spriteSel1 = True
                Mouse.spriteSelection = [1, 1]
