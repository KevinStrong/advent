rules = open('day_12/rules.txt').read().splitlines()
# rules = open('day_12/testing_rules.txt').read().splitlines()

current_position = open('day_12/starting_plants.txt').readline().lower().rstrip()
# current_position = open('day_12/testing_input.txt').readline().lower().rstrip()
generations = 50000000000
index_of_zero_pot = 0

print("0: " + current_position)

padding = '....'


def print_position():
    print(str(gen) + ": " + ''.join(['.'] * (3 - index_of_zero_pot)) + current_position)


def calculate_pot_sum(current_position, index_of_zero_pot):
    sum = 0
    for pot_index in range(0, len(current_position)):
        if current_position[pot_index] == '#':
            sum += pot_index - index_of_zero_pot
    return sum

score = 0


def print_info():
    global score
    # print_position()
    previous_score = score
    score = calculate_pot_sum(current_position, index_of_zero_pot)
    if (score - previous_score == 80):
        print(str(gen) + ": " + str(score))


def add_padding(index_of_zero_pot):
    global previous_position, current_position
    if '#' in current_position[0:3]:
        previous_position = padding + current_position
        index_of_zero_pot += len(padding)
    else:
        previous_position = current_position
    if '#' in previous_position[-3:]:
        previous_position += padding
    current_position = ""
    return index_of_zero_pot


for gen in range(1, generations + 1):
    index_of_zero_pot = add_padding(index_of_zero_pot)

    for index in range(2, len(previous_position) - 2):
        this_location = previous_position[index - 2:index + 3]
        current_position += '#' if this_location in rules else '.'
    index_of_zero_pot -= 2
    print_info()

print(index_of_zero_pot)
print(calculate_pot_sum(current_position, index_of_zero_pot))
print(((50000000000 - 100) * 80) + 8000)
# 3025
# Correct answer is 3248
