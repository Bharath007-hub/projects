import random

num = random.randrange(1, 10)
print("The number is from 1 to 10.")
guess_num = int(input("Enter your guess: "))

if guess_num > num:
    print("Your number is too high. Guess a bit lower.")
if guess_num < num:
    print("Your number is too low. Guess a bit higher.")
if guess_num == num:
    print("You got the number!")

