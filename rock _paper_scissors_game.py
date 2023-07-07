import random
user_wins = 0
computer_wins = 0
draw=0
option = ["rock","paper","scissors"]
while True:
    user_input = input("type ROCK/PAPER/SCISSORS or 'quit' enter q").lower()
    if user_input == 'q':
        break
    if user_input not in option:
        continue
    random_number = random.randint(0,2)
    # rock: 0 ,paper : 1,scissor:2
    computer_pick = option[random_number]
    print("computer picked ", computer_pick + ".")
    if user_input == "rock" and computer_pick == "scissors":
        print("you won!")
        user_wins += 1
    elif user_input == "scissors" and computer_pick == "paper":
        print("you won!")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("you won!")
        user_wins += 1
    elif user_input == "rock" and computer_pick == "rock":
        print("its a draw!")
        draw +=1
    elif user_input == "paper" and computer_pick == "paper":
        print("its a draw!")
        draw +=1
    elif user_input == "scissors" and computer_pick == "scissors":
        print("its a draw!")
        draw +=1
    else:
        print("you lost!")
        computer_wins +=1
print("you won!",user_wins,"times")
print("computer won!",computer_wins,"times")
print("draw!",draw,"times")
print("GOOD BYE!")