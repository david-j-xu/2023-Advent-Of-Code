
class Node:
    def __init__(self, name, left, right) -> None:
        self.name = name
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"[{self.name}: ({self.left}, {self.right})]"


class Graph:
    def __init__(self) -> None:
        self.nodes = {}

    def enter_node(self, node):
        self.nodes[node.name] = node

    def __repr__(self) -> str:
        return f"{self.nodes}"


with open("input") as f:
    lines = [line[:-1] for line in f.readlines()]
    is_left_strategy = [char == "L" for char in lines[0]]

    graph = Graph()

    for line in lines[2:]:
        name, children = line.split(" = ")
        left, right = children[1:-1].split(", ")
        graph.enter_node(Node(name, left, right))

    startNode = "AAA"
    endNode = "ZZZ"
    count = 0

    currentNode = graph.nodes[startNode]
    while currentNode.name != endNode:
        move_is_left = is_left_strategy[count % len(is_left_strategy)]
        currentNode = graph.nodes[currentNode.left if move_is_left else currentNode.right]
        count += 1

    print(count)
