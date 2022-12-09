

def sol1():
    file = open("input.txt", "r")
    lines = file.readlines()
    file.close()
    overlap = 0

    for line in lines:
        line = line.strip("\n").split(",")
        line1 = line[0].split("-")
        line2 = line[1].split("-")
        a1 = int(line1[0])
        a2 = int(line1[1])
        b1 = int(line2[0])
        b2 = int(line2[1])
        if a1 <= b1 and a2 >= b2 or b1 <= a1 and b2 >= a2:
            overlap += 1
    print(overlap)


def sol2():
    file = open("input.txt", "r")
    lines = file.readlines()
    file.close()
    overlap = 0

    for line in lines:
        line = line.strip("\n").split(",")
        line1 = line[0].split("-")
        line2 = line[1].split("-")
        print(line1)
        print(line2)
        a1 = int(line1[0])
        a2 = int(line1[1])
        b1 = int(line2[0])
        b2 = int(line2[1])
        if a1 < b1 and a2 < b1 or b1 < a1 and b2 < a1:
            continue
        else:
            overlap += 1
        print(overlap)


if __name__ == "__main__":
    sol1()
    sol2()
