class Range:
    def __init__(self, start, end) -> None:
        self.start = start
        self.end = end

    def __lt__(self, other):
        return self.start < other.start

    def __eq__(self, other):
        return self.start == other.start

    def __repr__(self) -> str:
        return f"[{self.start}, {self.end}]"


class MapEntry:
    def __init__(self, dest_start, source_start, range):
        self.source_start = source_start
        self.start = source_start
        self.end = source_start + range - 1
        self.range = range
        self.dest_start = dest_start

    def map_number(self, number):
        if number >= self.source_start and number < self.source_start + self.range:
            return (number - self.source_start) + self.dest_start
        return number

    def map_range(self, range):
        return Range(self.map_number(range.start), self.map_number(range.end))

    def __lt__(self, other):
        return self.source_start < other.source_start

    def __eq__(self, other):
        return self.source_start == other.source_start

    def __repr__(self) -> str:
        return f"({self.start}, {self.end}) -> ({self.dest_start}, {self.dest_start + self.range - 1})"


class Map:
    def __init__(self) -> None:
        self.entries = []

    def insert_entry(self, dest_start, source_start, range):
        self.entries.append(MapEntry(dest_start, source_start, range))

    def finalize_map(self):
        self.entries = sorted(self.entries)

    def find_list(self, ranges):
        find_results = []
        for range in ranges:
            find_results.extend(self.find(range))

        return find_results

    def find(self, map_range):
        mapped_ranges = []
        to_mapped_ranges = []
        for entry in self.entries:
            if (entry.end >= map_range.start and entry.end <= map_range.end) or \
                (entry.start >= map_range.start and entry.start <= map_range.end) or \
                    (entry.start <= map_range.start and entry.end >= map_range.end):
                new_mapped_range = Range(
                    max(entry.start, map_range.start), min(entry.end, map_range.end))
                mapped_ranges.append(new_mapped_range)
                new_to_mapped_range = entry.map_range(new_mapped_range)
                to_mapped_ranges.append(new_to_mapped_range)

        mapped_ranges = sorted(mapped_ranges)
        min_range_start = None
        max_range_end = None

        for mapped_range in mapped_ranges:
            if min_range_start is None or mapped_range.start < min_range_start:
                min_range_start = mapped_range.start
            if max_range_end is None or mapped_range.end > max_range_end:
                max_range_end = mapped_range.end

        if min_range_start is None:
            return [map_range]

        if map_range.start < min_range_start:
            to_mapped_ranges.append(
                Range(map_range.start, min_range_start - 1))
        if map_range.end > max_range_end:
            to_mapped_ranges.append(Range(max_range_end + 1, map_range.end))

        for i in range(len(mapped_ranges) - 1):
            lower_range = mapped_ranges[i]
            upper_range = mapped_ranges[i + 1]

            if lower_range.end + 1 < upper_range.start:
                to_mapped_ranges.append(
                    Range(lower_range.end + 1, upper_range.start - 1)
                )

        return sorted(to_mapped_ranges)


class ProblemInstance:
    def __init__(self) -> None:
        self.seeds = []
        self.maps = {}

    def parse_lines(self, lines):
        mode = 0
        for line in lines:
            if line.startswith("seeds: "):
                seed_ints = [int(seed)
                             for seed in line[7:].split(" ")]

                for i in range(len(seed_ints) // 2):
                    self.seeds.append(
                        Range(seed_ints[2 * i], seed_ints[2 * i] + seed_ints[2 * i + 1] - 1))
            elif "map:" in line:
                mode += 1
                self.maps[mode] = Map()
            elif len(line) != 0:
                self.maps[mode].insert_entry(
                    *[int(entry) for entry in line.split(" ")])

        for map in self.maps.values():
            map.finalize_map()

    def calculate_seeds(self):
        return self.calculate_seed(self.seeds)

    def calculate_seed(self, seeds):
        for mode in sorted(self.maps.keys()):
            seeds = self.maps[mode].find_list(seeds)

        return seeds


if __name__ == "__main__":
    problem = ProblemInstance()
    with open("input") as f:
        lines = [line[:-1] for line in f.readlines()]
        problem.parse_lines(lines)
        print(min(problem.calculate_seeds()).start)
