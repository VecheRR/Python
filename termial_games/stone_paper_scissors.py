import random
from termcolor import colored

# scissors, paper, stone

enemy = random.randint(1, 3)

draw = colored('Draw.', 'yellow')
won = colored('You won', 'green')
lose = colored('You lose', 'red')

try:
    print('Input your thing, please.\n1) Scissors.\n2) Paper.\n3) Stone.\n')
    my_thing = int(input())
    if my_thing == 1:
        print('{}\nThe enemy chose SCISSORS.'.format(draw) if enemy == 1 else '{}\nThe enemy chose PAPER.'.format(won) if enemy == 2 else '{}\nThe enemy chose STONE.'.format(lose))
    elif my_thing == 2:
        print('{}\nThe enemy chose SCISSORS'.format(lose) if enemy == 1 else '{}\nThe enemy chose PAPER'.format(draw) if enemy == 2 else '{}\nThe enemy chose STONE.'.format(won))
    elif my_thing == 3:
        print('{}\nThe enemy chose SCISSORS.'.format(won) if enemy == 1 else '{}\nThe enemy chose PAPER.'.format(lose) if enemy == 2 else '{}\nThe enemy chose STONE.'.format(draw))
    else:
        print('Your number is incorrect. Input INT number between 1 and 3.')
except:
    print("ERROR! Input only INT number (1/2/3), please.")