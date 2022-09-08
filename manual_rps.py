import random

class RPS():

    def __init__(self, compchoice, userchoice):
        compchoice = []
        self.compchoice = compchoice
        userchoice = []
        self.userchoice = userchoice
        self.options = ['rock', 'paper', 'scissors']

    def get_computer_choice (self):
        self.compchoice = random.choice(self.options)

    def get_user_choice (self):
        self.userchoice = input ('You choose: ').lower()
        if input not in self.options:
            print ('Your input is invalid')
        

    def find_winner (self):
        if self.compchoice == self.userchoice:
            print ('It is a draw')
        
        elif self.options.index(self.userchoice) - self.options.index(self.compchoice) == -2 or 1:
            print ('You won')
'''
The above code was used as i worked out those were the values obtained from the winning index subtraction. Rock is 0, Paper is 1 and Scissors is 2.
R-S = -2; P-R & S-P = 1
'''
        else:
            print ('You lost')

def play_game():
    game = RPS()
    while True:
        game.find_winner()

if __name__ == '_main_':
    play_game()
