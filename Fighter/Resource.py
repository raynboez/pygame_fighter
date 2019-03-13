class Resource:
    def __init__(self, num, max):
        self.value = num
        self.origin = num
        self.max = max

    def remove(self, num):
        self.value-=num

    def add(self,num):
        self.value+=num
        if(self.value > self.max):
            self.value = self.max

    def restore(self):
        self.value = self.origin

    def draw(self, canvas, player):
       pass
       # current_percent = ( self.value / self.max ) * 100
       # canvas.draw_line()