l = [11, 2, 333, 1, 44, 5, 66, 777]


def get_min(this_list):
    min_ele = this_list[0]
    l_i = 0
    for i in range(1, len(this_list)):
        if this_list[i] < min_ele:
            min_ele = this_list[i]
            l_i = i
    del this_list[l_i]
    return min_ele


def sol2():
    print(l)

    new_1 = []
    new_2 = []
    for each in range(0, len(l), 2):
        new_1.append(l[each])
    for each in range(1, len(l), 2):
        new_2.append(l[each])

    newest = []
    while new_2 or new_1:
        small1 = get_min(new_1)
        small2 = get_min(new_2)
        newest.append(small1)
        newest.append(small2)
        print(newest)


def sol1():
    print(l)

    swap = True
    while swap:
        swap = False
        for each in range(0, len(l) - 2, 2):
            k = each + 1
            if l[k] > l[k + 2]:
                l[k], l[k + 2] = l[k + 2], l[k]
                swap = True
        if swap: print(l)
    swap = True
    while swap:
        swap = False
        for each in range(0, len(l) - 2, 2):
            k = each
            if l[k] > l[k + 2]:
                l[k], l[k + 2] = l[k + 2], l[k]
                swap = True
        if swap: print(l)
    print(l)

sol1()
sol2()