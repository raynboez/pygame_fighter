from Fighter.Platform import Platform
from Fighter import GameLoop
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui


def main():
    GameLoop.init()


if __name__ == '__main__':
    main()
