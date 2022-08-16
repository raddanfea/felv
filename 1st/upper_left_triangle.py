n = 5

for col in range(1, n+1):
    for row in range(1, n+1):
        if col == 1 or row == 1 or row+col==n+1 :
            print("*", end="\t")
        else:
            print("", end="\t")
    print("")