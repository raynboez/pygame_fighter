class Resource:
    def __init__(self, num, maximum):
        #current stored value
        self.value = num
        #initial value (0 for energy, 100 for health etc
        self.origin = num
        #maximum possible value
        self.max = maximum


    #decrease resource with limits
    def remove(self, num):
        self.value-=num
        if self.value < 0:
            self.value = 0

    #increase resource with limits
    def add(self,num):
        self.value += num
        if self.value > self.max:
            self.value = self.max

    #reset resource to original value
    def restore(self):
        self.value = self.origin

    #can be used later to draw health bars, energy bars etc
    def draw(self, canvas, playernumber, colour):
        if(colour == 'Yellow'):
            if (playernumber == 1):
                canvas.draw_line((10, 450), (self.value*2+10, 450), 5, colour)
                print(self.value)
            if(playernumber == 2):
                canvas.draw_line((500-10, 450), (500-(self.value*2+10), 450), 5, colour)
                print(self.value)

        if(colour == 'Blue'):
            if (playernumber == 1):
                canvas.draw_line((10, 460), (self.value*2+10, 460), 5, colour)
                print(self.value)
            if(playernumber == 2):
                canvas.draw_line((500-10, 460), (500-(self.value*2+10), 460), 5, colour)
                print(self.value)
       # current_percent = ( self.value / self.max ) * 100
       # canvas.draw_line()