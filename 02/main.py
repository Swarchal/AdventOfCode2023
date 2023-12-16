import sys
from dataclasses import dataclass
from collections import defaultdict
from typing import List, Tuple


@dataclass
class Set:
    red: int = 0
    green: int = 0
    blue: int = 0

    def is_possible(self, rlim=12, glim=13, blim=14) -> bool:
        return self.red <= rlim and self.green <= glim and self.blue <= blim


@dataclass
class Game:
    id: int
    sets: List[Set]

    def is_possible(self) -> bool:
        return all(s.is_possible() for s in self.sets)

    def fewest(self) -> Tuple[int, int, int]:
        # actually max for each colour across sets
        max_cubes = defaultdict(int)
        for colour in ["red", "green", "blue"]:
            for s in self.sets:
                n_cubes = getattr(s, colour)
                if n_cubes >= max_cubes[colour]:
                    max_cubes[colour] = n_cubes
        return tuple(max_cubes.values())

    def prod_fewest(self) -> int:
        r, g, b = self.fewest()
        return r * g * b


def parse_game(line: str) -> Game:
    prefix, rest = line.split(":")
    id = int(prefix.split()[1])
    sets = parse_sets(rest.split(";"))
    return Game(id, sets)


def parse_sets(sets: List[str]) -> List[Set]:
    output = []
    for s in sets:
        this_set = Set()
        cubes = s.split(",")
        for c in cubes:
            n_cubes = get_cube_count(c)
            if c.endswith("blue"):
                this_set.blue = n_cubes
            elif c.endswith("green"):
                this_set.green = n_cubes
            elif c.endswith("red"):
                this_set.red = n_cubes
            else:
                raise ValueError(f"unknown cube {c}")
            output.append(this_set)
    return output


def get_cube_count(cube: str) -> int:
    return int(cube.split()[0])


def read_input(path: str) -> List[Game]:
    with open(path, "r") as f:
        lines = [i.strip() for i in f.readlines()]
    return [parse_game(i) for i in lines]


def part_1(games: List[Game]) -> int:
    return sum(g.id for g in games if g.is_possible())


def part_2(games: List[Game]) -> int:
    return sum(g.prod_fewest() for g in games)


def main() -> None:
    games = read_input(sys.argv[1])
    print(part_1(games))
    print(part_2(games))


if __name__ == "__main__":
    main()
