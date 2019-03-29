from Fighter.Ai import Ai
from Fighter.Platform import Platform
from Fighter.Sprite import Sprite
from Fighter.Character import Character
from Fighter.Keyboard import Keyboard
from Fighter.Interaction import Interaction
from Fighter.Vector import Vector
from Fighter.Wall import Wall
from Fighter.Background import Background
from Fighter import Master
from Fighter.Rounds import Rounds
from Fighter.Mouse import Mouse

CANVAS_WIDTH = 500
CANVAS_HEIGHT = 500
has_ai = False
sprites = {
    "Red" : "https://i.ibb.co/M7Ff2wx/redsheet.png",
    "Blue" : "https://i.ibb.co/2hv9qcq/bluesheet.png",
    "Green" : "https://i.ibb.co/K2616MG/greensheet.png",
    "Yellow" : "https://i.ibb.co/CbMDdVC/yellowsheet.png",
    "Base" : "https://i.ibb.co/6m5sd2h/fullsheet.png"
}
SPRITE1 = "Red"
SPRITE2 = "Blue"
player1Sprite = Sprite(sprites[SPRITE1], 2, 14, (100, 300), 4, "idle", "left")
player2Sprite = Sprite(sprites[SPRITE2], 2, 14, (400, 300), 4, "idle", "right")  ##Get Sprite sheets
player1 = Character(player1Sprite, Vector(100, 300), 1, 'right')
player2 = Character(player2Sprite, Vector(400, 300), 2, 'left')
round = Rounds(player1, player2)

#when GameLoop is called by a class, init starts the frame
def init(sp1, sp2, ai):
    global SPRITE1, SPRITE2, has_ai
    has_ai = ai
    kbd.ai = has_ai
    SPRITE1 = sp1
    SPRITE2 = sp2
    Master.masterframe.setDrawHandler(draw)
    Mouse.screen = "game"
    #Master.masterframe.set_canvas_background('rgba(0, 200, 200, 0.3)')

    Master.masterframe.setKeydownHandler(kbd)
    Master.masterframe.setKeyupHandler(kbd)
    Master.music.pause()
    Master.music.play("fight")

    player1Sprite = Sprite(sprites[SPRITE1], 2, 14, (100, 300), 4, "idle", "left")
    player2Sprite = Sprite(sprites[SPRITE2], 2, 14, (400, 300), 4, "idle", "right")
    player1.setSprite(player1Sprite, SPRITE1)
    player2.setSprite(player2Sprite, SPRITE2)
    #display main menu
    #
    round.reset()
    round.start()



#main draw handler, updates all interactions and then draws objects on frame
def draw(canvas):
    if kbd.ai and round.startTimer % ai.loopsPerGo == 0:##allows the ai to select a move once every x cycles of the gameloop
        Ai.move(Ai)
        if round.startTimer % 20 == 0:#stops moves lasting more than 20 cycles
            kbd.ai_keyup()
    round.startTimer +=1
    interactions.update(round)
    background.draw(canvas)
    player1.draw(canvas, player2)   #fireball drawing done in character draw
    player2.draw(canvas, player1)
    #platform_bottom.draw(canvas)
    if round.gameEnded:
        if round.startTimer < round.endTime + 180:
            round.drawend(canvas)

        else:
            #enter main menu
            kbd.key_up(next)
            round.gameEnded = False
            Master.menu()
    if round.startTimer < 180:
        round.draw(canvas)

#initialises a keyboard
kbd = Keyboard(has_ai)

#creates arena with background
background = Background()
platform_bottom = Platform(CANVAS_WIDTH, 400, 10, 'Grey')
walla = Wall(CANVAS_WIDTH + 10, CANVAS_HEIGHT, 10, 'Red')
wallb = Wall(-10, CANVAS_HEIGHT, 10, 'Red')

#creates interaction class and adds the objects
interactions = Interaction(kbd)
interactions.addCharacter(player1)
interactions.addCharacter(player2)
interactions.addPlatform(platform_bottom)
interactions.addWall(walla)
interactions.addWall(wallb)
ai = Ai(kbd)

#SPRITESHEET URLS
#
#https://i.ibb.co/vB3Q4QG/fullsheet.png
#   BASE

#https://i.ibb.co/CbMDdVC/yellowsheet.png
#   YELLOW

#https://i.ibb.co/M7Ff2wx/redsheet.png
#   RED

#https://i.ibb.co/2hv9qcq/bluesheet.png
#   BLUE

#https://i.ibb.co/K2616MG/greensheet.png
#   GREEN
