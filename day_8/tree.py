from day_8.node import create_node

# For Diagnostic purposes.
# tree_input_full = list(map(int, open("day_8/input.txt").read().split(' ')))
tree_input = list(map(int, open("day_8/input.txt").read().split(' ')))

result = create_node(tree_input)
node = result[0]


def sum_metadata():
    metadata_sum = 0
    children_to_sum = [node]
    while children_to_sum:
        current_node = children_to_sum[0]
        children_to_sum.remove(current_node)
        metadata_sum += sum(current_node.metadata)
        children_to_sum += current_node.children
    print(metadata_sum) # 40984


sum_metadata()


def calculate_node_value(a_node):
    value = 0;
    if not a_node.children:
        value = sum(a_node.metadata)
    else:
        for i in a_node.metadata:
            if 0 < i <= len(a_node.children):
                value += calculate_node_value(a_node.children[i-1])
    return value


print(calculate_node_value(node))

number = 0
