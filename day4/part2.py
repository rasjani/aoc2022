def get_range(elf):
    start, end = elf.split("-")
    return list(range(int(start), int(end)+1))

data = []
with open("input") as f:
    data = f.read().splitlines()

total = 0
for i in data:
    elf_a, elf_b = i.split(",",2)
    elf_a = get_range(elf_a)
    elf_b = get_range(elf_b)

    lower = set(elf_a if elf_a[0] < elf_b[0] else elf_b)
    higher = set(elf_a if elf_a[0] > elf_b[0] else elf_b)

    result = lower & higher
    #print(f"{result}")

    if len(result) > 0:
        #print(f"MATCH")
        total += 1


print(total)
