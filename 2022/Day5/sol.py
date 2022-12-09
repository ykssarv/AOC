

def sol1():
    file = open("input.txt", "r")
    lines = file.readlines()
    file.close()

    stacks = [["J", "H", "G", "M", "Z", "N", "T", "F"],
              ["V", "W", "J"],
              ["G", "V", "L", "J", "B", "T", "H"],
              ["B", "P", "J", "N", "C", "D", "V", "L"],
              ["F", "W", "S", "M", "P", "R", "G"],
              ["G", "H", "C", "F", "B", "N", "V", "M"],
              ["D", "H", "G", "M", "R"],
              ["H", "N", "M", "V", "Z", "D"],
              ["G", "N", "F", "H"]]

    result = ""

    for i in range(len(lines)):
        line = lines[i].strip("\n").split(" ")
        amount = int(line[1])
        f = int(line[3]) - 1
        t = int(line[5]) - 1
        for j in range(amount):
            el = stacks[f].pop()
            stacks[t].append(el)

    for i in range(len(stacks)):
        result += stacks[i].pop()

    print(result)


def sol2():
    file = open("input.txt", "r")
    lines = file.readlines()
    file.close()

    stacks = [["J", "H", "G", "M", "Z", "N", "T", "F"],
              ["V", "W", "J"],
              ["G", "V", "L", "J", "B", "T", "H"],
              ["B", "P", "J", "N", "C", "D", "V", "L"],
              ["F", "W", "S", "M", "P", "R", "G"],
              ["G", "H", "C", "F", "B", "N", "V", "M"],
              ["D", "H", "G", "M", "R"],
              ["H", "N", "M", "V", "Z", "D"],
              ["G", "N", "F", "H"]]

    result = ""

    for i in range(len(lines)):
        line = lines[i].strip("\n").split(" ")
        amount = int(line[1])
        f = int(line[3]) - 1
        t = int(line[5]) - 1
        for j in range(amount):
            stacks[t].append(stacks[f][len(stacks[f]) - amount + j])
        stacks[f] = stacks[f][:-amount]

    for i in range(len(stacks)):
        result += stacks[i].pop()

    print(result)


if __name__ == "__main__":
    sol1()
    sol2()
