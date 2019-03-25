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
redsprite = Sprite(sprites["Red"], 210, 52, 2, 14, (100, 235), 4, "idle", "left")
greensprite = Sprite(sprites["Green"], 210, 52, 2, 14, (200, 235), 4, "idle", "left")
bluesprite = Sprite(sprites["Blue"], 210, 52, 2, 14, (400, 235), 4, "idle", "left")
yellowsprite = Sprite(sprites["Yellow"], 210, 52, 2, 14, (300, 235), 4, "idle", "left")
kbd = MenuKeyboard()
pointer = 0
timer = 0

def init():
    global selected
    #Ai.leve1 = 0
    Master.masterframe.setDrawHandler(draw)
    Mouse.screen = "null"
    Master.masterframe.setKeydownHandler(kbd)
    Master.masterframe.setKeyupHandler(kbd)
    selected = False

def interaction():
    global pointer, timer
    if timer > 7:
        if kbd.left:
            timer = 0
            pointer -=1
        if kbd.right:
            timer = 0
            pointer +=1
        if pointer < 0:
            pointer = 0
        elif pointer > 3:
            pointer = 3
        if kbd.enter:
            timer = 0
            select()
    timer += 1

def select():
    global selected
    if pointer == 0:
        Ai.level = 1
    if pointer == 1:
        Ai.level = 1
    if pointer == 2:
        Ai.level = 1
    else:
        Ai.level = 1
    kbd.enter = 0
    selected = True

def draw(canvas):
    canvas.draw_polygon([(0, 400), (0, 100), (500, 100), (500,400)], 5, "Grey", "Grey")
    global selected
    redsprite.updateStatic(canvas)
    greensprite.updateStatic(canvas)
    bluesprite.updateStatic(canvas)
    yellowsprite.updateStatic(canvas)

    interaction()
    #canvas.draw_image(image, (img_size[0] // 2, img_size[1] // 2), img_size, (250, 250),
     #                 (500, 500))
    if selected and pointer == 0:
        Master.gameLoop('Base', 'Red')
    if selected and pointer == 1:
        Master.gameLoop('Base', 'Green')
    if selected and pointer == 2:
        Master.gameLoop('Base', 'Yellow')
    if selected and pointer == 3:
        Master.gameLoop('Base', 'Blue')
    canvas.draw_polygon([[50 + (pointer *100), 315],[50 + (pointer *100), 150],[150 + (pointer *100), 150],[150 + (pointer *100), 315]], 5, "Red")
    canvas.draw_text("Level 1", (75, 300), 20, "White")
    canvas.draw_text("Level 2", (175, 300), 20, "White")
    canvas.draw_text("Level 3", (275, 300), 20, "White")
    canvas.draw_text("Level 4", (375, 300), 20, "White")