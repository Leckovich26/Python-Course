import random

def rolldice():
    
    min=1
    max=6
    
    dice=random.randint(min,max)

    return dice

while True:

    players=input("Please type the number of players between 2 - 4: ")
    if players.isdigit():
        players=int(players)

        if 2<= players <= 4:
            break
        else:
            print("Must be between 2 - 4 players.") 

    else:
        print("Please enter a number between 2 -4 ")
    
max_score= 50

players_score= [0 for _ in range(players)]

while max(players_score) < max_score:

    for player_idx in range(players):
        print(f"\nPlayer {player_idx + 1} turn has just started!\n")
        print("Your total score is: ", players_score[player_idx], "\n")
        current_score=0

    while True:

        should_roll=input("Do you want to roll the dice? (y)")
        if should_roll.lower() != "y":
            break

        value= rolldice()
        
        if value == 1:
            print("You rolled a 1! Your turn is done!")
            current_score=0
            break
        else:
            current_score += value
            print(f"You rolled a: {value}")
        
        print(f"Your score is: {current_score}")
    
    players_score[player_idx] += current_score

    print(f"Your total score is: {players_score[player_idx]}")

max_score = max(players_score)
winning_idx= players_score.index(max_score)
print(f"Player number {winning_idx} + {1}")
