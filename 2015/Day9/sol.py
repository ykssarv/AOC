import random


def sol1():
    file = open("input.txt", "r")
    lines = file.readlines()
    file.close()
    distances = {}

    for line in lines:
        line = line.strip("\n").split()
        if line[0] not in distances.keys():
            distances[line[0]] = {}
        if line[2] not in distances.keys():
            distances[line[2]] = {}

    for line in lines:
        line = line.strip("\n").split()
        distances[line[0]][line[2]] = int(line[-1])
        distances[line[2]][line[0]] = int(line[-1])

    best_sol = []
    for distance in distances.keys():
        best_sol.append(distance)

    best_distance = 0
    for i in range(len(best_sol)):
        if i < len(best_sol) - 1:
            best_distance += distances[best_sol[i]][best_sol[i + 1]]

    for i in range(1000000):
        distance = 0
        new_sol = [x for x in best_sol]
        random.shuffle(new_sol)
        for j in range(len(new_sol)):
            if j < len(new_sol) - 1:
                distance += distances[new_sol[j]][new_sol[j+1]]
        if distance > best_distance:
            best_distance = distance
            best_sol = new_sol

    print(best_distance)


if __name__ == "__main__":
    sol1()