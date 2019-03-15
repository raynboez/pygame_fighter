from Fighter import Master
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

############################################################
#
#   run this class to play the game
#
############################################################


def main():
    print("running master")
    Master.runGame()


if __name__ == '__main__':
    main()
