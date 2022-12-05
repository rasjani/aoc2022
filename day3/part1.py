
def priority(item):
    if not item.islower():
        return ord(item) - 38
    else:
        return ord(item) - 96

data = []
with open("input") as f:
    data = f.read().splitlines()



sum = 0
for row in data:
    compA = set(list(row[0: int(len(row)/2)]))
    compB = set(list(row[int(len(row)/2): ]))

    common = list(compA & compB)

    for i in common:
        pri = priority(i)
        sum += pri
        print(i, pri )

print(sum)
