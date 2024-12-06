from collections import defaultdict
import sys
import copy


dirs: dict[str, tuple[int, int]] = {
    "^": (-1, 0),
    ">": (0, 1),
    "<": (0, -1),
    "v": (1, 0),
}


def main():
    with open("day-06/data.txt") as f:
        tiles = [list(line) for line in f.read().splitlines()]
        # Find Guard
        rows, cols = len(tiles), len(tiles[0])
        guard: tuple[int, int] | None = None
        for row in range(rows):
            for col in range(cols):
                if tiles[row][col] == "^":
                    guard = (row, col)
                    break
        if not guard:
            raise Exception("No guard found")
        sol = Solution(tiles, guard)
        sol.solve()
        return len(sol.found) - 1


class Solution:
    def __init__(self, tiles: list[list[str]], guard_pos: tuple[int, int]) -> None:
        self.tiles = tiles
        self.pos = guard_pos
        self.dir = "^"
        self.found = {guard_pos}
        self.history: defaultdict[tuple[int, int], set[str]] = defaultdict(set)

    def solve(self):
        count = 0
        for row in range(len(self.tiles)):
            for col in range(len(self.tiles[0])):
                tiles_copy = copy.deepcopy(self.tiles)
                tiles_copy[row][col] = "#"
                if self.does_loop(tiles_copy, self.pos, self.dir, defaultdict(set)):
                    count += 1
                    print(count)
        return count

    def does_loop(
        self,
        tiles: list[list[str]],
        pos: tuple[int, int],
        dir: str,
        history: defaultdict[tuple[int, int], set],
    ) -> bool:
        history[pos].add(dir)
        dir_values = dirs[dir]
        new_pos: tuple[int, int] = (pos[0] + dir_values[0], pos[1] + dir_values[1])
        if not self.in_bounds(tiles, new_pos):
            return False
        if dir in history[new_pos]:
            return True
        if tiles[new_pos[0]][new_pos[1]] == "#":
            dir = self.turn(dir)
            return self.does_loop(tiles, pos, dir, history)
        return self.does_loop(tiles, new_pos, dir, history)

    def turn(self, char: str):
        match char:
            case "^":
                return ">"
            case ">":
                return "v"
            case "v":
                return "<"
            case "<":
                return "^"
        raise Exception(f"Cant find {char}")

    def debug_tiles(self):
        return "\n".join("".join(inner_list) for inner_list in self.tiles)

    def in_bounds(self, tiles: list[list[str]], pos: tuple[int, int]):
        row, col = pos
        rows, cols = len(tiles), len(tiles[0])
        return 0 <= row < rows and 0 <= col < cols


if __name__ == "__main__":
    # Not proud of this :) next time ill use an inter pattern
    sys.setrecursionlimit(1000000)
    print(main())
