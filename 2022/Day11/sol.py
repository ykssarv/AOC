

def sol1():
    file = open("input.txt", "r")
    lines = file.readlines()
    file.close()
    items = {}
    counter = [0, 0, 0, 0]

    for i in range(1, len(lines) + 1, 7):
        monkey = int(lines[i - 1][-3])
        worried = lines[i].strip("\n").split(": ")[1].split(", ")
        items[monkey] = worried

    for j in range(20):
        for i in range(1, len(lines) + 1, 7):
            monkey = int(lines[i - 1][-3])
            while len(items[monkey]) > 0:
                counter[monkey] += 1
                operation = lines[i + 1].strip("\n").split("= ")[1].split(" ")
                amount = operation[-1]
                sign = operation[-2]
                value = int(items[monkey][0])
                if amount == "old":
                    new = lambda x: x * x
                else:
                    amount = int(amount)
                    if sign == "+":
                        new = lambda x: x + amount
                    else:
                        new = lambda x: x * amount
                value = new(value)
                value = value // 3
                condition = int(lines[i + 2].strip("\n").split(" ")[-1])
                true = int(lines[i + 3].strip("\n")[-1])
                false = int(lines[i + 4].strip("\n")[-1])
                print(items)
                if value % condition == 0:
                    items[true].append(items[monkey][0])
                else:
                    items[false].append(items[monkey][0])
                items[monkey].remove(items[monkey][0])
                print(items)

    print(counter)
if __name__ == "__main__":
    sol1()