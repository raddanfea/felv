
def generate_row(inner, length):
    flip_bool = False

    temp = 1

    print("\t" * int(length - inner), end="")
    if inner == 1:
        print("1", "\t")
        return 1
    while True:
        print(temp, end="\t")
        if flip_bool:
            temp -= 1
        else:
            temp += 1
        if temp == 0:
            break
        if temp == inner:
            flip_bool = True
    print("")


def draw_whole(n):
    for row in range(1, n + 1):
        generate_row(row, n)
    for row in range(n - 1, 0, -1):
        generate_row(row, n)

n = 4
draw_whole(n)
