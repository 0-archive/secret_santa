import random

players = [
    "Fred",
    "Wilma",
    "Barney",
    "Pebbles",
    "Bam Bam"]

random.shuffle(players)

for i, player in enumerate(players):
    print(str(players[i]), "-->" , str(players[i-1]))

