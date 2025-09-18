"""
Question 1: Beginner Number Guessing Game

Create a simple number guessing game with these requirements:

Random number between 1-20
    Maximum 6 attempts
    Show remaining attempts after each guess
    Display appropriate win/lose messages
    Validate numeric input only
    
Example 

    === SIMPLE GUESSING GAME ===
    Guess my number between 1 and 20!
    You have 6 attempts.

    Attempt 1/6 - Enter your guess: 10
    Too low! Try again.

    Attempt 2/6 - Enter your guess: 15
    Too high! Try again.

    Attempt 3/6 - Enter your guess: 12
    Congratulations! You won in 3 attempts!

"""

import random
 
def test_random():
    random_number = random.randint(1, 20)
    attempts = 6
   
    for num in range(attempts):
        print(f'รอบที่ {num+1} ')
        number = int(input(f'input number {num+1}/6 = '))
        if number == random_number:
            print('you win เก่งวะๆ')
            break
        elif number > random_number:
            print('Too high')
        else:
            print('Too low')
    else:
        print('You lose กากวะๆ')
    print(f'Number Win is : {random_number} ')
 
test_random()