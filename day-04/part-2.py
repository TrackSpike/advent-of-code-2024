def main():
    found = 0
    with open("day-04/input.txt", "r") as f:
        lines = [line.strip() for line in f.readlines()]
        for col in range(1, len(lines[0]) - 1):
            for row in range(1, len(lines) - 1):
                if lines[col][row] == "A":
                    tl, tr, bl, br = (
                        lines[col - 1][row - 1],
                        lines[col + 1][row - 1],
                        lines[col - 1][row + 1],
                        lines[col + 1][row + 1],
                    )
                    if (tl == "M" and br == "S" or tl == "S" and br == "M") and (
                        tr == "M" and bl == "S" or tr == "S" and bl == "M"
                    ):
                        found += 1

    return found


if __name__ == "__main__":
    print(main())
