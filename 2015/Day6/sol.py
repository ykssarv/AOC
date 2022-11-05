

def sol1():
    file = open("input.txt", "r")
    lines = file.readlines()
    grid = []
    total = 0

    for i in range(1000):
        line = []
        for j in range(1000):
            line.append(0)
        grid.append(line)

    for line in lines:
        instruction = line.strip("\n").split(" ")
        command = instruction[-4]
        ax = int(instruction[-3].split(",")[0])
        ay = int(instruction[-3].split(",")[1])
        bx = int(instruction[-1].split(",")[0])
        by = int(instruction[-1].split(",")[1])
        if command == "off":
            for i in range(ax, bx + 1):
                for j in range(ay, by + 1):
                    grid[i][j] = 0
        elif command == "on":
            for i in range(ax, bx + 1):
                for j in range(ay, by + 1):
                    grid[i][j] = 1
        else:
            for i in range(ax, bx + 1):
                for j in range(ay, by + 1):
                    if grid[i][j] == 1:
                        grid[i][j] = 0
                    else:
                        grid[i][j] = 1

    for line in grid:
        for number in line:
            if number == 1:
                total += 1

    print(total)

def sol2():
    file = open("input.txt", "r")
    lines = file.readlines()
    grid = []
    total = 0

    for i in range(1000):
        line = []
        for j in range(1000):
            line.append(0)
        grid.append(line)

    for line in lines:
        instruction = line.strip("\n").split(" ")
        command = instruction[-4]
        ax = int(instruction[-3].split(",")[0])
        ay = int(instruction[-3].split(",")[1])
        bx = int(instruction[-1].split(",")[0])
        by = int(instruction[-1].split(",")[1])
        if command == "off":
            for i in range(ax, bx + 1):
                for j in range(ay, by + 1):
                    if grid[i][j] == 0:
                        grid[i][j] = 0
                    else:
                        grid[i][j] -= 1
        elif command == "on":
            for i in range(ax, bx + 1):
                for j in range(ay, by + 1):
                    grid[i][j] += 1
        else:
            for i in range(ax, bx + 1):
                for j in range(ay, by + 1):
                    grid[i][j] += 2

    for line in grid:
        for number in line:
            total += number

    print(total)




if __name__ == "__main__":
    sol1()
    sol2()


