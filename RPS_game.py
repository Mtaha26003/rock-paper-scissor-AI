import random

#  Bots 
def quincy(prev_play, opponent_history=[]):
    moves = ["R", "P", "S"]
    return moves[len(opponent_history) % 3]

def abbey(prev_play, opponent_history=[]):
    if prev_play == "":
        return "R"
    return prev_play

def kris(prev_play, opponent_history=[]):
    pattern = ["R", "R", "S"]
    return pattern[len(opponent_history) % 3]

def mrugesh(prev_play, opponent_history=[]):
    return random.choices(["R", "P", "S"], weights=[1, 6, 1])[0]

# Game Engine 
def play(player1, player2, num_games=1000, verbose=False):
    score1 = 0
    score2 = 0
    wins = {"R": "S", "S": "P", "P": "R"}

    p1_history = []
    p2_history = []

    for i in range(num_games):
        move1 = player1(p2_history[-1] if p2_history else "", p2_history)
        move2 = player2(p1_history[-1] if p1_history else "", p1_history)

        p1_history.append(move1)
        p2_history.append(move2)

        if move1 == move2:
            winner = "Tie"
        elif wins[move1] == move2:
            winner = "Player1"
            score1 += 1
        else:
            winner = "Player2"
            score2 += 1

        if verbose:
            print(f"Game {i+1}: {move1} vs {move2} → {winner}")

    print(f"Final Score → Player1: {score1}, Player2: {score2}")
    print(f"Player1 Win %: {score1/num_games*100:.2f}%")
    return score1/num_games*100
