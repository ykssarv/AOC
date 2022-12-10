

def sol1():
    file = open("input.txt", "r")
    line = file.readline()
    file.close()
    four = set()
    count = 0
    i = 0

    while i < len(line):
        if i < len(line) - 4:
            four.add(line[i])
            four.add(line[i + 1])
            four.add(line[i + 2])
            four.add(line[i + 3])
            if len(four) == 4:
                count = i + 4
                break
        four = set()
        i += 1

    print(count)


def sol2():
    file = open("input.txt", "r")
    line = file.readline()
    file.close()
    fourteen = set()
    count = 0
    i = 0

    while i < len(line):
        if i < len(line) - 14:
            for j in range(14):
                fourteen.add(line[i + j])
            if len(fourteen) == 14:
                count = i + 14
                break
        fourteen = set()
        i += 1

    print(count)


if __name__ == "__main__":
    sol1()
    sol2()


