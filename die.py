from random import randint

class Die():
    '''表示色子'''
    def __init__(self,num_side=6):
        self.num_side = 6
    def roll(self):
        return randint(1,self.num_side)
