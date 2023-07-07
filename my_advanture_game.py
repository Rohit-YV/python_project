name = input("what is your name? ")
print("welcome",name,"to my adventure game")
answer= input("you are in a dirt road,it comes to an end and you can go (left or right)?").lower()
if answer == "left":
    answer=input("you come to the river, you walk around it or (swim/cross) ?").lower()
    if answer == "swim":
        print("you swam across and were eaten by alligator.")
    if answer == "road":
        print("you walked many miles,ran out of water and you lost the game!")
elif answer == "right":
    answer =input("you come to the bridge,it looks woodly,do you want to cross it or go back('cross/back')? ").lower()
    if answer == "back":
        print("you go back to the road and you loose!")
    if answer == "cross":
        answer = input("you crossed the bridge and meet a stranger.DO you want to talk to the stranger(YES/NO)? ").lower()
        if answer == "yes":
            print("you cross the jungle safly !Now you came to the next stage!")
        if answer == "no":
            print("you did't talk to the stranger and lost into the jungle and eaten by animals")
    else:
            print("not a valid option. you lose.")
else:
    print("not a valid option. you lose.")
print("thanks for playing my game")