import random

def create_list(players):
    finished_list = []
    recipients = players.copy()
    for player in players:
        try:
            recipients.remove(player)
            replace = True
        except:
            replace = False
        try:
            recipient = random.choice(recipients)
            finished_list.append([player, recipient])
            recipients.remove(recipient)
        except:
            recipient = finished_list[0][1]
            finished_list[0][1] = player
            finished_list.append([player, recipient])
        if replace:
            recipients.append(player)
    return finished_list

players = [
    "Fred",
    "Wilma",
    "Barney",
    "Pebbles",
    "Bam Bam"
]

random.shuffle(players)
santas = create_list(players)

for x in santas:
    print(x)
