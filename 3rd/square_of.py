
def square(n):
    return n * n


def get_length_of_number(n):
    k = 0
    while True:
        n = n / 10
        k += 1
        if n < 1:
            break
    return k


def check_end(n):
    sqr = square(n)
    sqr_m = sqr - n
    length = get_length_of_number(n)
    return not (sqr_m % (10**length))


n = 5
print(check_end(n), square(n), n)
