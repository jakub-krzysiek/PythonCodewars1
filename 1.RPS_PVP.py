def rps(p1, p2):
    if (p1 == "scissors" and p2 == "paper") or (p1 == "paper" and p2 == "rock") or (p1 == "rock" and p2 == "scissors"):
        print("Player 1 chose " + p1 + ", Player 2 chose " + p2 + ". Player 1 won!")
    elif (p1 == "scissors" and p2 == "rock") or (p1 == "paper" and p2 == "scissors") or (p1 == "rock" and p2 == "paper"):
        print("Player 1 chose " + p1 + ", Player 2 chose " + p2 + ". Player 2 won!")
    elif p1 == p2:
        print("Both players have chosen " + p1 + ". It's a draw!")


p1 = input("Player 1, what do you choose? Pick one (rock, paper, scissors)!:")
print("\n" * 100)
p2 = input("Player 2, what do you choose? Pick one (rock, paper, scissors)!:")
rps(p1, p2)
