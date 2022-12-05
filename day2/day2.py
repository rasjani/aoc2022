
ELF = { "A": "ROCK", "B": "PAPER", "C": "SCISSORS"}
ME = { "X": "ROCK", "Y": "PAPER", "Z": "SCISSORS"}
BEATS = {"ROCK": "SCISSORS", "SCISSORS": "PAPER", "PAPER": "ROCK"}
WIN = 6
POINTS = {"ROCK": 1, "PAPER": 2, "SCISSORS": 3}

data = []
total_elf_score = 0
total_my_score = 0
ties = 0
with open("input") as f:
    data = f.read().splitlines()


for day in data:
    print(f"XXX: {day} ")
    elf, me = day.split(" ",2)

    elf_hand = ELF[elf]
    my_hand = ME[me]
    my_bonus = 0
    elf_bonus = 0

    elf_score = POINTS[elf_hand]
    my_score = POINTS[my_hand]

    winner = ""
    full = f"{elf_hand} {elf_score} vs {my_hand} {my_score}"

    if elf_hand == my_hand:
        ties += 1
        my_bonus = 3
        elf_bonus = 3
        winner = "TIE"
    elif BEATS[elf_hand] == my_hand:
        my_bonus = 0
        my_scrore = 0
        elf_bonus = 6
        winner = "ELF"
    else:
        my_bonus = 6
        elf_bonus = 0
        winner = "ME"

    total_elf_score += elf_score + elf_bonus
    total_my_score += my_score + my_bonus

print(total_my_score)

