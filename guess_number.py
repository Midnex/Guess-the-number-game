import random

name = input('Hello! What is your name?\n') # Shorter version, by including text within input().
secret_number = random.randint(1, 20)  # random integer between 1 and 20
print(f'{name} I am thinking of a number between 1 and 20')
for _ in range(6):  # the user has 6 guesses
    guess = int(input('Take a guess\n') # Shorter version, by including text within input().
    if guess > secret_number:
        print('Your guess is too high')
    elif guess < secret_number:
        print('Your guess is too low')
    else:
        break
if guess == secret_number: # condition if the user guesses right
    print(f'Good job {name} That is the number I was thinking')
else:  # condition if the user fails to guess correctly 6 times
    print(f'You are wrong the number I was thinking is {secret_number}')
