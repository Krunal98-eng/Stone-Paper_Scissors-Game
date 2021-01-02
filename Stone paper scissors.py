###Game of stone paper scissors###

import random
list = ["stone","paper","scissors"]

user_count = 0
computer_count = 0
n = 0

while(n<10):

    computer_choice =random.choice(list)
    user_choice = input("Enter your choice from stone,paper,scissors\n")
    if (computer_choice=="stone"  and user_choice=="paper"):
        print("You won")
        user_count+=1
    elif(computer_choice=="stone"  and user_choice=="scissor"):
        print("Computer won")
        computer_count+=1
    elif(computer_choice=="paper"  and user_choice=="stone"):
        print("Computer won")
        computer_count+=1
    elif(computer_choice=="paper"  and user_choice=="scissors"):
        print("You won")
        user_count+=1
    elif(computer_choice=="scissor"  and user_choice=="stone"):
        print("You won")
        user_count+=1
    elif(computer_choice=="scissor"  and user_choice=="paper"):
        print("Computer  won")
        computer_count+=1
    else:
        print("Match Draw")
    n= n + 1
if __name__ == '__main__':

 if computer_count>>user_count:
    print(f"Computer score  ({computer_count})  and user score  ({user_count})\n")
    print("Computer won")
 elif computer_count==user_count:
    print("Final Scores Are Equal Try Your luck again")

else:
    print(f"User score  ({user_count})  and computer score  ({computer_count})\n")
    print("User won")

