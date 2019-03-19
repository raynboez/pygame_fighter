try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from Fighter import GameLoop
from Fighter.Frame import Frame

masterframe = Frame("Name", 500, 500)

def runGame():

    #menu()
    #SpriteSelect()
    gameLoop()


def menu():
    #MainMenu.init()
    pass
def spriteSelect():
    #SpriteSelect.init()
    pass

def gameLoop():
    GameLoop.init()