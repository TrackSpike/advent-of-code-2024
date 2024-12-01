def main():
    l1, l2 = [], []
    with open("day-01/data.txt", "r") as file:
        data = file.read().splitlines()
        for line in data:
            num1, num2 = line.split()
            l1.append(int(num1))
            l2.append(int(num2))
    l1.sort()
    l2.sort()
    result = 0
    for i in range(len(l1)):
        result += abs(l1[i] - l2[i])

    return result

if __name__ == "__main__":
    main()