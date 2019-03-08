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

CANVAS_WIDTH = 500
CANVAS_HEIGHT = 500
NAME = 'TestFrame'


def init():
    frame.start()


def draw(canvas):
    interactions.update()
    for player in players:
        player.draw(canvas)
    platform_top.draw(canvas)
    platform_bottom.draw(canvas)






kbd = Keyboard()
player1Sprite = Sprite(".\\Sprites\\PlaceHolder.png", 180, 350, 7, 6, (100, 300), 1)##TODO
player2Sprite = Sprite(".\\Sprites\\PlaceHolder.png", 180, 350, 7, 6, (400, 300), 1)##TODO
player1 = Character(player1Sprite, Vector(100, 300), Vector(0,0), 1, 'right')
player2 = Character(player2Sprite, Vector(400, 300), Vector(0,0),2, 'left')
platform_top = Platform(CANVAS_WIDTH, 50, 10, 'Grey')
platform_bottom = Platform(CANVAS_WIDTH, 400, 10, 'Grey')

players = [player1, player2]
interactions = Interaction(kbd)
interactions.addCharacter(player1)
interactions.addCharacter(player2)
interactions.addPlatform(platform_top)
interactions.addPlatform(platform_bottom)

frame = simplegui.create_frame(NAME, CANVAS_WIDTH, CANVAS_HEIGHT)
frame.set_draw_handler(draw)
# frame.set_keydown_handler(kbd.keydown)#todo
# frame.set_keyup_handler(kbd.keyup)#todo

#TODO
#keyboard stuff
#   2 keyboards - 1 for wasd, one for arrow keys?
#   left, right, up, down, attack, fire
#
#resources
#   generic class, used for lives, health, energy
#
#
#
#sprites
#
#platform interactions
#   gravity
#   jumping
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
