def sol1():
    file = open("input.txt", "r")
    directions = file.readlines()
    file.close()
    x = 0
    y = 0
    visited = [(0, 0)]

    for direction in directions[0]:
        if direction == "^":
            y += 1
        elif direction == "v":
            y -= 1
        elif direction == ">":
            x += 1
        else:
            x -= 1
        location = (x, y)
        if location not in visited:
            visited.append(location)

    print(len(visited))


def sol2():
    file = open("input.txt", "r")
    directions = file.readlines()
    file.close()
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0
    visited = [(0, 0)]

    for i in range(len(directions[0])):
        direction = directions[0][i]
        if i % 2 == 0:
            if direction == "^":
                y1 += 1
            elif direction == "v":
                y1 -= 1
            elif direction == ">":
                x1 += 1
            else:
                x1 -= 1
            location = (x1, y1)
        else:
            if direction == "^":
                y2 += 1
            elif direction == "v":
                y2 -= 1
            elif direction == ">":
                x2 += 1
            else:
                x2 -= 1
            location = (x2, y2)
        if location not in visited:
            visited.append(location)

    print(len(visited))



if __name__ == "__main__":
    sol1()
    sol2()

