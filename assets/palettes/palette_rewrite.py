from sharpie_palette import PALETTE
from math import sqrt

def dist(pixel):
    r,g,b = pixel
    return sqrt(r**2 + g**2 + b**2)

seq = list()
for color in PALETTE.keys():
    seq.append([dist(PALETTE[color]), color, PALETTE[color]])

seq = [item for item in reversed(sorted(seq, key=lambda entry: entry[0]))]

with open("sharp.txt", "w") as writefile:
    for item in seq:
        r,g,b = item[2]
        writefile.write("{}=({},{},{})\n".format(item[1], r,g,b))
