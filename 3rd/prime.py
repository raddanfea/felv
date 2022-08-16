def get_last_digit(n):
    return n%10


def is_prime(n):
    for i in range(2, (n//2)+2):
        if (n % i) == 0:
            return False
    return True


def sum_digits(n):
    red = 0
    while n:
        last = get_last_digit(n)
        n = (n - last) // 10
        red = red + last
    return red


def check_nums(n):
    while n:
        last = get_last_digit(n)
        n = (n - last) // 10
        if not is_prime(last):
            return False
    return True


n = 11
print(is_prime(sum_digits(n)) and is_prime(n))
