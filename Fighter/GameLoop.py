try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
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

CANVAS_WIDTH = 500
CANVAS_HEIGHT = 500

player1Sprite = Sprite("https://i.ibb.co/vqQr5QQ/Place-Holder.png", 180, 350, 7, 6, (100, 300), 1)  ##TODO
player2Sprite = Sprite("https://i.ibb.co/vqQr5QQ/Place-Holder.png", 180, 350, 7, 6, (400, 300), 1)  ##Get Sprite sheets
player1 = Character(player1Sprite, Vector(100, 300), 1, 'right')
player2 = Character(player2Sprite, Vector(400, 300), 2, 'left')
round = Rounds(player1, player2)

#when GameLoop is called by a class, init starts the frame
def init():
    Master.masterframe.setDrawHandler(draw)
    #Master.masterframe.set_canvas_background('rgba(0, 200, 200, 0.3)')

    Master.masterframe.setKeydownHandler(kbd)
    Master.masterframe.setKeyupHandler(kbd)

    #display main menu
    #
    round.start()
    Master.masterframe.start()


#main draw handler, updates all interactions and then draws objects on frame
def draw(canvas):

    interactions.update(round)
    background.draw(canvas)
    player1.draw(canvas, player2)   #fireball drawing done in character draw
    player2.draw(canvas, player1)
    platform_bottom.draw(canvas)

#initialises a keyboard
kbd = Keyboard()

#creates arena with background
background = Background()
platform_bottom = Platform(CANVAS_WIDTH, 400, 10, 'Grey')
walla = Wall(CANVAS_WIDTH, CANVAS_HEIGHT, 10, 'Red')
wallb = Wall(0, CANVAS_HEIGHT, 10, 'Red')

#creates interaction class and adds the objects
interactions = Interaction(kbd)
interactions.addCharacter(player1)
interactions.addCharacter(player2)
interactions.addPlatform(platform_bottom)
interactions.addWall(walla)
interactions.addWall(wallb)


#TODO list
#
#hitboxes
#   adjust punch and kick hitbox
#
#player collisions
#   players not drawn over each other?
#
#
#knockback on punch?
#   player being hit moves back a little
#
#knockback on kick
#   player being kicked moves back more
#   player doing kicking recoils
#