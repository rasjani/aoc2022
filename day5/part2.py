#!/usr/bin/env python3

import sys
from pprint import pprint


STACKS = 9 # COULD BE 9
ROWS = 8 # COULD BE 8
MOVES_START_AT = ROWS + 2

def splitchunk(l, cz):
    start = 0
    end = len(l)
    final = []
    for i in range(start, end, cz):
        x = i
        final.append(l[x:x+cz])
    return final


def newstack(stack, items):
    remainder = stack[:len(stack) - items]
    to_be_moved = stack[len(stack) - items: ]
    return remainder, to_be_moved


translation_table = dict.fromkeys(map(ord, '[] '), None)
data = []
with open("input") as f:
    data = f.read().splitlines()

stacks = {
  0: [],
  1: [],
  2: [],
  3: [],
  4: [],
  5: [],
  6: [],
  7: [],
  8: [],
}

stacktmp = data[0:STACKS]

for row in stacktmp[::-1]:
    items = splitchunk(row, 4)
    for stack_id, i in enumerate(items):
        i = i.translate(translation_table)
        if i:
            stacks[stack_id].extend(i)

for row in data[MOVES_START_AT:]:
    tmp = row.split(" ", 6)
    amount = int(tmp[1])
    src = int(tmp[3]) - 1
    dst = int(tmp[5]) - 1

    tmpstack, transit = newstack(stacks[src], amount)
    stacks[src] = tmpstack
    stacks[dst].extend(transit)


pprint(stacks)
