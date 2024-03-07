#1-1
import random

print("Start 'rock-paper-scissors' game")
print('Input your hand choice')
choice = int(input('0=Rock, 1=paper, 2=scissor'))
comp_choice = random.randint(0, 2)

# print(comp_choice)
if choice == 0:
    if comp_choice == 0:
        print('Draw')
    elif comp_choice == 1:
        print('win')
    else:
        print('loose')
elif choice == 1:
    if comp_choice == 1:
        print('Draw')
    elif comp_choice == 2:
        print('loose')
    else:
        print('win')
elif choice == 2:
    if comp_choice == 2:
        print('Draw')
    elif comp_choice == 0:
        print('loose')
    else:
        print('win')
else:
    print('Chose between 0,1 and 2')
