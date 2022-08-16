
n = 6

for row in range(n, 0, -1):
    if row % 2:
        for col in range(row, 0, -1):
            print(col, end="")
    else:
        for col in range(1, row+1):
            print(col, end="")
    print("")