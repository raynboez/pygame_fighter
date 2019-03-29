#Jed Arno
from Fighter.Mouse import Mouse
from Fighter.Sprite import Sprite
from Fighter.Sprite import StaticSprite
from Fighter.Keyboard import Keyboard
from Fighter.Cursor import Cursor
from Fighter.Navigation import Navigation
from Fighter import Master

kbd = Keyboard(False)

def init():
    Mouse.screen = "spriteSelect"
    Master.masterframe.setDrawHandler(drawSpriteSheet)
    Master.masterframe.setKeydownHandler(kbd)
    Master.masterframe.setKeyupHandler(kbd)

cursor1 = Cursor([125, 105], [125, 255], [250, 255], [250, 105], 'cyan')
cursor1.addPos([250, 105], [250, 255], [375, 255], [375, 105], 0)
cursor1.addPos([125, 255], [125, 420], [250, 420], [250, 255], 1)
cursor1.addPos([250, 255], [250, 420], [375, 420], [375, 255], 1)

cursor2 = Cursor([125, 105], [125, 255], [250, 255], [250, 105], 'red')
cursor2.addPos([250, 105], [250, 255], [375, 255], [375, 105], 0)
cursor2.addPos([125, 255], [125, 420], [250, 420], [250, 255], 1)
cursor2.addPos([250, 255], [250, 420], [375, 420], [375, 255], 1)

player1 = Navigation(cursor1, kbd, 0)
player2 = Navigation(cursor2, kbd, 1)

selection = StaticSprite("https://i.ibb.co/wCnM7pP/fullscaled.png", 247, 322, [250, 255], 1)
previewSprites = [ "https://i.ibb.co/M7Ff2wx/redsheet.png",

    "https://i.ibb.co/2hv9qcq/bluesheet.png",
    "https://i.ibb.co/K2616MG/greensheet.png",
    "https://i.ibb.co/CbMDdVC/yellowsheet.png"]

selectedSprite1 = Sprite("https://i.ibb.co/p0QcQJg/lights.png", 30, 27, 1, 2, [100, 100], 2, "on", "left")
selectedSprite2 = Sprite("https://i.ibb.co/p0QcQJg/lights.png", 30, 27, 1, 2, [400, 100], 2, "off", "left")

finalnames = [ "Red", "Blue", "Green", "Yellow"]

def ready():
    if cursor1.getSelected() and cursor2.getSelected():

        cursor1.deselect()
        cursor2.deselect()
        return True
    else:
        return False

def drawSpriteSheet(canvas):
    canvas.draw_polygon([[125, 105], [125, 420], [375, 420], [375, 105]], 1, 'Grey', 'Grey')
    canvas.draw_text("Select Sprite", (200, 50), 20, "White")
    player1.update()
    player2.update()
    selection.draw(canvas)
    if Mouse.spriteSel1:
        cursor1.selected = True
        if not Mouse.spriteSel2:
            cursor1.position = Mouse.spriteSelection
    if Mouse.spriteSel2:
        Mouse.spriteSel1 = False
        cursor2.selected = True
        cursor2.position = Mouse.spriteSelection
        Mouse.spriteSel2 = False
    if cursor1.getSelected():
        selectedSprite1.changeState("on")
        selectedSprite1.nextSprite()
    else:
        selectedSprite1.changeState("off")
        selectedSprite1.nextSprite()
    if cursor2.getSelected():
        selectedSprite2.changeState("on")
        selectedSprite2.nextSprite()
    else:
        selectedSprite2.changeState("off")
        selectedSprite2.nextSprite()
    cursor1.draw(canvas)
    cursor2.draw(canvas)
    Sprite(previewSprites[cursor1.previewSelection()], 210, 52, 2, 14, (50, 250), 8, "idle", "right").updateStatic(canvas)
    Sprite(previewSprites[cursor2.previewSelection()], 210, 52, 2, 14, (450, 250), 8, "idle", "left").updateStatic(canvas)
    selectedSprite1.draw(canvas)
    selectedSprite2.draw(canvas)
        
    if ready():
        Master.gameLoop(finalnames[cursor1.previewSelection()], finalnames[cursor2.previewSelection()], False)
