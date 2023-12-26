class GridGraph:
    def __init__(self, num_rows, num_cols) -> None:
        self.num_rows, self.num_cols = num_rows, num_cols
        self.repr = {(r, c): [] for r in range(num_rows)
                     for c in range(num_cols)}

    def in_bounds(self, r, c):
        return r >= 0 and r < self.num_rows and c >= 0 and c < self.num_cols

    def add_edge_if_possible(self, r1, c1, r2, c2):
        # adds a directed edge
        if self.in_bounds(r1, c1) and self.in_bounds(r2, c2):
            self.repr[(r1, c1)].append((r2, c2))

    def filter_to_bidirectional_edges(self):
        self.repr = {
            node: [
                neighbor for neighbor in adjacent if self.repr[neighbor].count(node)
            ] for node, adjacent in self.repr.items()
        }

    def bfs_until_connected(self, r, c):
        q = [(r, c, [])]
        visited = set()
        while q:
            r, c, path = q.pop(0)
            if (r, c) in visited:
                if (r, c) in path:
                    continue
                return len(path)

            new_path = path[:]
            new_path.append((r, c))
            visited.add((r, c))
            for new_r, new_c in self.repr[(r, c)]:
                q.append((new_r, new_c, new_path))


with open("input") as f:
    lines = [line[:-1] for line in f.readlines()]
    graph = None
    start = None
    for r, row in enumerate(lines):
        for c, char in enumerate(row):
            if not graph:
                graph = GridGraph(len(lines), len(row))
            if char == '|':
                graph.add_edge_if_possible(r, c, r - 1, c)
                graph.add_edge_if_possible(r, c, r + 1, c)
                pass
            elif char == '-':
                graph.add_edge_if_possible(r, c, r, c - 1)
                graph.add_edge_if_possible(r, c, r, c + 1)
            elif char == 'L':
                graph.add_edge_if_possible(r, c, r - 1, c)
                graph.add_edge_if_possible(r, c, r, c + 1)
            elif char == 'J':
                graph.add_edge_if_possible(r, c, r - 1, c)
                graph.add_edge_if_possible(r, c, r, c - 1)
            elif char == '7':
                graph.add_edge_if_possible(r, c, r, c - 1)
                graph.add_edge_if_possible(r, c, r + 1, c)
            elif char == 'F':
                graph.add_edge_if_possible(r, c, r, c + 1)
                graph.add_edge_if_possible(r, c, r + 1, c)
            elif char == 'S':
                start = (r, c)
                graph.add_edge_if_possible(r, c, r, c + 1)
                graph.add_edge_if_possible(r, c, r + 1, c)
                graph.add_edge_if_possible(r, c, r, c - 1)
                graph.add_edge_if_possible(r, c, r - 1, c)
    graph.filter_to_bidirectional_edges()
    print(graph.bfs_until_connected(*start))
