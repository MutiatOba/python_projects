#short code to play rock paper and scissors game

import random

def play():
    user = input("'r' for rock, 'p' for paper, 's' for scissors: ")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'it\'s a tie'

    if is_win(user, computer):
        return 'you won'
    
    if is_win(computer, user):
        return 'you lost'

def is_win(player, opponent):
    #return true if player wins
    if (player =='r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent =='r'):
        return True 

print(play())
