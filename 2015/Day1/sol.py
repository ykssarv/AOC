def sol1():
    file = open("input.txt", "r")
    text = file.readlines()
    file.close()
    floor = 0

    for ch in text[0]:
        if ch == "(":
            floor += 1
        else:
            floor -= 1

    print(floor)


def sol2():
    file = open("input.txt", "r")
    text = file.readlines()
    file.close()

    floor = 0
    count = 0

    for ch in text[0]:
        count += 1
        if ch == "(":
            floor += 1
        else:
            floor -= 1
            if floor == -1:
                print(count)
                return


if __name__ == "__main__":
    sol1()
    sol2()
