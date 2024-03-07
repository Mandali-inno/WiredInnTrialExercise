import random

# print("Start 'rock-paper-scissors' game")
# print('Input your hand choice')
# choice = int(input('0=Rock, 1=paper, 2=scissor'))
# comp_choice = random.randint(0, 2)
#
# # print(comp_choice)
# if choice == 0:
#     if comp_choice == 0:
#         print('Draw')
#     elif comp_choice == 1:
#         print('win')
#     else:
#         print('loose')
# elif choice == 1:
#     if comp_choice == 1:
#         print('Draw')
#     elif comp_choice == 2:
#         print('loose')
#     else:
#         print('win')
# elif choice == 2:
#     if comp_choice == 2:
#         print('Draw')
#     elif comp_choice == 0:
#         print('loose')
#     else:
#         print('win')
# else:
#     print('Chose between 0,1 and 2')
#

# 1-3

def startMessage():
     print("Start 'rock-paper-scissors' game")

def get_player():
    print('Input your hand choice')
    return int(input('0=Rock, 1=paper, 2=scissor'))

def get_computer():
    return random.randint(0,2)

def viewResult():

    hand_diff = get_player - get_computer()
    if hand_diff == 0:
        print('draw')
    elif hand_diff == -1 or hand_diff == 2:
        print('win')
    else:
        print('lose')

def get_hand(hand_number):
    hands={0:'rock', 1:'scissor', 2:'paper'}
    return hands[hand_number]

def view_hand(your_hand, comp_hand):
    print('My hand is' + get_hand(your_hand))
    print("Computer's hand is" + get_hand(comp_hand))

startMessage()
get_player()
get_computer()
view_hand(get_player(), get_computer())
viewResult()


