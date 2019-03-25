try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from Fighter import GameLoop
from Fighter import Instructions
from Fighter.Frame import Frame
from Fighter import SplashScreen
from Fighter import MainMenu
from Fighter import MultiplayerOrNo


#frame used throughout Game
masterframe = Frame("Name", 500, 500)#encapsulates simplegui.create_frame

def runGame():
    splashScreen()

def splashScreen():
    SplashScreen.init()

#adjust these classes when menu and spriteselect are created - can be used to hand over selections
def menu():
    MainMenu.init()
    #pass

def modeSelect():
    MultiplayerOrNo.init()

def instructions():
    Instructions.init()

def spriteSelect():
    #SpriteSelect.init()
    pass

def gameLoop(sprite1, sprite2):
    GameLoop.init(sprite1, sprite2)