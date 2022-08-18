import random
import time

roll_again= 'yes'

while roll_again =='yes' or roll_again == 'y':
    # Gets number of both dices 
    dice1 = random.randint(1,6)
    dice2 =random.randint(1,6)

    print('Rolling.....')
    # Waits a moment to provide results. 
    time.sleep(.8)

    # Prints results of both dice 
    print(f'You rolled {dice1} and {dice2}! ') 


    Roll_again=input('Roll again?')
