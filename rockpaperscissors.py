import random


def get_choices():
    player_choice = input("enter a choice(rock, paper, scissors): ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices    


def check_win(player, computer):
    print(f"You chose {player} , computer chose {computer}")
    if player == computer:
        return "TIE!"
    
    elif player == "rock" :
        if computer == "scissors":
            return "ROCK SMASHES SCISSORS, YOU WIN!!"
        else:                   #condition for if comp= rock already done at the top w TIE 
            return "PAPER COVERS ROCK, YOU LOSE :( )"

    elif player == "paper" :
        if computer == "ROCK":
            return "PAPER COVERS ROCK, YOU WIN!!"
        else:
            return "SCISSORS CUT PAPER, YOU LOSE :( )"

    elif player == "scissors" :
        if computer == "paper":
            return "SCISSORS CUT PAPER, YOU WIN!!"
        else:
            return "ROCK SMASHES SCISSORS, YOU LOSE :( )"


choices = get_choices()

result = check_win(choices["player"], choices["computer"])
print(result)
