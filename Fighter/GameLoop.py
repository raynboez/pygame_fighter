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
NAME = 'PLACEHOLDER NAME'
player1Sprite = Sprite("https://i.ibb.co/vqQr5QQ/Place-Holder.png", 180, 350, 7, 6, (100, 300), 1)  ##TODO
player2Sprite = Sprite("https://i.ibb.co/vqQr5QQ/Place-Holder.png", 180, 350, 7, 6, (400, 300), 1)  ##TODO
player1 = Character(player1Sprite, Vector(100, 300), Vector(0, 0), 1, 'right')
player2 = Character(player2Sprite, Vector(400, 300), Vector(0, 0), 2, 'left')
round = Rounds(5, player1, player2)

#when GameLoop is called by a class, init starts the frame
def init():
    Master.frame.set_draw_handler(draw)
    Master.frame.set_canvas_background('rgba(0, 200, 200, 0.3)')

    Master.frame.set_keydown_handler(kbd.key_down)
    Master.frame.set_keyup_handler(kbd.key_up)

    #display main menu
    #
    round.start()
    Master.frame.start()


#main draw handler, updates all interactions and then draws objects on frame
def draw(canvas):

    interactions.update(round)
    background.draw(canvas)
    #fireball drawing done in character draw
    player1.draw(canvas, player2)
    player2.draw(canvas, player1)


    #draws platforms (platform_top has no interaction state)
    #qplatform_top.draw(canvas)
    platform_bottom.draw(canvas)



background = Background()

#initialises a keyboard
kbd = Keyboard()

#spritesheets will go here
#creating the characters - created above platform, then fall to platform




#creates platforms and walls
platform_top = Platform(CANVAS_WIDTH, 50, 10, 'Grey')
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

#sets bounds for frame and sets handlers


#TODO
#platform interactions
#   #   jumping - stop acceleration
#   double jump
#   edge of screen
#
#hitboxes
#   seperate hurtbox and hitbox
#
#player collisions
#   players not drawn over each other
#
#punch cooldown
#   timer based(can only punch once every half second)
#   timer starts when punch thrown
#   need to set up game timer
#
#knockback on punch?
#   player being hit moves back a little
#
#knockback on kick
#   player being kicked moves back more
#   player doing kicking recoils
