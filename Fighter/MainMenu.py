from Fighter import Master
from Fighter.Keyboard import MenuKeyboard
from Fighter.Mouse import Mouse

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

image = simplegui.load_image("https://i.ibb.co/wR6DF4M/IMG-20190325-WA0000.jpg")
img_size = (500, 500)
kbd = MenuKeyboard()
pointer = 2
timer = 0

def init():
    Master.masterframe.setDrawHandler(draw)
    Mouse.screen = "menu"
    Master.masterframe.setKeydownHandler(kbd)
    Master.masterframe.setKeyupHandler(kbd)

def playgame():
    kbd.key_up(next)
    Master.modeSelect()

def instructions():
    kbd.key_up(next)
    Master.instructions()

def quitgame():
    quit(0)

def interaction(canvas):
    global pointer, timer
    if timer > 4:
        timer = 0
        if kbd.up:
            pointer -= 1
        if kbd.down:
            pointer += 1
        if kbd.enter:
            select()
    else:
        timer+=1
    if pointer < 0:
        pointer = 2
    if pointer > 2:
        pointer = 0

def select():
    if pointer == 0:
        quitgame()
    elif pointer == 1:
        instructions()
    elif pointer == 2:
        playgame()


def draw(canvas):
    #User has option to contol main menu using keyboard


    canvas.draw_image(image, (img_size[0] // 2, img_size[1] // 2), img_size, (250, 250),
                      (500, 500))
    if pointer == 2:
        canvas.draw_circle((246, 74 + (83 * 2)), 40, 1, "Green", "Green")
    elif pointer == 1:
        canvas.draw_circle((246, 74 + (83 * 1)), 40, 1, "Orange", "Orange")
    else:
        canvas.draw_circle((246, 74), 40, 1, "Red", "Red")
    interaction(canvas)
    canvas.draw_text("Exit(b)", (363, 74), 20, "White")
    canvas.draw_text("Instructions(n)", (363, 157), 20, "White")
    canvas.draw_text("Play(m)", (363, 240), 20, "White")
    #canvas.draw_circle((246, 74 + (83 * pointer)), 45, 4, "Red")

