def main():
    with open("day-07/example.txt") as f:
        data = [
            [int(x.replace(":", "")) for x in line.split()]
            for line in f.read().splitlines()
        ]

        answer_total = 0

        for eq in data:
            target = eq[0]

            for operators in generate_permutation([], len(eq) - 2, ["+", "*"]):
                total = eq[1]
                for num, operator in zip(eq[2:], operators):
                    match operator:
                        case "+":
                            total += num
                        case "*":
                            total *= num
                if total == target:
                    answer_total += eq[0]
                    break

        return answer_total


def generate_permutation(
    cur: list[str], left: int, candidates: list[str]
) -> list[list[str]]:
    if not left:
        return [cur]
    else:
        result = []
        for c in candidates:
            result.extend(generate_permutation(cur + [c], left - 1, candidates))

        return result


if __name__ == "__main__":
    print(main())
