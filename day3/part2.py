
def priority(item):
    if not item.islower():
        return ord(item) - 38
    else:
        return ord(item) - 96

def splitchunk(l, cz):
    start = 0
    end = len(l)
    final = []
    for i in range(start, end, cz):
        x = i
        final.append(l[x:x+cz])
    return final

data = []

with open("input") as f:
    data = splitchunk(f.read().splitlines(), 3)


sum = 0
for row in data:
    compA = set(list(row[0]))
    compB = set(list(row[1]))
    compC = set(list(row[2]))

    common = list(compA & compB & compC)

    for i in common:
        pri = priority(i)
        sum += pri
        print(i, pri )

print(sum)
