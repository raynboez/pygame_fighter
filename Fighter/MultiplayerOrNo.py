from Fighter import Master
from Fighter.Keyboard import MenuKeyboard
from Fighter.Mouse import Mouse
from Fighter.Ai import Ai
from Fighter.Sprite import Sprite

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui



sprites = {
    "Red" : "https://i.ibb.co/M7Ff2wx/redsheet.png",
    "Blue" : "https://i.ibb.co/2hv9qcq/bluesheet.png",
    "Green" : "https://i.ibb.co/K2616MG/greensheet.png",
    "Yellow" : "https://i.ibb.co/CbMDdVC/yellowsheet.png",
    "Base" : "https://i.ibb.co/6m5sd2h/fullsheet.png"
}

selected = False
#Todo add image for 1v1 and you vs cpu
#image = simplegui.load_image("https://i.ibb.co/TqyhqKk/IMG-20190322-WA0000.jpg")
#img_size = (500, 500)
aisprite = Sprite(sprites["Base"], 210, 52, 2, 14, (350, 225), 4, "idle", "left")
pvpsprite = Sprite(sprites["Red"], 210, 52, 2, 14, (150, 225), 4, "idle", "right")

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
    aisprite.updateStatic(canvas)
    pvpsprite.updateStatic(canvas)
    interaction()
    #canvas.draw_image(image, (img_size[0] // 2, img_size[1] // 2), img_size, (250, 250),
     #                 (500, 500))
    if selected and pointer == 1:
        Master.gameLoop('Base', 'Red')
    if selected and pointer == 0:
        Master.gameLoop('Green', 'Blue')
    canvas.draw_polygon([[100 + (pointer *200), 350],[100 + (pointer *200), 150],[200 + (pointer *200), 150],[200 + (pointer *200), 350]], 5, "Red")
    canvas.draw_text("PvP", (130, 300), 20, "White")
    canvas.draw_text("StoryMode", (307, 300), 20, "White")