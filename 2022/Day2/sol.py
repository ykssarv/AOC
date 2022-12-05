

def sol1():
    file = open("input.txt", "r")
    lines = file.readlines()
    file.close()

    total = 0
    points = {
        "A X": 4,
        "B Y": 5,
        "C Z": 6,
        "A Y": 8,
        "A Z": 3,
        "B X": 1,
        "B Z": 9,
        "C X": 7,
        "C Y": 2

    }

    for line in lines:
        total += points[line.strip("\n")]

    print(total)


def sol2():
    file = open("input.txt", "r")
    lines = file.readlines()
    file.close()

    total = 0
    points = {
        "A X": 3,
        "B Y": 5,
        "C Z": 7,
        "A Y": 4,
        "A Z": 8,
        "B X": 1,
        "B Z": 9,
        "C X": 2,
        "C Y": 6

    }

    for line in lines:
        total += points[line.strip("\n")]

    print(total)

if __name__ == "__main__":
    sol1()
    sol2()
