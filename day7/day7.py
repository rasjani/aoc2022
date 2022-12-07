from anytree import Node, RenderTree, LevelOrderIter
from pprint import pprint
from functools import reduce

ROOT = None
curdir = None
OUTPUT = False
SIZE = 70000000
AT_LEAST = 30000000


with open("input") as f:
    data = f.read().splitlines()

for row in data:

    if row[0] == "$":
        OUTPUT = False
        res = row[2:].split(" ")
        cmd = res[0]
        if len(res)>1:
            arg = res[1]
        else:
            arg = None

        # Path structure
        if cmd == "cd":
            if arg == "..":
                curdir = curdir.parent
            elif arg == "/" and not ROOT:
                ROOT = Node(arg, ftype="dir", fsize=0)
                curdir = ROOT
            else:
                np = Node(arg, parent=curdir, ftype="dir", fsize=0)
                curdir = np
        elif cmd == "ls":
            OUTPUT = True
    else:
        if OUTPUT:
            res = row.split(" ")
            if res[0] == "dir":
                continue
            Node(res[1], parent=curdir, ftype="file", fsize=int(res[0]))


for pre, fill, node in RenderTree(ROOT):
    if node.ftype == "file":
        node.parent.fsize += node.fsize

only_dirs = list(LevelOrderIter(ROOT, filter_=lambda n: n.ftype == "dir"))[::-1]

for n in only_dirs:
    if n.parent:
        n.parent.fsize += n.fsize

sum  = reduce(lambda a,b: a + b.fsize, filter(lambda i: i.fsize < 100000, only_dirs), 0)
print(f"Part1: {sum}")

CURRENT_FREESPACE = SIZE - ROOT.fsize

print(f"Current freespace : {CURRENT_FREESPACE}")
print(f"At least required : {AT_LEAST}")
removed = filter(lambda i: CURRENT_FREESPACE + i.fsize >= AT_LEAST, only_dirs)

x = SIZE
for n in removed:
    if n.fsize < x:
       x = n.fsize


print(x)


