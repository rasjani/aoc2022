#!/usr/bin/env python3

import sys
from pprint import pprint


class comms():
    state = []
    marker = 0

    def __init__(self, markerlen = 4):
        self.state = []
        self.markerlen = markerlen

    def add(self, b):
        self.marker += 1
        self.state.append(b)
        if len(self.state)>self.markerlen:
            self.state = self.state[1:]

    def wegood(self):
        res = len(set(self.state)) == self.markerlen
        return res, self.marker


with open("input") as f:
    data = f.read()

packet = comms()

for c in data:
    packet.add(c)
    res, marker = packet.wegood()
    if res:
        print(f"packet pos {marker}")
        break


msg = comms(14)

for c in data:
    msg.add(c)
    res, marker = msg.wegood()
    if res:
        print(f"msg pos {marker}")
        break
