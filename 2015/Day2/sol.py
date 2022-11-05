def sol1():
    file = open("input.txt", "r")
    presents = file.readlines()
    file.close()
    total = 0
    for present in presents:
        dimensions = present.split("\n")[0].split("x")
        a = 2 * int(dimensions[0]) * int(dimensions[1])
        b = 2 * int(dimensions[0]) * int(dimensions[2])
        c = 2 * int(dimensions[1]) * int(dimensions[2])
        extra = min(a, b, c) / 2
        total += a + b + c + extra

    print(total)

def sol2():
    file = open("input.txt", "r")
    presents = file.readlines()
    file.close()
    total = 0
    for present in presents:
        dimensions = present.split("\n")[0].split("x")
        a = 2 * (int(dimensions[0]) + int(dimensions[1]))
        b = 2 * (int(dimensions[0]) + int(dimensions[2]))
        c = 2 * (int(dimensions[1]) + int(dimensions[2]))
        total += min(a, b, c) + int(dimensions[0]) * int(dimensions[1]) * int(dimensions[2])

    print(total)

if __name__ == "__main__":
    sol1()
    sol2()
