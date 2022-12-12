
def sol1():
    file = open("input.txt", "r")
    lines = file. readlines()
    file.close()
    east = True
    west = True
    north = True
    south = True
    count = 0

    for i in range(len(lines)):
        line = lines[i].strip("\n")
        for j in range(len(line)):
            for e in range(j + 1, len(line)):
                if line[j] <= line[e]:
                    east = False
            for w in range(0, j):
                if line[j] <= line[w]:
                    west = False
            for n in range(i + 1, len(lines)):
                if lines[i][j] <= lines[n][j]:
                    north = False
            for s in range(0, i):
                if lines[i][j] <= lines[s][j]:
                    south = False
            if east or north or south or west:
                count += 1
            east = True
            west = True
            north = True
            south = True
    print(count)

def sol2():
    file = open("input.txt", "r")
    lines = file.readlines()
    file.close()
    east = 0
    west = 0
    north = 0
    south = 0
    score = 0
    i = 0

    while i < len(lines):
        line = lines[i].strip("\n")
        j = 0
        while j < len(line):
            for e in range(j + 1, len(line)):
                if line[j] <= line[e]:
                    east = e - j
                    break
                if line[j] > line[e]:
                    east += 1
                    continue
            for w in range(j - 1,  - 1, -1):
                if line[j] <= line[w]:
                    west = j - w
                    break
                if line[j] > line[w]:
                    west += 1
                    continue
            for n in range(i + 1, len(lines)):
                if lines[i][j] <= lines[n][j]:
                    south = n - i
                    break
                if lines[i][j] > lines[n][j]:
                    south += 1
                    continue
            for s in range(i - 1, -1, -1):
                if lines[i][j] <= lines[s][j]:
                    north = i - s
                    break
                if lines[i][j] > lines[s][j]:
                    north += 1
                    continue
            print(f"i={i} j={j} and e={east} w={west} s={south} n={north}")
            if east * west * south * north > score:
                score = east * west * south * north
            east = 0
            west = 0
            north = 0
            south = 0
            j += 1
        i += 1

    print(score)


if __name__ == "__main__":
    sol1()
    sol2()
