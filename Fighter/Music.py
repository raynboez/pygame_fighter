try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

class Music:
    def __init__(self):
      self.menu = simplegui.load_sound("https://raw.githubusercontent.com/raynboez/pygame_fighter/master/Fighter/music/Maz%20Nimra%20-%20Level%20One.ogg")
      self.fight = simplegui.load_sound("https://raw.githubusercontent.com/raynboez/pygame_fighter/master/Fighter/music/07%20Battle%20of%20Pogs.ogg")
      self.currentSound = self.menu
      self.menu.set_volume(0.2)#todo change back to 1
      self.fight.set_volume(0.2)
    
    def play(self, music):
      if music == "menu":
          self.menu.play()
          self.currentSound = self.menu
      elif music == "fight":
          self.fight.play()
          self.currentSound = self.fight

    def pause(self):
      self.currentSound.pause()

