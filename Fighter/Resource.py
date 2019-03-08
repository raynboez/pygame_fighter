class Resource:
    def __init__(self, num):
        self.value = num

    def remove(self, num):
        self.value-=num

    def add(self,num):
        self.value+=num