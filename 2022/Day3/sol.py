

def sol1():
    file = open("input.txt", "r")
    lines = file.readlines()
    file.close()
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    priority = 0

    for i in range(len(lines)):
        first = lines[i].strip("\n")[:len(lines[i]) // 2]
        second = lines[i].strip("\n")[len(lines[i]) // 2:]
        for j in range(len(first)):
            letter = first[j]
            if letter in second and letter not in first[:j]:
                if letter.islower():
                    priority += lower.index(letter) + 1
                else:
                    priority += upper.index(letter) + 27

    print(priority)


def sol2():
    file = open("input.txt", "r")
    lines = file.readlines()
    file.close()
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    priority = 0
    i = 0

    while i < len(lines):
        if i < len(lines) - 2:
            first = lines[i].strip("\n")
            second = lines[i + 1].strip("\n")
            third = lines[i + 2].strip("\n")
        for j in range(len(first)):
            letter = first[j]
            if letter not in first[:j] and letter in second and letter in third:
                if letter.islower():
                    priority += lower.index(letter) + 1
                else:
                    priority += upper.index(letter) + 27
        i += 3
    print(priority)


if __name__ == "__main__":
    sol1()
    sol2()
