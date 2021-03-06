from Fighter import GameLoop
from Fighter import Instructions
from Fighter.Frame import Frame
from Fighter import SplashScreen
from Fighter import MainMenu
from Fighter import MultiplayerOrNo
from Fighter import SpriteSelect
from Fighter.Music import Music
from Fighter import LevelSelect
from Fighter import StorySplash
#frame used throughout Game
masterframe = Frame("Road Wars", 500, 500)#encapsulates simplegui.create_frame

music = Music()

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

def levelSelect():
    LevelSelect.init()

def instructions():
    Instructions.init()

def spriteSelect():
    SpriteSelect.init()

def storySplash():
    StorySplash.init()

def gameLoop(sprite1, sprite2, ai):
    GameLoop.init(sprite1, sprite2, ai)
