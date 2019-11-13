from random import randint


t = ["rock", "paper", "scissors"]

computer = t[randint(0,2)]


player = False
while player == False:

    player = input("rock, paper, scissors?")
    if player == computer:
        print("Tie!")
    elif player == "rock":
        if computer == "paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You win")
            
    elif player == "paper":
        if computer =="scissors":
            print("NOO You Lose")
        else:
            print("you win")
    elif player == "scissors":
        if computer == "rock":
            print("Noo You Lose")
        else:
            print("You Win, Gz")
    else:
        print("That's not a valid play. Check your spelling!")
    player = input("Type Y/N ")
    if player == "Y":
        player = False
        computer = t[randint(0,2)]
    elif player == "N":
        exit()
    else:
        print("inv")
    
    