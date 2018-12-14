from day_5.stack import Stack

full_polymer = [*open("full_polymer.txt").read().strip()]

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'j', 'i', 'j','k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def process_polymer(polymer):
    processed_polymer = Stack()
    for char in polymer:
        if processed_polymer.isEmpty():
            processed_polymer.push(char)
        else:
            current_top = processed_polymer.peek()
            if current_top != char and current_top.upper() == char.upper():
                processed_polymer.pop()
            else:
                processed_polymer.push(char)
    return processed_polymer.items


def remove_letter(a_full_polymer, a_letter):
    return list(filter(lambda a: a != a_letter.lower() and a != a_letter.upper(), a_full_polymer.copy()))
    # return [c for c in a_full_polymer if c != a_letter.lower() and c != a_letter.upper()]


full_polymer = process_polymer(full_polymer)
altered_polymers = {}
shortest_polymer = ['a', 1e10]
for letter in letters:
    altered_polymer = remove_letter(full_polymer, letter)
    altered_polymer = process_polymer(altered_polymer)
    altered_polymers[letter] = altered_polymer
    if shortest_polymer[1] > len(altered_polymer):
        shortest_polymer = letter, len(altered_polymer)

number = 0
# shortest_polymer = ['s', 11102]
