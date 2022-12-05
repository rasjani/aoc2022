data = []
with open("input") as f:
    data = f.read().splitlines()

elf = 0
elfs = {}
max_cals = 0
for line in data:
    if line == "":
        if elfs[elf] > max_cals:
            max_cals = elfs[elf]
        elf += 1
        continue
    cal = int(line)
    if elf not in elfs:
        elfs[elf] = 0
    elfs[elf] += cal


print(f"PART1: {max_cals}")
cals = sorted(list(elfs.values()), reverse=True)
print(f"PART2: {sum(cals[0:3])}")



