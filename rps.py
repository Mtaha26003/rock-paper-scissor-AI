import random

def player(prev_play, opponent_history=[]):
    # Save opponent move
    if prev_play != "":
        opponent_history.append(prev_play)

    # Counter moves
    counter = {"R": "P", "P": "S", "S": "R"}

    # First move
    if len(opponent_history) == 0:
        return "R"

    # --- Strategy 1: Pattern Detection (last 3 moves) ---
    if len(opponent_history) > 4:
        last_three = "".join(opponent_history[-3:])
        patterns = {}

        for i in range(len(opponent_history) - 3):
            seq = "".join(opponent_history[i:i+3])
            next_move = opponent_history[i+3]
            if seq == last_three:
                patterns[next_move] = patterns.get(next_move, 0) + 1

        if patterns:
            predicted = max(patterns, key=patterns.get)
            return counter[predicted]

    # --- Strategy 2: Beat most common move ---
    most_common = max(set(opponent_history), key=opponent_history.count)
    return counter[most_common]
