import re

def main():
    with open("day-03/input.txt", "r") as f:
        line = f.read()
        functions = re.findall(r"(don't|mul|do)\((\d+,\d+|)\)", line)
        enabled = True
        result = 0
        for f in functions:
            match f[0]:
                case "do":
                    enabled = True
                case "don't":
                    enabled = False
                case "mul":
                    if enabled:
                        num1, num2 = f[1].split(",")
                        result += int(num1) * int(num2)

        return result

if __name__ == "__main__":
    print(main())