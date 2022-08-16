n = 5

first = True
number1 = 0
number2 = 1

for col in range(n):
    for row in range((n * 2) - 1):
        if row + col < n - 1:  # upper left
            print("".ljust(n*2), end="\t")
        elif row - col > n - 1:  # upper right
            print("".ljust(n*2), end="\t")
        else:
            if first:
                print("0".ljust(n*2), end="\t")
                first = not first
            else:
                print(str(number2).ljust(n*2), end="\t")
                number2, number1 = number1 + number2, number2

    print("")
