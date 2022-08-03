import random
randNumber= random.randint(1,100)
# print(randNumber)
userGuess= None
guesses= 0
while(userGuess != randNumber):
    userGuess= int(input("******Enter your Guess: "))
    guesses += 1
    if(userGuess==randNumber):
        print("You Guess it Right!")
    else:
        if(userGuess>randNumber):
            print("You Guess it Wrong! Enter Smaller Number Buddy!!!!")
        else:
            print("You Guess it Wrong! Enter Larger Number Buddy!!!!")
print(f"Your Try To Guessed Number is {guesses} guesses!!!!!!!")


# with open("hiscore.txt","r") as f:
#     hiscore= int(f.read())
# if(guesses<hiscore):
#     print(" Congretulations!!  You  Just Brake The Hiscore!!!!")
#     with open("hiscore.txt","w") as f:
#         f.write(str(guesses))
