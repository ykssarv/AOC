import hashlib


def sol1():
    key = "iwrupvqb"
    number = 1
    while True:
        puzzle = key + str(number)
        result = hashlib.md5(puzzle.encode()).hexdigest()
        if result[:6] == "000000":
            print(number)
            print(result)
            print(puzzle)
            break
        number += 1



if __name__ == "__main__":
    sol1()

