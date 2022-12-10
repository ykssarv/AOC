
class Folder:
    def __init__(self, name):
        self.folders = {}
        self.files = {}
        self.parent = None
        self.name = name
        self.size = 0

    def calculate_size(self):
        for folder in self.folders.values():
            folder.calculate_size()
        self.size = sum(self.files.values())
        self.size += sum([x.size for x in self.folders.values()])

    def sum_less_than(self):
        total = 0
        for folder in self.folders.values():
            total += folder.sum_less_than()
        if self.size < 100000:
            total += self.size
        return total

    def min_greater_than(self, room_needed):
        best = 10000000000000000000000000000
        for folder in self.folders.values():
            best = min(folder.min_greater_than(room_needed), best)
        if self.size > room_needed:
            best = min(best, self.size)
        return best


def sol1():
    file = open("input.txt", "r")
    lines = file.readlines()
    file.close()
    root = Folder("")
    current = root

    for i in range(1, len(lines)):
        line = lines[i].strip("\n")
        if line == "$ ls":
            continue
        if line.split(" ")[0].isnumeric():
            current.files[line.split(" ")[1]] = int(line.split(" ")[0])
            continue
        if line[:3] == "dir":
            current.folders[line[4:]] = Folder(line[4:])
            current.folders[line[4:]].parent = current
            continue
        if line == "$ cd ..":
            current = current.parent
            continue
        if line[:4] == "$ cd":
            current = current.folders[line[5:]]
            continue
        print("error")

    root.calculate_size()
    answer = root.sum_less_than()
    print(answer)

    room_available = 70000000 - root.size
    room_needed = 30000000 - room_available

    answer2 = root.min_greater_than(room_needed)
    print(answer2)


if __name__ == "__main__":
    sol1()

