n = 1224


def get_length_of_number(n):
    k = 0
    while True:
        n = n / 10
        k += 1
        if n < 1:
            break
    return k


def get_last_digit(n):
    a = 1
    while True:
        k = n - a
        if k % 10 == 0:
            break
        a += 1
    return a


def get_first_digit(n):
    red = 1
    while True:
        reduced = (10 ** (get_length_of_number(n)-1) * red)
        if get_length_of_number(n - reduced) < get_length_of_number(n):
            break
        red += 1
    return red


def check_if_in_number(big, num):
    digits = get_length_of_number(big)-1
    n_local = big
    for each in range(1, digits + 2):
        last = get_last_digit(n_local)
        if last == 10: last = 0
        if last == num:
            return True
        n_local = int((n_local - last) / 10)

    else:
        return False


def create_new_num(n):
    new_num = 0
    place_holder = int(n)
    while get_length_of_number(place_holder) > 0:
        first = get_first_digit(place_holder)
        print(new_num, place_holder, first, end="")
        if not check_if_in_number(new_num, first):
            new_num = new_num + first
            new_num = new_num * 10
            print("")
        else:
            print("skip")
        place_holder = (place_holder - (10 ** get_length_of_number(place_holder) * first))
    return int(new_num / 10)


print(create_new_num(n))
