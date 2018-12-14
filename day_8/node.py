def create_node(note_data):
    number_of_children = note_data[0]
    children_and_remaining_input = generate_children(number_of_children, note_data[2:])

    number_of_metadata = note_data[1]
    children = children_and_remaining_input[0]
    metadata = children_and_remaining_input[1][:number_of_metadata]
    node = Node(number_of_children, number_of_metadata, children, metadata)

    remaining_input = children_and_remaining_input[1][number_of_metadata:]
    return node, remaining_input


def generate_children(number_of_children, node_data):
    children = []
    for _ in range(0, number_of_children):
        node_and_remaining_input = create_node(node_data)
        children.append(node_and_remaining_input[0])
        node_data = node_and_remaining_input[1]
    return children, node_data


class Node:

    def __init__(self, number_of_children, number_of_metadata, children, metadata):
        self.number_of_children = number_of_children
        self.number_of_metadata = number_of_metadata
        self.children = children
        self.metadata = metadata
