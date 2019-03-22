try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from Fighter import GameLoop
from Fighter.Frame import Frame

#frame used throughout Game
masterframe = Frame("Name", 500, 500)

def runGame():
    #menu()
    gameLoop()

#adjust these classes when menu and spriteselect are created - can be used to hand over selections
def menu():
    #MainMenu.init()
    pass
def spriteSelect():
    #SpriteSelect.init()
    pass

def gameLoop():
    GameLoop.init("Green", "Yellow")