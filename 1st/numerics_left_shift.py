n = 123456
r = 2


def get_length_of_number(n):
    k = 0
    while True:
        n = n / 10
        k += 1
        if n < 1:
            break
    return k - 1


def get_first_digit(n):
    red = 1
    while True:
        reduced = (10 ** (get_length_of_number(n)) * red)
        if get_length_of_number(n - reduced) < get_length_of_number(n):
            break
        red += 1
    return red


def get_next(n):
    red = get_first_digit(n)
    return (n - (10 ** get_length_of_number(n) * red)) * 10 + red


n = get_next(n)
print(n)
n = get_next(n)
print(n)
