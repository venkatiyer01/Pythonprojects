print("Welcome to my computer quiz!")

playing = input("Do you want to play or not? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's Play: )")
score = 0

answer = input('what does GPU stands for? ')
if answer.lower() == "graphics processing unit":
    print('Correct!')
    score+=1
else:
    print("Incorrect,Try again!")

answer = input('What does RAM stands for? ')
if answer.lower() == "random access memory":
        print('Correct!')
        score += 1
else:
        print("Incorrect,Try again!")

answer = input('What does PSU stands for? ')
if answer.lower() == "power supply":
            print('Correct!')
            score += 1
else:
            print("Incorrect,Try again!")

answer = input('What does CPU stands for? ')
if answer.lower() == "central processing unit":
                print('Correct!')
                score += 1
else:
                print("Incorrect,Try again!")

print("You got " + str(score) + " Questions correct")
print("You scored " + str((score/4)*100) + "%.")

