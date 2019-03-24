from Fighter import Master
from Fighter.Keyboard import MenuKeyboard
from Fighter.Mouse import Mouse
from Fighter.Ai import Ai

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

selected = False
#Todo add image for 1v1 and you vs cpu
#image = simplegui.load_image("https://i.ibb.co/TqyhqKk/IMG-20190322-WA0000.jpg")
#img_size = (500, 500)
kbd = MenuKeyboard()
pointer = 0
timer = 0

def init():
    #Ai.leve1 = 0
    Master.masterframe.setDrawHandler(draw)
    Mouse.screen = "MultOrNo"
    Master.masterframe.setKeydownHandler(kbd)
    Master.masterframe.setKeyupHandler(kbd)

def interaction():
    global pointer
    if kbd.left:
        pointer = 0
    if kbd.right:
        pointer = 1
    if kbd.enter:
        select()

def select():
    global selected
    if pointer == 1:
        Ai.level = 1
    else:
        Ai.level = 0
    kbd.enter = 0
    selected = True

def draw(canvas):
    global selected
    interaction()
    #canvas.draw_image(image, (img_size[0] // 2, img_size[1] // 2), img_size, (250, 250),
     #                 (500, 500))
    if selected and pointer == 1:
        Master.gameLoop('Yellow', 'Red')
    if selected and pointer == 0:
        Master.gameLoop('Green', 'Blue')
    canvas.draw_circle((120 + (pointer * 200), 300), 20, 4, "Red")
    canvas.draw_text("PvP(p)", (120, 300), 20, "White")
    canvas.draw_text("StoryMode(s)", (320, 300), 20, "White")