def get_length_of_number(n):
    k = 0
    while True:
        n = n / 10
        k += 1
        if n < 1:
            break
    return k


def get_first_digit(n):
    if get_length_of_number(n) == 1:
        return n
    red = 1
    while True:
        reduced = (10 ** (get_length_of_number(n) - 1) * red)
        if get_length_of_number(n - reduced) < get_length_of_number(n):
            break
        red += 1
    return red


def calc(n):
    new_num = 0
    while n > 0:
        length = get_length_of_number(n)
        first = get_first_digit(n)
        n = n - (10 ** (length - 1)) * first
        if n != 0:
            second = get_first_digit(n)
            n = n - (10 ** (length - 2)) * second
            new_num += second
            new_num *= 10
        new_num += first
        new_num *= 10
    return new_num // 10

# daniel
n1 = 12345
n2 = 34162
print(f"{n1} -> {calc(n1)}")
print(f"{n2} -> {calc(n2)}")

