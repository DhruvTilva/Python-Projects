# *****stone,paper,ceaser game program******
# there are two players game the one of them is computer and second is  you
import random

# define function and inputs two 
def game(comp,you):
    # condition let when win and when losse with boolean with if else condition
    if comp==you:
        return None
    elif comp == "s":
        if you == "p":
            return True
        elif you == "c":
            return False
    elif comp == "p":
        if you == "s":
            return False
        elif you == "c":
            return True
    elif comp == "c":
        if you == "s":
            return False
        elif you == "p":
            return True
print("Computer Turn:  choosed one item Now It's your Turn" )
#  TO generate the random number beetween 1,2,3, write an random.randint() function with imported modules 
randNo= random.randint(1,3)
# To store value 1 as stone and 2 is paper and 3 as ceaser stored with if else condition 
if randNo == 1:
    comp = "s"
elif randNo == 2:
    comp = "p"
elif randNo == 3:
    comp = "c"
# take the input from you and print options 
you= input("Your Turn: stone(s) paper(p) ceaser(c)?")

# choosen option displayed
print(f"Computer Choosen {comp}")
print(f"You Choosen {you} ")
# If else statement on basis of function working win or looser declare 
if game(comp,you)== None:
    print("Hey Buddy there is a Tie!!")
elif game(comp,you):
    print("You Win!!!")
else:
    print("You Losse!!")
