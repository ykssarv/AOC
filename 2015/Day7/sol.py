

def sol1():
    file = open("input.txt", "r")
    lines = file.readlines()
    file.close()
    wires = {}

    for line in lines:
        instruction = line.strip("\n").split(" ")
        wires[instruction[-1]] = instruction[:-2]

    wires["b"] = 16076

    while True:
        if isinstance(wires["a"], int):
            print(wires["a"])
            break
        for key, value in wires.items():
            if isinstance(value, int):
                continue
            if len(value) == 1:
                if value[0].isnumeric():
                    wires[key] = int(value[0])
                elif isinstance(wires[value[0]], int):
                    wires[key] = wires[value[0]]
                continue
            if len(value) == 2:
                if value[1].isnumeric():
                    wires[key] = ~int(value[1])
                elif isinstance(wires[value[1]], int):
                    wires[key] = ~wires[value[1]]
                continue
            if value[1] == "AND":
                if value[0].isnumeric() and value[2].isnumeric():
                    wires[key] = int(value[0]) & int(value[2])
                elif value[0] in wires.keys() and isinstance(wires[value[0]], int) and value[2] in wires.keys() and isinstance(wires[value[2]], int):
                    wires[key] = wires[value[0]] & wires[value[2]]
                elif value[0] in wires.keys() and isinstance(wires[value[0]], int) and value[2].isnumeric():
                    wires[key] = wires[value[0]] & int(value[2])
                elif value[2] in wires.keys() and isinstance(wires[value[2]], int) and value[0].isnumeric():
                    wires[key] = wires[value[2]] & int(value[0])
                continue
            if value[1] == "OR":
                if value[0].isnumeric() and value[2].isnumeric():
                    wires[key] = int(value[0]) | int(value[2])
                elif value[0] in wires.keys() and isinstance(wires[value[0]], int) and value[2] in wires.keys() and isinstance(wires[value[2]], int):
                    wires[key] = wires[value[0]] | wires[value[2]]
                elif value[0] in wires.keys() and isinstance(wires[value[0]], int) and value[2].isnumeric():
                    wires[key] = wires[value[0]] | int(value[2])
                elif value[2] in wires.keys() and isinstance(wires[value[2]], int) and value[0].isnumeric():
                    wires[key] = wires[value[2]] | int(value[0])
                continue
            if value[1] == "RSHIFT":
                if value[0].isnumeric() and value[2].isnumeric():
                    wires[key] = int(value[0]) >> int(value[2])
                elif value[0] in wires.keys() and isinstance(wires[value[0]], int) and value[2] in wires.keys() and isinstance(wires[value[2]], int):
                    wires[key] = wires[value[0]] >> wires[value[2]]
                elif value[0] in wires.keys() and isinstance(wires[value[0]], int) and value[2].isnumeric():
                    wires[key] = wires[value[0]] >> int(value[2])
                elif value[2] in wires.keys() and isinstance(wires[value[2]], int) and value[0].isnumeric():
                    wires[key] = wires[value[2]] >> int(value[0])
                continue
            if value[1] == "LSHIFT":
                if value[0].isnumeric() and value[2].isnumeric():
                    wires[key] = int(value[0]) << int(value[2])
                elif value[0] in wires.keys() and isinstance(wires[value[0]], int) and value[2] in wires.keys() and isinstance(wires[value[2]], int):
                    wires[key] = wires[value[0]] << wires[value[2]]
                elif value[0] in wires.keys() and isinstance(wires[value[0]], int) and value[2].isnumeric():
                    wires[key] = wires[value[0]] << int(value[2])
                elif value[2] in wires.keys() and isinstance(wires[value[2]], int) and value[0].isnumeric():
                    wires[key] = wires[value[2]] << int(value[0])
                continue
    print(wires)


if __name__ == "__main__":
    sol1()
