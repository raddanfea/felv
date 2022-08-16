from math import ceil

n = 4

# for row in range(1, 9):
#    for col in range(1, n + 1):
#        if (row + col) % 14 == 5 or (col-row) % 14 ==3:
#            print("*", end='\t')
#        else:
#            print("", end='\t')
#    print("")

for row in range(1, 2 * n + 1):
    for col in range(1, 3 * n + 3):
        if (row + col) % ((4 * n) - 2) == 5 or (col - row) % ((4 * n) - 2) == 3:
            print("*", end='\t')
        else:
            print("", end='\t')
    print("")
