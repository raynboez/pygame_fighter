try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from Fighter import GameLoop


frame = simplegui.create_frame("NAME", 500, 500)

def runGame():
    #menu()
    #SpriteSelect()
    print("running gameloop")
    gameLoop()


def menu():
    #MainMenu.init()
    pass
def spriteSelect():
    #SpriteSelect.init()
    pass

def gameLoop():
    GameLoop.init()