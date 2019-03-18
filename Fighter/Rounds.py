try:
    import simplegui
except ImportError:
        import SimpleGUICS2Pygame as simplegui


class Rounds:

    def __init__(self, maxrounds, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.maxrounds = maxrounds

    def start(self):
        self.roundNum = 1

    def over(self, character):
        if (self.player1.lives.value == 0) or (self.player2.lives.value == 0):
            self.end(character)
        else:
            self.roundNum += 1
            self.nextRound()


    def nextRound(self):
        self.player1.newLife()
        self.player2.newLife()

    def end(self, character):#canvas, text):
        #print(character.p_number + " has died")
        #canvas.draw_text(text + "has won!", text_pos, 12, 'Blue')
        quit(1)  #return to main menu
