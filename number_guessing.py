import random

top_of_range = input("Type a number: ")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)
else:
    print('Please type a valid number next time.')
    quit()

if top_of_range <= 0:
    print('Please type a number larger than 0 next time.')
    quit()

random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please type a valid number next time.')
        continue

    if user_guess == random_number:
        print("you got it!congratulation!")
        break
    else:
        if user_guess > random_number:
            print("you are above the number")
        else:
            print("you are lesser the number")

print("you got it in",guesses,"guesses")