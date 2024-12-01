a = []
b = {}

with open('./input.txt', "rt") as data:
    for line in data.read().split("\n"):
        tmp = line.split(" ")
        try:
            a.append(int(tmp[0]))
        except:
            continue
        try:
            b[int(tmp[-1])] += 1
        except:
            b[int(tmp[-1])] = 1
            continue

diff = 0

for i in a:
    try:
        diff += i * b[i]
    except:
        continue

print(diff)
