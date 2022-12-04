def sol1():
    file = open("input.txt", "r")
    lines = file.readlines()
    file.close()
    value = 0
    result = []

    for i in range(len(lines)):
        line = lines[i].strip("\n")
        if line != "":
            value += int(line)
        else:
            result.append(value)
            value = 0
        if i == len(lines) - 1:
            result.append(value)

    total = 0
    for i in range(3):
        total += max(result)
        result.remove(max(result))

    print(total)


if __name__ == "__main__":
    sol1()
