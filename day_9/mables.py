players = 491
# last_marble = 71058  # Part 1
last_marble = 7105800  # Part 2
# players = 9
# last_marble = 25
special_interval = 23

current_player = 1
active_marble = 0
player_score = {}
marbles = [0]


def add_marble(marble):
    marbles.insert(increment_active_marble(2), marble)


def increment_active_marble(amount):
    global active_marble
    active_marble = (active_marble + len(marbles) + amount) % (len(marbles))
    if active_marble == 0:
        active_marble = len(
            marbles)  # Marbles between the beginning and end of the list go at the end.  This is to match example.
    return active_marble


def special_add_marble(marble):
    if current_player in player_score:
        player_score[current_player] += marble
    else:
        player_score[current_player] = marble
    global active_marble
    player_score[current_player] += marbles.pop(increment_active_marble(-7))


def next_player():
    global current_player
    current_player += 1
    if current_player > players:
        current_player = 1


for marble in range(1, last_marble + 1):
    print("Marble Number: " + str(marble))
    if marble % 23 == 0:
        special_add_marble(marble)
    else:
        add_marble(marble)
    next_player()

print("Maximum player score is: " + str(max(player_score.values())))

number = 0
