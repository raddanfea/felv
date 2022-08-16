
# n = 153 1**3+5*3+3**3

def get_length_of_number(n):
    k = 0
    while True:
        n = n // 10
        k += 1
        if n < 1:
            break
    return k


def check_armstrong(n):
    sum_of = 0
    length = get_length_of_number(n)
    temp = n
    while temp > 0:
        digit = temp % 10
        sum_of += digit ** length
        temp //= 10
    return n == sum_of


for each in range(10000):
    if check_armstrong(each):
        print(each)
