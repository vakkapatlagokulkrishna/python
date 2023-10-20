import random
user_win=0
computer_win=0
print("Hey! Welcome to Rock ,Paper and Scissor:)")
choice=["rock","paper","scissor"]


while True:
    user_choice=input("Make a choice Rock/Paper/Scissor/Quit/:").lower()
    print(user_choice)

    if user_choice=="quit":
        break

    elif user_choice not in choice:
        continue


    random_number=random.randint(0,2)
    computer_pick=choice[random_number]
    print("computer picked",computer_pick,".")


    if user_choice=="rock" and computer_pick=="scissor":
        print("Good")
        print("YOU WON!!")
        user_win+=1
        continue
    
    elif user_choice==computer_pick:
        print("you both choose the same try next time ")
        continue

    elif user_choice=="paper" and computer_pick=="rock":
        print("YOU WON!!")
        user_win+=1
        continue

    elif user_choice=="scissor" and computer_pick=="paper":
        print("YOU WON!!")
        user_win+=1
        continue

    else:
        print("YOU LOST:(")
        computer_win+=1

        print("You won ",user_win,"times.")
        print("computer won",computer_win,"times")
        print("Good bye!Have a great day:)")