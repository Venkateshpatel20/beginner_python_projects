import random 


def play():
    user = input("choose one 'r' for Rock , 'p' for Paper and 's' for Scissor,if you want to exit enter Quit 'q' : ")
    computer = random.choice(['r','p','s'])
    if user == 'q':
        return "You are out of game now!"
    elif user == computer :
        return "It\'s a tie"
    elif is_win(user , computer):
        return "You Won"
    return "Computer Won"
def is_win(player , opponent):
    #return True if player wins
    # r > s ,p > r , s > p
    if (player == 'r' and opponent == 's') or \
        (player == 'p' and opponent == "r") or \
        (player == 's' and opponent == "p"):
        return True
    
while True:
    print(play())
    

    


