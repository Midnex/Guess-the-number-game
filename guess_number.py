import random

print('Hello! What is your name?')
name = input()  # string input from user
secretNumber = random.randint(1, 20)  # random integer between 1 and 20
print(f"{name} I am thinking of a number between 1 and 20")
for GuessesTaken in range(1, 7):  # the user has 6 guesses
    print('Take a guess.')
    guess = int(input())
    if guess > secretNumber:
        print('Your guess is too high')
    elif guess < secretNumber:
        print('Your guess is too low')
    else:
        break
if guess == secretNumber: # condition if the user guesses right
    print(f"Good job {name} That is the number I was thinking")
else:  # condition if the user fails to guess correctly 6 times
    print('You are wrong the number I was thinking is {0}'.format(str(secretNumber)))
