#!/usr/bin/python
"""
Rolling dice

input a roll arg and output a result
roll arg examples
1d4
3d6
1d100 - 4
4d4 + 1d6
"""

import random
try:
    raw_input
except:
    raw_input=input
def roll_die(arg):
    total = 0
    if "d" not in arg:
        return int(arg)
    if arg[0] is "-":
        neg = True
        arg = arg[0:]
    else:
        neg = False
    rolls, sides = arg.split("d")
    if rolls == "":
        rolls = 1
    for roll in range(int(rolls)):
        total += random.randint(1, int(sides))
    if neg:
        total *= -1
    return total

def roll(arg):
    total = 0
    for term in arg.replace(" ","").replace("-","+-").split("+"):
        total += roll_die(term)
    return total

line = raw_input("roll : ")
print(roll(line))
