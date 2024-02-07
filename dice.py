import random

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def add_score(self, points):
        self.score += points

    def reset_score(self):
        self.score = 0

def roll_die():
    return random.randint(1, 6)

def take_turn(player):
    print(f"It's {player.name}'s turn.")
    input("Press Enter to roll the die...")
    roll = roll_die()
    print(f"{player.name} rolled a {roll}.")
    if roll == 1:
        print("Oops! You rolled a 1. No points this turn.")
        return 0
    else:
        return roll

def play_game(players, target_score=100):
    current_player_index = 0
    while True:
        current_player = players[current_player_index]
        turn_score = take_turn(current_player)
        if turn_score == 0:
            current_player.reset_score()
            current_player_index = (current_player_index + 1) % len(players)
        else:
            current_player.add_score(turn_score)
            print(f"{current_player.name}'s current score: {current_player.score}")
            if current_player.score >= target_score:
                print(f"Congratulations, {current_player.name} wins!")
                break
            choice = input("Do you want to roll again? (y/n): ").lower()
            if choice != 'y':
                current_player_index = (current_player_index + 1) % len(players)

if __name__ == "__main__":
    num_players = int(input("Enter the number of players: "))
    players = [Player(input(f"Enter name of player {i+1}: ")) for i in range(num_players)]
    play_game(players)
