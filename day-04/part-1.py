key = "XMAS"
directions = [
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 1),
    (1, 1),
    (1, -1),
    (-1, -1),
]


def main():
    found = 0

    def dfs(lines: list[str], row: int, col: int, index: int, dir: tuple[int, int]):
        nonlocal found
        width, height = len(lines[0]), len(lines)
        if 0 <= row < height and 0 <= col < width:
            if lines[row][col] == key[index]:
                if index == len(key) - 1:
                    found += 1
                else:
                    dfs(lines, row + dir[1], col + dir[0], index + 1, dir)

    with open("day-04/data.txt", "r") as f:
        lines = [line.strip() for line in f.readlines()]
        width, height = len(lines[0]), len(lines)
        for col in range(width):
            for row in range(height):
                for dir in directions:
                    dfs(lines, row, col, 0, dir)

    return found


if __name__ == "__main__":
    print(main())
