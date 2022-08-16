n = 123456
r = 3


def get_length_of_number(n):
    k = 0
    while True:
        n = n / 10
        k += 1
        if n < 1:
            break
    return k - 1


def get_last_digit(n):
    a = 1
    while True:
        k = n - a
        if k % 10 == 0:
            break
        a += 1
    return a


def get_next_rotation(n):
    last = get_last_digit(n)
    length = get_length_of_number(n)
    n = (n - last) / 10
    return int(n + 10 ** length * last)


for each in range(r):
    n = get_next_rotation(n)
print(n)
