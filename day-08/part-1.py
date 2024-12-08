from collections import defaultdict
from typing import TypeVar

type Point = tuple[int, int]
T = TypeVar("T")


def main():
    with open("day-08/data.txt") as f:
        lines = f.read().splitlines()
        rows, cols = len(lines), len(lines[0])
        mapping: defaultdict[str, list[Point]] = defaultdict(list)
        for row in range(rows):
            for col in range(cols):
                char = lines[row][col]
                if char != ".":
                    mapping[char].append((row, col))

    marked: list[list[str]] = [["."] * cols for _ in range(rows)]
    for key in mapping.keys():
        for a, b in combination(mapping[key]):
            a_diff, b_diff = dist(b, a), dist(a, b)
            a_node, b_node = (
                (a[0] + a_diff[0], a[1] + a_diff[1]),
                (b[0] + b_diff[0], b[1] + b_diff[1]),
            )
            if in_bounds(a_node, rows, cols):
                marked[a_node[0]][a_node[1]] = "#"
            if in_bounds(b_node, rows, cols):
                marked[b_node[0]][b_node[1]] = "#"

    print_debug(marked)
    count = 0
    for line in marked:
        for ele in line:
            if ele == "#":
                count += 1

    return count


def dist(a: Point, b: Point) -> Point:
    return (b[0] - a[0], b[1] - a[1])


def in_bounds(p: Point, rows: int, cols: int) -> bool:
    return 0 <= p[0] < rows and 0 <= p[1] < cols


def combination(l: list[T]) -> list[tuple[T, T]]:
    result = []
    for i in range(len(l) - 1):
        for j in range(i + 1, len(l)):
            result.append((l[i], l[j]))

    return result


def print_debug(l: list[list[str]]):
    for row in l:
        print("".join(row))


if __name__ == "__main__":
    print(main())
