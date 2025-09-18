"""
#Question 2: Enhanced Guessing Game with Hints
Develop an enhanced guessing game with intelligent hint system:
Core Features:

Random number between 1-100
Unlimited attempts

Progressive hint system:

    After 3 wrong guesses: Show if number is odd/even
    After 5 wrong guesses: Show if divisible by 3 or 5
    After 7 wrong guesses: Narrow the range to 25-number window
    After 10 wrong guesses: Show first digit
    
Example 
    === Enhanced GUESSING GAME ===
    Guess my number between 1 and 100!
    You have unlimited attempts.

    Attempt 1 - Enter your guess: 10
    Too low! Try again.

    Attempt 2 - Enter your guess: 15
    Too high! Try again.

    Attempt 3 - Enter your guess: 12
    Too low! Try again.
    HINT: The number is even
    
    ...
    
    Attempt 5 - Enter your guess: 20
    Too high! Try again.
    HINT: The number is divisible by 5
    
    ...
    
    Congratulations! You won in 10 attempts!

"""

"""
#Question 2: Enhanced Guessing Game with Hints
Develop an enhanced guessing game with intelligent hint system:
Core Features:
 
Random number between 1-100
Unlimited attempts
 
Progressive hint system:
 
    After 3 wrong guesses: Show if number is odd/even
    After 5 wrong guesses: Show if divisible by 3 or 5
    After 7 wrong guesses: Narrow the range to 25-number window
    After 10 wrong guesses: Show first digit
   
Example
    === Enhanced GUESSING GAME ===
    Guess my number between 1 and 100!
    You have unlimited attempts.
 
    Attempt 1 - Enter your guess: 10
    Too low! Try again.
 
    Attempt 2 - Enter your guess: 15
    Too high! Try again.
 
    Attempt 3 - Enter your guess: 12
    Too low! Try again.
    HINT: The number is even
   
    ...
   
    Attempt 5 - Enter your guess: 20
    Too high! Try again.
    HINT: The number is divisible by 5
   
    ...
   
    Congratulations! You won in 10 attempts!
 
"""
import random
number = random.randint(1, 100)
 
def get_parity_hint(number):
    if number % 2 == 0:
        return "HINT: The number is even"
    else:
        return "HINT: The number is odd"
 
def get_divisibility_hint(number):
    if number % 3 == 0:
        return "HINT: The number is divisible by 3"
    elif number % 5 == 0:
        return "HINT: The number is divisible by 5"
    else:
        return "HINT: The number is NOT divisible by 3 or 5"
 
def get_range_hint(number, current_min=1, current_max=100):
    # Return narrowed range around the number
    current_min = max(0, current_min)
    current_max = max(0, current_max)
    return f'HINT: the Narrow the range {range(current_min, current_max)}'
   
def get_thefirst_digit_hint(number):
    return f'HINT The first digit is {number//10}'
 
def game_Random():
    i=1
    while True:
        print(f"พยายามครั้งที่ {i}")
        numbers=int(input('Enter number (1-100): '))
        if numbers < number:
            print('number is low')
        elif numbers > number:
            print('number is high')
        elif numbers == number:
            print(f'you win ')
            break
 
        if i==3:
            print(get_parity_hint(number))
        elif i==5:
            print(get_divisibility_hint(number))
        elif i==7:
            print(get_range_hint(number,number-12,number+12))
        elif i==10:
            print(get_thefirst_digit_hint(number))
        i=i+1
game_Random()
 