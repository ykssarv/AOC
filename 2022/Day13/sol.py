

def sol1():
    file = open("input.txt", "r")
    lines = file.readlines()
    file.close()
    total = 0

    for i in range(0, len(lines), 3):
        left = eval(lines[i].strip("\n"))
        right = eval(lines[i + 1].strip("\n"))
        if compare(left, right) < 0:
            total += i // 3 + 1
    print(total)


def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        return left - right
    if isinstance(left, list) and isinstance(right, list):
        if len(left) == 0 and len(right) == 0:
            return 0
        if len(left) == 0:
            return -1
        if len(right) == 0:
            return 1
        result = compare(left[0], right[0])
        if result == 0:
            return compare(left[1:], right[1:])
        return result
    if isinstance(left, int):
        return compare([left], right)
    return compare(left, [right])


def sol2():
    file = open("input.txt", "r")
    lines = file.readlines()
    file.close()
    total = 0
    ordered = [[[2]], [[6]]]

    for i in range(len(lines)):
        if lines[i] == "\n":
            continue
        line = eval(lines[i].strip("\n"))
        for j in range(len(ordered)):
            if compare(ordered[j], line) < 0:
                continue
            ordered = ordered[:j] + [line] + ordered[j:]
            break

    print((ordered.index([[2]]) + 1) * (ordered.index([[6]]) + 1))


if __name__ == "__main__":
    sol1()
    sol2()
