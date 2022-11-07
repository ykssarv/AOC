

def sol1():
    file = open("input.txt", "r")
    lines = file.readlines()
    file.close()
    total_len_code = 0
    total_len_memory = 0

    for line in lines:
        print(line.strip("\n"))
        len_memory = 0
        i = 0
        len_code = len(line) - 1
        while True:
            if i == len(line):
                break
            if line[i] == "\\":
                if line[i + 1] == "\"":
                    i += 1
                elif line[i + 1] == "\\":
                    i += 1
                else:
                    i += 3
            i += 1
            len_memory += 1
        total_len_memory += len_memory - 3
        total_len_code += len_code
    print(total_len_code)
    print(total_len_memory)
    print(total_len_code - total_len_memory)


def sol2():
    file = open("input.txt", "r")
    lines = file.readlines()
    file.close()
    total_len_code = 0
    total_len_memory = 0

    for line in lines:
        line = line.strip("\n")
        len_code = 0
        i = 0
        len_memory = len(line)
        while True:
            if i >= len_memory:
                break
            if line[i] == "\"":
                len_code += 2
            elif line[i] == "\\":
                len_code += 2
            else:
                len_code += 1
            i += 1
        total_len_memory += len_memory
        total_len_code += len_code + 2
    print(total_len_code)
    print(total_len_memory)
    print(total_len_code - total_len_memory)


if __name__ == "__main__":
    sol1()
    sol2()

