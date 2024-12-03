import re

def main():
    with open("day-03/data.txt", "r") as f:
        return sum([int(x[0]) * int(x[1]) for x in re.findall(r"mul\((\d+),(\d+)\)", f.read())
])

if __name__ == "__main__":
    print(main())