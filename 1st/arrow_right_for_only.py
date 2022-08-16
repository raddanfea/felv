n = 8

for row in range(n):
    for col in range(1, round(n / 2) + 1):
        if row + col == n or row == col - 1 or col == 1:
            print("*", end="")
        else:
            print("-", end="")

    print("")
