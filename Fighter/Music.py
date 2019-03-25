try:
  import simplegui
except:
  import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

class Music:
  def __init__(self):
    self.menu = simplegui.load_sound("https://raw.githubusercontent.com/raynboez/pygame_fighter/master/Fighter/music/Maz%20Nimra%20-%20Level%20One.ogg")
    self.fight = simplegui.load_sound("https://raw.githubusercontent.com/raynboez/pygame_fighter/master/Fighter/07%20Battle%20of%20Pogs.ogg")
    self.currentSound = self.menu
    self.menu.set_volume(1)
    self.fight.set_volume(1)
    
  def play(self, music):
    if music == "menu":
      self.menu.play()
      self.currentSound = self.menu
    elif music == "fight":
      self.fight.play()
      self.currentSound = self.fight

  def pause(self):
    self.currentSound.pause()

