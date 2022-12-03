

def sol1():
    old = [x for x in "vzbxkghb"]
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    counter = 0
    while True:
        # increment step
        count = -1
        while True:
            # increment single letter
            if alphabet[alphabet.index(old[count])] == "z":
                old[count] = "a"
                count -= 1
            else:
                old[count] = alphabet[alphabet.index(old[count]) + 1]
                break

        bad_letters = False
        double_count = 0
        double_letters = False
        straight = False
        i = 0
        while i < len(old):
            if old[i] == "i" or old[i] == "l" or old[i] == "o":
                bad_letters = True
            if i < len(old) - 1:
                if old[i] == old[i + 1]:
                    double_count += 1
                    i += 1
                    if double_count == 2:
                        double_letters = True
            i += 1
        i = 0
        while i < len(old):
            if i < len(old) - 2:
                if alphabet.index(old[i]) + 2 < len(alphabet):
                    if old[i + 1] == alphabet[alphabet.index(old[i]) + 1] and old[i + 2] == alphabet[alphabet.index(old[i]) + 2]:
                        i += 2
                        straight = True
            i += 1

        if not bad_letters and double_letters and straight:
            counter += 1
            if counter == 2:
                return old
        # print(old)

if __name__ == "__main__":
    print(sol1())
