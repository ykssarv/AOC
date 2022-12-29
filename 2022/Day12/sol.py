from queue import PriorityQueue

def sol1():
    file = open("input.txt", "r")
    lines = file.readlines()
    file.close()
    heightmap = []
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    start = ()
    target = ()

    for i in range(len(lines)):
        lines[i].strip("\n")
        heightmap.append([])
        for char in lines[i].strip("\n"):
            heightmap[i].append(char)

    for y in range(len(heightmap)):
        for x in range(len(heightmap[y])):
            if heightmap[y][x] == "S":
                start = (x, y)
            if heightmap[y][x] == "E":
                target = (x, y)

    queue = PriorityQueue()
    visited = set()
    queue.put((0, start, None))
    while not queue.empty():
        dist, came_from, previous = queue.get()
        if came_from == target:
            return dist
        if came_from in visited:
            continue
        visited.add(came_from)
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx = int(came_from[0] + dx)
            ny = int(came_from[1] + dy)
            if nx < 0 or ny < 0 or nx >= len(heightmap[0]) or ny >= len(heightmap):
                continue
            if heightmap[came_from[1]][came_from[0]] == "S":
                value = 0
            else:
                value = alphabet.index(heightmap[came_from[1]][came_from[0]])
            if heightmap[ny][nx] == "E":
                value2 = 25
            elif heightmap[ny][nx] == "S":
                value2 = 0
            else:
                value2 = alphabet.index(heightmap[ny][nx])
            if value2 - value > 1:
                continue
            if (nx, ny) in visited:
                continue
            neighbour = (nx, ny)
            print(dist)
            queue.put((dist + 1, neighbour, came_from))




def sol2():
    file = open("input.txt", "r")
    lines = file.readlines()
    file.close()
    heightmap = []
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    start = ()
    target = ()

    for i in range(len(lines)):
        lines[i].strip("\n")
        heightmap.append([])
        for char in lines[i].strip("\n"):
            heightmap[i].append(char)

    queue = PriorityQueue()

    for y in range(len(heightmap)):
        for x in range(len(heightmap[y])):
            if heightmap[y][x] == "S" or heightmap[y][x] == "a":
                start = (x, y)
                queue.put((0, start, None))
            if heightmap[y][x] == "E":
                target = (x, y)

    visited = set()

    while not queue.empty():
        dist, came_from, previous = queue.get()
        if came_from == target:
            return dist
        if came_from in visited:
            continue
        visited.add(came_from)
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx = int(came_from[0] + dx)
            ny = int(came_from[1] + dy)
            if nx < 0 or ny < 0 or nx >= len(heightmap[0]) or ny >= len(heightmap):
                continue
            if heightmap[came_from[1]][came_from[0]] == "S":
                value = 0
            else:
                value = alphabet.index(heightmap[came_from[1]][came_from[0]])
            if heightmap[ny][nx] == "E":
                value2 = 25
            elif heightmap[ny][nx] == "S":
                value2 = 0
            else:
                value2 = alphabet.index(heightmap[ny][nx])
            if value2 - value > 1:
                continue
            if (nx, ny) in visited:
                continue
            neighbour = (nx, ny)
            print(dist)
            queue.put((dist + 1, neighbour, came_from))


if __name__ == "__main__":
    sol1()
    sol2()
