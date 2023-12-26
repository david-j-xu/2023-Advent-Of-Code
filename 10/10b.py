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
        path_sets = {node: None for node in self.repr.keys()}
        while q:
            r, c, path = q.pop(0)
            if (r, c) in visited:
                if (r, c) in path:
                    continue
                path.extend(path_sets[(r, c)])
                return sorted(path)

            new_path = path[:]
            new_path.append((r, c))
            path_sets[(r, c)] = new_path
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
    path = set(graph.bfs_until_connected(*start))

    start_r, start_c = start
    if lines[start_r - 1][start_c] in "F|7" and lines[start_r + 1][start_c] in "J|L":
        lines[start_r] = lines[start_r].replace("S", "|")
    elif lines[start_r - 1][start_c] in "F|7" and lines[start_r][start_c + 1] in "J7-":
        lines[start_r] = lines[start_r].replace("S", "L")
    elif lines[start_r - 1][start_c] in "F|7" and lines[start_r][start_c - 1] in "F-L":
        lines[start_r] = lines[start_r].replace("S", "J")
    elif lines[start_r + 1][start_c] in "J|L" and lines[start_r][start_c - 1] in "F-L":
        lines[start_r] = lines[start_r].replace("S", "7")
    elif lines[start_r + 1][start_c] in path and lines[start_r][start_c + 1] in "J7-":
        lines[start_r] = lines[start_r].replace("S", "F")
    elif lines[start_r][start_c - 1] in "F-L" and lines[start_r - 1][start_c + 1] in "J7-":
        lines[start_r] = lines[start_r].replace("S", "-")

    area = 0
    for r in range(graph.num_rows):
        in_shape = False
        on_shape = False
        on_corner = None
        for c in range(graph.num_cols):
            if (r, c) in path:
                if lines[r][c] in "|F7JL":
                    if lines[r][c] == "|":
                        in_shape = not in_shape
                    elif lines[r][c] in "FL":
                        # left hand side
                        on_corner = lines[r][c]
                    elif (lines[r][c] == "J" and on_corner == "F") or (lines[r][c] == "7" and on_corner == "L"):
                        # staircase guys
                        in_shape = not in_shape
                on_shape = True
            else:
                on_shape = False
                if in_shape:
                    area += 1

print(area)
