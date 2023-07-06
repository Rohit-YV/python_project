print("welcome to my computer quiz!")
playing = input("do you want to play? ")

if playing.lower() != "yes":
        quit()
print("okay! let's play :) ")
score = 0
answer = input("what does cpu stands for ? ")
if answer.lower() == "central processing unit":
    print('CORRECT!')
    score +=1
else:
    print('INCORRECT')
answer = input("what does GPU stands for ? ")
if answer.lower() == "graphical processing unit":
    print('CORRECT!')
    score += 1
else:
    print('INCORRECT')
answer = input("what does psu stands for ? ")
if answer.lower() == "power supply":
    print('CORRECT!')
    score += 1
else:
    print('INCORRECT')
answer = input("what does ram stands for ? ")
if answer.lower() == "random access memory":
    print('CORRECT!')
    score += 1
else:
    print('INCORRECT')
print("you got "+ str(score)+ "question correct!")
print("you got "+ str((score / 4) *100) + "%.")