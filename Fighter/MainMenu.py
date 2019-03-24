from Fighter import Master
from Fighter.Keyboard import MenuKeyboard
from Fighter.Mouse import Mouse

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

image = simplegui.load_image("https://i.ibb.co/TqyhqKk/IMG-20190322-WA0000.jpg")
img_size = (500, 500)
kbd = MenuKeyboard()

def init():
    Master.masterframe.setDrawHandler(draw)
    Mouse.screen = "menu"
    Master.masterframe.setKeydownHandler(kbd)
    Master.masterframe.setKeyupHandler(kbd)
    Master.masterframe.start()

def draw(canvas):
    canvas.draw_image(image, (img_size[0] // 2, img_size[1] // 2), img_size, (250, 250),
                      (500, 500))
    if kbd.quit:
        quit(0)
    if kbd.instructions:
        kbd.key_up(next)
        Master.instructions()
    if kbd.playgame:
        kbd.key_up(next)
        Master.gameLoop('Yellow', 'Red')

    canvas.draw_text("Exit(b)", (363, 74), 20, "White")
    canvas.draw_text("Instructions(n)", (363, 157), 20, "White")
    canvas.draw_text("Play(m)", (363, 240), 20, "White")

def music():
    pass