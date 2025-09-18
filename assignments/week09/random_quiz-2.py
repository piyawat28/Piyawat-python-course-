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
    return f"HINT: The narrowed range{range(current_min,current_max)}"
    

def get_thefirst_digit_hint(number):
    return f"HINT: The first digit of number is {number//10}"
    # Retun the first digit of the number

    
import random

test_radom = random.randiant(1,21)

print("-- เกมทายตัวเลข มาเดาใจคอมพิ้วเตอร์กันเถอะ --")
print("-- ทายเลขจำนวนเต็มตั้งแต่ --")
print("-- คุณมีโอกาส unlimited --")

i=0

while True:

    print(f"ความพยามยามครั้งที่ {i+1}")
    guess_number = int(input("what is your guess number (1-100)?:"))

    if test_random == guess_number:
         print("เจ๋งแจ๋ว")
         break
    elif guess_number < test_random:
         print("มั่วจ้า น้อยไปน้า")
    elif guess_number > test_random:
         print("มั่วจ้า มากไปปหน่อย")

         if i ==3:
             get_parity_hint(test_random)
        
    elif i == 5:
            get_divisibility_hint(test_random)
    elif i == 7:
            get_range_hint(test_random,test_random-12,test_random+12)
    elif i == 10:
            get_thefirst_digit_hint(test_random)

    i = i + i