from math import *

n = 8

for col in range(n):
    for row in range(n):
        if row+col < ceil(n/2)-1 \
                or col-row > n//2 \
                or (col+row > n+floor(n/2)-1) \
                or (row-col > n//2):
            print("*", end="\t")
        else:
            print("", end="\t")
    print("")