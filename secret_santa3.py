import random

def create_list(players):
    random.shuffle(players)
    finished_list = []
    breakpoint()
    for i, player in enumerate(players):
        finished_list.append((player, players[i -1]))
    finished_list = sorted(finished_list)
    return finished_list

players = [
    "Fred",
    "Wilma",
    "Barney",
    "Pebbles",
    "Bam Bam"
]

santas = create_list(players)

for item in santas:
    print(item[0], "-->", item[1])
