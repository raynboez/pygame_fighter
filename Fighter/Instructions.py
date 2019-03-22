from Fighter import Master
from Fighter.Keyboard import InstructionsKeyboard

def init():
    Master.masterframe.setDrawHandler(draw)
    Master.masterframe.setKeydownHandler(kbd)
    Master.masterframe.setKeydownHandler(kbd)
    Master.masterframe.start()

def instructions(canvas):
    canvas.draw_text("HOW TO PLAY", (50, 50), 25, "White")
    canvas.draw_text("Player 1", (100, 75), 20, "White")
    canvas.draw_text("MOVE:", (100, 100), 15, "White")
    canvas.draw_text("A, D", (100, 120), 15, "White")
    canvas.draw_text("JUMP:", (100, 140), 15, "White")
    canvas.draw_text("W", (100, 160), 15, "White")
    canvas.draw_text("BLOCK", (100, 180), 15, "White")
    canvas.draw_text("S", (100, 200), 15, "White")
    canvas.draw_text("ATTACK", (100, 220), 15, "White")
    canvas.draw_text("E", (100, 240), 15, "White")
    canvas.draw_text("FIRE", (100, 260), 15, "White")
    canvas.draw_text("Q", (100, 280), 15, "White")
    canvas.draw_text("Player 2", (200, 75), 20, "White")
    canvas.draw_text("MOVE:", (200, 100), 15, "White")
    canvas.draw_text("J, L", (200, 120), 15, "White")
    canvas.draw_text("JUMP:", (200, 140), 15, "White")
    canvas.draw_text("I", (200, 160), 15, "White")
    canvas.draw_text("BLOCK", (200, 180), 15, "White")
    canvas.draw_text("K", (200, 200), 15, "White")
    canvas.draw_text("ATTACK", (200, 220), 15, "White")
    canvas.draw_text("O", (200, 240), 15, "White")
    canvas.draw_text("FIRE", (200, 260), 15, "White")
    canvas.draw_text("U", (200, 280), 15, "White")

def draw(canvas):
    instructions(canvas)
    if kbd.next:
        Master.gameLoop("Red", "Blue")

kbd = InstructionsKeyboard()


