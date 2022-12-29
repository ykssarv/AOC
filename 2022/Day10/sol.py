

def sol1():
    file = open("input.txt", "r")
    lines = file.readlines()
    file.close()

    i = 0
    strength = 1
    memory = {}
    cycle = 0
    total = 0

    while True:
        if cycle not in memory.keys() and len(lines) < i:
            break
        if i <= len(lines) - 1:
            line = lines[i].strip("\n")
            if line != "noop":
                memory[cycle + 2] = int(lines[i][5:])
                if cycle == 20 or cycle == 60 or cycle == 100 or cycle == 140 or cycle == 180 or cycle == 220:
                    total += cycle * strength
                    print((cycle, strength))
                    print(total)
                if cycle in memory.keys():
                    strength += memory[cycle]
                cycle += 1
        if cycle == 20 or cycle == 60 or cycle == 100 or cycle == 140 or cycle == 180 or cycle == 220:
            total += cycle * strength
            print((cycle, strength))
            print(total)
        if cycle in memory.keys():
            strength += memory[cycle]
        cycle += 1
        i += 1
    print(total)


def sol2():
    file = open("input.txt", "r")
    lines = file.readlines()
    file.close()

    i = 0
    strength = 1
    memory = {}
    cycle = 0
    pixels = ["." for i in range(240)]

    while True:
        if cycle not in memory.keys() and len(lines) < i:
            break
        if i <= len(lines) - 1:
            line = lines[i].strip("\n")
            if line != "noop":
                memory[cycle + 2] = int(lines[i][5:])
                if cycle in memory.keys():
                    strength += memory[cycle]
                if strength == cycle % 40 or strength == cycle % 40 - 1 or strength == cycle % 40 + 1:
                    pixels[cycle] = "#"
                cycle += 1
        if cycle in memory.keys():
            strength += memory[cycle]
        if strength == cycle % 40 or strength == cycle % 40 - 1 or strength == cycle % 40 + 1:
            pixels[cycle] = "#"
        cycle += 1
        i += 1

    print(pixels[:40])
    print(pixels[40:80])
    print(pixels[80:120])
    print(pixels[120:160])
    print(pixels[160:200])
    print(pixels[200:240])




if __name__ == "__main__":
    #sol1()
    sol2()
