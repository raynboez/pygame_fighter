from Fighter import Master
from Fighter.Keyboard import InstructionsKeyboard
from Fighter.Mouse import Mouse

def init():
    Master.masterframe.setDrawHandler(draw)
    Mouse.screen = "instructions"
    Master.masterframe.setKeydownHandler(kbd)

def instructions(canvas):
    canvas.draw_text("HOW TO PLAY", (50, 50), 25, "White")

    canvas.draw_text("Player 1", (100, 75), 20, "White", 'monospace')
    canvas.draw_text("MOVE:", (100, 100), 15, "White", 'monospace')
    canvas.draw_text("A, D", (100, 120), 15, "White", 'monospace')
    canvas.draw_text("JUMP:", (100, 140), 15, "White", 'monospace')
    canvas.draw_text("W", (100, 160), 15, "White", 'monospace')
    canvas.draw_text("BLOCK", (100, 180), 15, "White", 'monospace')
    canvas.draw_text("S", (100, 200), 15, "White", 'monospace')
    canvas.draw_text("ATTACK", (100, 220), 15, "White", 'monospace')
    canvas.draw_text("E", (100, 240), 15, "White", 'monospace')
    canvas.draw_text("FIRE", (100, 260), 15, "White", 'monospace')
    canvas.draw_text("Q", (100, 280), 15, "White", 'monospace')

    canvas.draw_text("Player 2", (250, 75), 20, "White", 'monospace')
    canvas.draw_text("MOVE:", (250, 100), 15, "White", 'monospace')
    canvas.draw_text("J, L", (250, 120), 15, "White", 'monospace')
    canvas.draw_text("JUMP:", (250, 140), 15, "White", 'monospace')
    canvas.draw_text("I", (250, 160), 15, "White", 'monospace')
    canvas.draw_text("BLOCK", (250, 180), 15, "White", 'monospace')
    canvas.draw_text("K", (250, 200), 15, "White", 'monospace')
    canvas.draw_text("ATTACK", (250, 220), 15, "White", 'monospace')
    canvas.draw_text("O", (250, 240), 15, "White", 'monospace')
    canvas.draw_text("FIRE", (250, 260), 15, "White", 'monospace')
    canvas.draw_text("U", (250, 280), 15, "White", 'monospace')

    canvas.draw_text("Yellow Bar is the Energy bar of your character", (50, 330), 15, "White", 'monospace')
    canvas.draw_text("Red Bar is the Health bar of your character", (50, 350), 15, "White", 'monospace')



    canvas.draw_text("Press any key to exit", (160, 400), 15, "White")

def draw(canvas):
    instructions(canvas)
    if kbd.next:
        kbd.key_up(next)
        Master.menu()

kbd = InstructionsKeyboard()


