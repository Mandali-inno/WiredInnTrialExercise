import random

# 1-3

def startMessage():
     print("Start 'rock-paper-scissors' game")

def get_player():
    print('Input your hand choice')
    return int(input('0=Rock, 1=paper, 2=scissor'))

def get_computer():
    return random.randint(0,2)



def viewResult():

    hand_diff = get_player() + get_computer()
    if hand_diff == 0:
        print('draw')
    elif hand_diff == -1 or hand_diff == 2:
        print('win')
    else:
        print('lose')


viewResult()


