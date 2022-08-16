n = 8


for row in range(1, n + 1):
    for col in range(n + 1 - int(not n%2)):
        if (col + row > n - int(not n%2) and col - row >= - int(not n%2)) \
                or (col + row < n + 1 and col - row <= -1):
            print("*", end="\t")
        else:
            print("", end="\t")
    print("")
