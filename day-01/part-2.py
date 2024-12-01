from collections import Counter

def main():
    l1, l2 = [], []
    with open('day-01/data.txt', "r") as file:
        lines = file.read().splitlines()
        for line in lines:
            num1, num2 = line.split()
            l1.append(int(num1))
            l2.append(int(num2))
    
    counter = Counter(l2)
    result = 0
    for num in l1:
        result += num * counter[num]
    
    return result



if __name__ == '__main__':
    print(main())