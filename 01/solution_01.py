
a = []
b = []

with open('./input.txt', "rt") as data:
    for line in data.read().split("\n"):
        tmp = line.split(" ")
        try:
            a.append(int(tmp[0]))
            b.append(int(tmp[-1]))
        except:
            continue

a.sort()
b.sort()

diff = 0

for (i,j) in zip(a,b):
    diff += abs(i - j)

print(diff)
