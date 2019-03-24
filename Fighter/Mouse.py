try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from Fighter.Vector import Vector
from Fighter import Master

class Mouse:

    screen = "null"

    def mainMenuButtons(click):
        radius = 36
        red = Vector(243, 74)
        yel = Vector(243, 157)
        gre = Vector(243, 240)

        cenToClick = click.copy().subtract(red)  # dist between centre of ball and click
        if (cenToClick.length() <= radius):  # check click is in ball
            pygame.quit()
            # pass
            # todo exit
        cenToClick = click.copy().subtract(yel)  # dist between centre of ball and click
        if (cenToClick.length() <= radius):  # check click is in ball
            Master.instructions()
        cenToClick = click.copy().subtract(gre)  # dist between centre of ball and click
        if (cenToClick.length() <= radius):  # check click is in ball
            # Master.gameLoop()
            Master.gameLoop('Yellow', 'Red')#todo change colors based on selection

    def handler(position):
        click = Vector(position[0], position[1])
        Mouse.mainMenuButtons(click)