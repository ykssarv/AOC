

def sol1():
    puzzle = "1113222113"
    output = ""
    i = 0

    for j in range(40):
        while i < (len(puzzle)):
            if i == len(puzzle) - 1 and puzzle[i] != puzzle[i - 1]:
                output = output + "1" + str(puzzle[i])
                i += 1
            if i < len(puzzle) - 1:
                if puzzle[i] == puzzle[i + 1] == puzzle[i + 2]:
                    output = output + "3" + str(puzzle[i])
                    i += 3
                elif puzzle[i] == puzzle[i + 1]:
                    output = output + "2" + str(puzzle[i])
                    i += 2
                else:
                    output = output + "1" + str(puzzle[i])
                    i += 1
        i = 0
        puzzle = output
        if j < 39:
            output = ""
        else:
            print(len(output))


def sol2():
    puzzle = [1, 1, 1, 3, 2, 2, 2, 1, 1, 3]
    output = []
    i = 0

    for j in range(50):
        while i < (len(puzzle)):
            if i == len(puzzle) - 1 and puzzle[i] != puzzle[i - 1]:
                output.append(1)
                output.append(puzzle[i])
                i += 1
            if i < len(puzzle) - 1:
                if puzzle[i] == puzzle[i + 1] == puzzle[i + 2]:
                    output.append(3)
                    output.append(puzzle[i])
                    i += 3
                elif puzzle[i] == puzzle[i + 1]:
                    output.append(2)
                    output.append(puzzle[i])
                    i += 2
                else:
                    output.append(1)
                    output.append(puzzle[i])
                    i += 1
        i = 0
        puzzle = output
        if j < 49:
            output = []
        else:
            print(len(output))


if __name__ == "__main__":
    sol1()
    sol2()
