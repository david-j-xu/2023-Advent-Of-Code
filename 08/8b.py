from math import lcm


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

    count = 0
    currentNodes = [graph.nodes[key]
                    for key in graph.nodes.keys() if key[-1:] == "A"]
    distances = []
    while currentNodes:
        move_is_left = is_left_strategy[count % len(is_left_strategy)]
        count += 1
        currentNodes = [
            graph.nodes[currentNode.left if move_is_left else currentNode.right]
            for currentNode in currentNodes
        ]

        if any([node.name[-1] == "Z" for node in currentNodes]):
            distances.append(count)
        currentNodes = [node for node in currentNodes if node.name[-1] != 'Z']

    print(lcm(*distances))
