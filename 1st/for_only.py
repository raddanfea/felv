

n = 10

for row in range(1, n+1):
    for col in range(1, row+1):
        print(f'{str(col)}\t', end="")

    x = "\t"*((n*2-row*2)-1)
    print(x, end="")

    for col in range(row, 0, -1):
        if col < n:
            print(f'{str(col)}\t', end="")
    print(f"   {len(x)}")