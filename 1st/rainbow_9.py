from math import ceil

n = 10

for row in range(1, n+1):
    for col in range(1, n+1):
        if (row+1 > col and row < 1+ceil(n/2)) or (row-1 < col and row > n//2):
            print("*", end='\t')
        else:
            print("", end='\t')
    print("")