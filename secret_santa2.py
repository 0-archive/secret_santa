import random

def create_list(players):
    random.shuffle(players)
    recipients = players.copy()
    recipients.append(recipients.pop(0))
    finished_list = sorted(list(zip(players, recipients)))
    return finished_list

players = [
    "Fred",
    "Wilma",
    "Barney",
    "Pebbles",
    "Bam Bam",
    "Steven"
    ]

santas = create_list(players)

for item in santas:
    print(item[0], "-->", item[1])
