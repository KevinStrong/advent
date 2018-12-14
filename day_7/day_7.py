def build_eligible_moves(instructions, completed_moves, moves_remaining):
    eligible_moves = []
    for move in moves_remaining:
        move_has_dependency = False
        for instruction in instructions:
            if instruction[1] == move and instruction[0] not in completed_moves:
                move_has_dependency = True
        if not move_has_dependency:
            eligible_moves.append(move)
    return eligible_moves


def make_move(eligible_moves):
    list.sort(eligible_moves)
    return eligible_moves[0]


def get_all_moves(instructions):
    all_moves = set()
    for instruction in instructions:
        all_moves.add(instruction[0])
        all_moves.add(instruction[1])
    return all_moves


instructions = []
for instruction in open("day_7/instructions.txt").read().splitlines():
    instructions.append(instruction.split('->'))

potential_moves = get_all_moves(instructions)
completed_moves = []
valid_moves = build_eligible_moves(instructions, completed_moves, potential_moves)

while valid_moves:
    next_move = make_move(valid_moves)
    potential_moves.remove(next_move)
    completed_moves.append(next_move)
    print(next_move)
    valid_moves = build_eligible_moves(instructions, completed_moves, potential_moves)

print('[%s]' % ', '.join(completed_moves))
number = 0
