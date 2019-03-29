from Fighter import Master
from Fighter.Keyboard import InstructionsKeyboard
from Fighter.Mouse import Mouse
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui


def init():
    Master.masterframe.setDrawHandler(draw)
    Mouse.screen = "instructions"
    Master.masterframe.setKeydownHandler(kbd)

def storysplash(canvas):
    canvas.draw_text("STORY", (50, 50), 25, "White")

    canvas.draw_text("THERE WAS AN ALIEN", (100, 75), 20, "White", 'monospace')
    canvas.draw_text("HE HATED TOBY'S COLOUR", (100, 100), 15, "White", 'monospace')
    canvas.draw_text("HE CREATED MANY OTHER TOBYS", (100, 120), 15, "White", 'monospace')
    canvas.draw_text("THEY HAD COOLER COLOURS", (100, 140), 15, "White", 'monospace')
    canvas.draw_text("HELP TOBY DEFEAT HIS MORTAL ENEMY:", (100, 160), 15, "White", 'monospace')
    canvas.draw_text("HIMSELF", (100, 180), 15, "White", 'monospace')
    canvas.draw_text("BUT COOLER", (100, 200), 15, "White", 'monospace')

    canvas.draw_text("Press any key to start", (160, 400), 15, "White")

def draw(canvas):
    storysplash(canvas)
    if kbd.next:
        kbd.key_up(next)
        Master.menu()

kbd = InstructionsKeyboard()


