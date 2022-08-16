

n = 3

for col in range(n * 2):
    for row in range((n * 2) - 1):
        if row + col < n:  # upper left
            print("*", end="\t")
        elif row - col > n - 2:  # upper right
            print("*", end="\t")
        elif row == (n * 2) - 2 or col == (n * 2) - 1 or row == 0:  # left, bottom, right lines
            print("*", end="\t")
        else:
            print("", end="\t")
    print("")
