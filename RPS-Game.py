import random  #random-module
import sys    #sys module
from enum import Enum    #enum data type

class RPS(Enum):
    ROCK=1
    PAPER=2
    SCISSORS=3


player_choice=input("Enter 1 For Rock:\n2 For Paper\n3 for scissors")   #get a input from the user


player=int(player_choice)   #convert a user input str to int

computer_choice=random.choice("123")

computer=int(computer_choice)    #convert a computer choice str to int

if player<1 or player>3:
    sys.exit("You Must Enter A Number Between 1 to 3")

print("You Chooose"+str(RPS(player)).replace("RPS","")+".")
print("Computer Choose"+str(RPS(computer)).replace("RPS"," ")+".")

if player==1 and computer==2:
    print("You Won")
elif player==2 and computer==1:
    print("You Won")
elif player==3 and computer==2:
    print("You Won")
elif player==computer:
    print("Tie")    
else:
    print("Computer Won")            


