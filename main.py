from RPS import player
from RPS_game import play, quincy, abbey, kris, mrugesh


bots = [quincy, abbey, kris, mrugesh]

for bot in bots:
    print(f"\nPlaying against {bot.__name__}...")
    play(player, bot, 1000)
