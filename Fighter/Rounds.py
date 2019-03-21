try:
    import simplegui
except ImportError:
        import SimpleGUICS2Pygame as simplegui

timer = 0
delay = 60

class Rounds:

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        #self.maxrounds = maxrounds

    def start(self):
        self.roundNum = 1

    def over(self, character):
        global timer, delay
        if (self.player1.lives.value == 0) or (self.player2.lives.value == 0):
            self.end(character)
        else:
            if timer == delay:
                self.roundNum += 1
                timer = 0
                self.nextRound()
            else:
                timer+=1

    def nextRound(self):
        self.player1.newLife()
        self.player2.newLife()

    def end(self, character):#canvas, text):
        #print(character.p_number + " has died")
        #canvas.draw_text(text + "has won!", text_pos, 12, 'Blue')
        quit(1)  #return to main menu
