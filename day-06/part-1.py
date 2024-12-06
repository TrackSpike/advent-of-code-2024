import sys


dirs: dict[str, tuple[int, int]] = {
    "^": (-1, 0),
    ">": (0, 1),
    "<": (0, -1),
    "V": (1, 0),
}


def main():
    with open("day-06/example.txt") as f:
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
        final = step(tiles, guard)
        result = 0
        for row in final:
            for tile in row:
                if tile in ["X", "^", ">", "<", "V"]:
                    result += 1
        return result


def step(tiles: list[list[str]], pos: tuple[int, int]):
    print(debug_tiles(tiles))
    print("\n")
    row, col = pos
    if in_bounds(tiles, pos):
        dir = dirs[tiles[row][col]]
        new_pos: tuple[int, int] = (pos[0] + dir[0], pos[1] + dir[1])
        while in_bounds(tiles, new_pos) and tiles[new_pos[0]][new_pos[1]] == "#":
            tiles[row][col] = turn(tiles[row][col])
            dir = dirs[tiles[row][col]]
            new_pos: tuple[int, int] = (pos[0] + dir[0], pos[1] + dir[1])
        try:
            tiles[row][col], tiles[new_pos[0]][new_pos[1]] = (
                tiles[row][col],
                tiles[row][col],
            )
        except Exception:
            return tiles
        return step(tiles, new_pos)

    else:
        return tiles


def in_bounds(tiles: list[list[str]], pos: tuple[int, int]):
    row, col = pos
    rows, cols = len(tiles), len(tiles[0])
    return 0 <= row < rows and 0 <= col < cols


def turn(char: str):
    match char:
        case "^":
            return ">"
        case ">":
            return "V"
        case "V":
            return "<"
        case "<":
            return "^"
    raise Exception(f"Cant find {char}")


def debug_tiles(list_of_lists):
    return "\n".join("".join(inner_list) for inner_list in list_of_lists)


if __name__ == "__main__":
    sys.setrecursionlimit(300000)
    print(main())
