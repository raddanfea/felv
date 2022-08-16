a = [11, 22, 33, 44, 55]
b = [1, 2, 3, 4]


print(a)


def length(a):
    l = 0
    for each in a:
        l += 1
    return l


def right_shift_list(a):
    lst = [0] * length(a)
    for i in range(length(a)-1):
        lst[i+1] = a[i]
    lst[0] = a[length(lst)-1]
    return lst


n = 3
for each in range(n):
    a = right_shift_list(a)
    print(a)