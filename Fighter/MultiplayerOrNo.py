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
redsprite = Sprite(sprites["Red"], 210, 52, 2, 14, (135, 253), 2, "idle", "right")
greensprite = Sprite(sprites["Green"], 210, 52, 2, 14, (135, 199), 2, "idle", "right")
bluesprite = Sprite(sprites["Blue"], 210, 52, 2, 14, (165, 253), 2, "idle", "left")
yellowsprite = Sprite(sprites["Yellow"], 210, 52, 2, 14, (165, 199), 2, "idle", "left")
kbd = MenuKeyboard()
pointer = 0
timer = 0

def init():
    global selected
    #Ai.leve1 = 0
    Master.masterframe.setDrawHandler(draw)
    Mouse.screen = "MultOrNo"
    Master.masterframe.setKeydownHandler(kbd)
    Master.masterframe.setKeyupHandler(kbd)
    selected = False

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
    canvas.draw_polygon([(0, 400), (0, 100), (500, 100), (500,400)], 5, "Grey", "Grey")
    global selected
    global pointer
    aisprite.updateStatic(canvas)

    redsprite.updateStatic(canvas)
    greensprite.updateStatic(canvas)
    bluesprite.updateStatic(canvas)
    yellowsprite.updateStatic(canvas)

    interaction()
    #canvas.draw_image(image, (img_size[0] // 2, img_size[1] // 2), img_size, (250, 250),
     #                 (500, 500))

    if (Mouse.multiNoSel):
        pointer = Ai.level
        Mouse.multiNoSel = False
        selected = True
    if selected and pointer == 1:
        Master.levelSelect()
    if selected and pointer == 0:
        Master.spriteSelect()
    canvas.draw_polygon([[100 + (pointer *200), 315],[100 + (pointer *200), 150],[200 + (pointer *200), 150],[200 + (pointer *200), 315]], 5, "Red")
    canvas.draw_text("Vs Player", (108, 300), 20, "White")
    canvas.draw_text("Vs CPU", (315, 300), 20, "White")