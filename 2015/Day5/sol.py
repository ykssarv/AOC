

def sol1():
    text = open("input.txt", "r")
    lines = text.readlines()
    vowels = ["a", "e", "i", "o", "u"]
    unallowed_strings = ["ab", "cd", "pq", "xy"]
    enough_vowels = False
    double_letters = False
    unallowed = False
    nice = 0
    vowel_count = 0
    previous_letter = ""

    for line in lines:
        for letter in line:
            if letter in vowels:
                vowel_count += 1
            if letter == previous_letter:
                double_letters = True
            if previous_letter + letter in unallowed_strings:
                unallowed = True
            previous_letter = letter
        if vowel_count >= 3:
            enough_vowels = True
        if enough_vowels and double_letters and not unallowed:
            nice += 1
        enough_vowels = False
        double_letters = False
        unallowed = False
        vowel_count = 0
    print(nice)


def sol2():
    text = open("input.txt", "r")
    lines = text.readlines()
    previous_letter = ""
    penultimate = ""
    double = False
    repeating = False
    nice = 0

    for line in lines:
        for i, letter in enumerate(line):
            if i == 0:
                previous_letter = letter
                continue
            if i == 1:
                if previous_letter + letter in line[i + 1:]:
                    double = True
                penultimate = previous_letter
                previous_letter = letter
                continue
            if previous_letter + letter in line[i + 1:]:
                double = True
            if penultimate == letter:
                repeating = True
            penultimate = previous_letter
            previous_letter = letter
        if repeating and double:
            nice += 1
        repeating = False
        double = False
    print(nice)

if __name__ == "__main__":
    sol1()
    sol2()