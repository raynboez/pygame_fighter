from Fighter import Master
from Fighter.Keyboard import MenuKeyboard
from Fighter.Mouse import Mouse

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui


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

def interaction():
    global pointer, timer
    if timer > 4:
        timer = 0
        if kbd.left:
            pointer = 0
        if kbd.right:
            pointer = 1

def draw(canvas):
    #canvas.draw_image(image, (img_size[0] // 2, img_size[1] // 2), img_size, (250, 250),
     #                 (500, 500))
    if kbd.playgame:
        kbd.playgame = False
        Master.gameLoop('Yellow', 'Red')

    canvas.draw_text("PvP(p)", (120, 300), 20, "White")
    canvas.draw_text("StoryMode(s)", (320, 300), 20, "White")