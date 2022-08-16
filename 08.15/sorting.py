import random

n = 5
a = [random.randint(1, 9) for i in range(n)]
a = [11, 4, 33, 3, 1]
print(a)


def bubble_sort():
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    print(a)


def insertion_sort():
    for i in range(n):
        key = a[i]
        j = i - 1

        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key


insertion_sort()
