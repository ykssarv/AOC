

def sol1():
    file = open("input.txt", "r")
    lines = file.readlines()
    file.close()
    xh = 0
    yh = 0
    xt = 0
    yt = 0
    unique = set()

    for line in lines:
        line = line.strip("\n").split(" ")
        direction = line[0]
        steps = int(line[1])
        for i in range(steps):
            if direction == "R":
                xh += 1
                if xh - xt == 2:
                    xt += 1
                    yt = yh
            if direction == "L":
                xh -= 1
                if xt - xh == 2:
                    xt -= 1
                    yt = yh
            if direction == "U":
                yh += 1
                if yh - yt == 2:
                    yt += 1
                    xt = xh
            if direction == "D":
                yh -= 1
                if yt - yh == 2:
                    yt -= 1
                    xt = xh
            location = (xt, yt)
            unique.add(location)


def sol2():
    file = open("input.txt", "r")
    lines = file.readlines()
    file.close()
    knots = {0: [0, 0],
             1: [0, 0],
             2: [0, 0],
             3: [0, 0],
             4: [0, 0],
             5: [0, 0],
             6: [0, 0],
             7: [0, 0],
             8: [0, 0],
             9: [0, 0]}
    unique = set()

    for line in lines:
        line = line.strip("\n").split(" ")
        direction = line[0]
        steps = int(line[1])
        for i in range(steps):
            if direction == "R":
                knots[0][0] += 1
            if direction == "L":
                knots[0][0] -= 1
            if direction == "U":
                knots[0][1] += 1
            if direction == "D":
                knots[0][1] -= 1
            for j in range(1, len(knots)):
                if knots[j - 1][0] - knots[j][0] == 2:
                    knots[j][0] += 1
                    if knots[j][1] < knots[j - 1][1]:
                        knots[j][1] += 1
                    elif knots[j][1] > knots[j - 1][1]:
                        knots[j][1] -= 1
                elif knots[j - 1][0] - knots[j][0] == -2:
                    knots[j][0] -= 1
                    if knots[j][1] < knots[j - 1][1]:
                        knots[j][1] += 1
                    elif knots[j][1] > knots[j - 1][1]:
                        knots[j][1] -= 1
                if knots[j - 1][1] - knots[j][1] == 2:
                    knots[j][1] += 1
                    if knots[j][0] < knots[j - 1][0]:
                        knots[j][0] += 1
                    elif knots[j][0] > knots[j - 1][0]:
                        knots[j][0] -= 1
                elif knots[j - 1][1] - knots[j][1] == -2:
                    knots[j][1] -= 1
                    if knots[j][0] < knots[j - 1][0]:
                        knots[j][0] += 1
                    elif knots[j][0] > knots[j - 1][0]:
                        knots[j][0] -= 1
                if j == 9:
                    location = (knots[j][0], knots[j][1])
                    unique.add(location)
    print(len(unique))

if __name__ == "__main__":
    sol1()
    sol2()