import random
randno = random.randint(1,100)
userguess=None
guesses = 0

while(userguess != randno):
    userguess = int (input("enter your guess\n"))
    guesses +=1
    if (userguess==randno):
        print ("your guess is right")
    elif(userguess>randno):
        print("your guess is wrong!enter a smaller number")
    else:
        print("your guess is wrong!enter a larger number")

print(f"you guessed the number in {guesses} guesses")
with open("highscore.txt","r") as f:
    highscore = int(f.read())

if (guesses<highscore):
    print ("you have just broken the highscore")
    with open ("highscore.txt","w") as f:
        f.write(str(guesses))


