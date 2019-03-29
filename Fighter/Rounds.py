timer = 0
delay = 60


class Rounds:

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.setEnd = False
        self.gameEnded = False
        self.startTimer = 0

    def reset(self):
        self.player1.lives.restore()
        self.player2.lives.restore()
        self.player1.newLife()
        self.player2.newLife()
        global timer
        self.roundNum = 0
        self.startTimer = 0
        timer = 0
        self.GameEnded = False
        self.setEnd = False


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
        self.startTimer = 0

    def end(self, character):
        self.gameEnded = True
        self.deadchar = character
        if not self.setEnd:
            self.endTime = self.startTimer
            self.setEnd = True

    def draw(self, canvas):
        canvas.draw_text('Round ' + str(self.roundNum), (180, 200), 50, 'White')

    def drawend(self, canvas):
        if self.deadchar.p_number == 1:
            self.winner = 'Player 2'
        else:
            self.winner = 'Player 1'
        canvas.draw_text(self.winner + " has won!", (120,200), 40, 'White')

