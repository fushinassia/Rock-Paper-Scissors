import random
options=["rock", "scissor", "paper"]
isrunning=True
while isrunning:
    computer = random.choice(options)
    player=input("Enter option: rock, scissor, paper:")
    while player!="scissor" and player!="paper" and player!="rock":
        print("Enter ONLY between rock, scissor and paper")
        player = input("Enter option: rock, scissor, paper:")
    print(f"Computer chose: {computer}")
    if player==computer:
        print("Tie")
    elif player=="scissor":
       if computer=="rock":
        print("Computer wins")
       else:
          print("You win")

    else:
        if computer == "rock":
            print("You win")
        else:
           print("Computer wins")
    play_again=input("do you want to play again? (Y/N/y/n):")
    if play_again!="y" and play_again!="Y":
        isrunning=False