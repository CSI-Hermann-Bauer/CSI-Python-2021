import random
#ARRAY OF CHOICES
moves = ["rock", "paper", "scissors"]
#TAKES INPUT CONVERTS IT TO INDEX
humanChoice = moves.index(input("rock, paper, scissors? "))
#RANDOM INT AS CHOICE
computerChoice = random.randint(0,2)
print(f"Computer selected: {moves[computerChoice]}")


#ROCKPAPERSCISSOR GAME LOGIC

if(humanChoice == computerChoice):
    print("Tie")
elif(humanChoice == 0 and computerChoice==2):
    print("you won")
    print(f"{moves[humanChoice]} beats {moves[computerChoice]}")

elif(humanChoice == 1 and computerChoice==0):
    print("you won")
    print(f"{moves[humanChoice]} beats {moves[computerChoice]}")

elif(humanChoice == 2 and computerChoice==1):
    print("you won")
    print(f"{moves[humanChoice]} beats {moves[computerChoice]}")

else:
    print("you lost")
    print(f"{moves[humanChoice]} looses to {moves[computerChoice]}")