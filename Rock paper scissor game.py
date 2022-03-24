#Rock paper scissor game

import random

you_win=0
comp_win=0
changes=1

while True:
    comp=random.choice(["R","P","S"])
    print("What do you want to print? Enter R for Rock P for papper and S for scissor ")
    choice=input()
    choice.upper()
    if choice==comp:
        print("Computer and you chosses the same so , points goes to you both")
        comp_win=comp_win+1
        you_win=you_win+1
    elif choice=="R" and  comp=="P":
        print("Computer choose Paper, you lose!")
        comp_win=comp_win+1
    elif choice=="P" and comp=="R":
        print("computer chose Rock, You won!")
        you_win=you_win+1
    elif choice=="P" and comp=="S":
        print("Computer choose paper , you won!")
        you_win=you_win+1
    elif choice=="S" and comp=="P":
        print("Computer choose Paper , You lose!")
        comp_win=comp_win+1
    elif choice=="R" and comp=="S":
        print("Computer choose Stone, You won!")
        you_win=you_win+1
    elif choice=="S" and comp=="R":
        print("Computer choose Rock, You lose! ")
        comp_win=comp_win+1
    else:
        print("ERROR 404 SOMETHING WRONG HAPPENED ")
    changes=changes+1
    if changes>10:
        print("CHANGES ARE OVER NOW")
        break

if you_win > 5:
    print("congrats! you have won ")
    print("computer score is ", str(comp_win)+ "/10")
    print("Your score is ", str(you_win)+ "/10")
elif you_win < 5:
    print("you lose! better luck next time")
    print("computer score is ", str(comp_win) + "/10")
    print("Your score is ", str(you_win) + "/10")
else:
    print("draw between you and computer ")



