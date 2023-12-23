class MapEntry:
    def __init__(self, dest_start, source_start, range):
        self.source_start = source_start
        self.range = range
        self.dest_start = dest_start

    def map(self, number):
        if number >= self.source_start and number < self.source_start + self.range:
            return (number - self.source_start) + self.dest_start
        return number

    def __lt__(self, other):
        return self.source_start < other.source_start

    def __eq__(self, other):
        return self.source_start == other.source_start

    def __repr__(self) -> str:
        return f"({self.dest_start}, {self.source_start}, {self.range})"


class Map:
    def __init__(self) -> None:
        self.entries = []

    def insert_entry(self, dest_start, source_start, range):
        self.entries.append(MapEntry(dest_start, source_start, range))

    def finalize_map(self):
        self.entries = sorted(self.entries)

    def find(self, number):
        last_entry = None
        for entry in self.entries:
            if entry.source_start > number:
                return last_entry.map(number) if last_entry else number
            last_entry = entry
        return last_entry.map(number) if last_entry else number


class ProblemInstance:
    def __init__(self) -> None:
        self.seeds = []
        self.maps = {}

    def parse_lines(self, lines):
        mode = 0
        for line in lines:
            if line.startswith("seeds: "):
                self.seeds = [int(seed)
                              for seed in line[7:].split(" ")]
            elif "map:" in line:
                mode += 1
                self.maps[mode] = Map()
            elif len(line) != 0:
                self.maps[mode].insert_entry(
                    *[int(entry) for entry in line.split(" ")])

        for map in self.maps.values():
            map.finalize_map()

    def calculate_seeds(self):
        values = []
        for seed in self.seeds:
            values.append(self.calculate_seed(seed))

        return values

    def calculate_seed(self, seed):
        for mode in sorted(self.maps.keys()):
            seed = self.maps[mode].find(seed)

        return seed


if __name__ == "__main__":
    problem = ProblemInstance()
    with open("input") as f:
        lines = [line[:-1] for line in f.readlines()]
        problem.parse_lines(lines)
        print(min(problem.calculate_seeds()))
