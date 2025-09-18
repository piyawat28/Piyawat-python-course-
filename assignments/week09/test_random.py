import random

def test_random():
    random_number = random.randint(1, 10)
    
    guess_number = int(input("what is your guess number (1-20)?:"))

    if test_random == guess_number:
        print("เจ๋งแจ๋ว")
    elif guess_number < test_random:
         print("มั่วจ้า น้อยไปน้า")
    elif guess_number > test_random:
         print("มั่วจ้า มากไปปหน่อย")
test_random()