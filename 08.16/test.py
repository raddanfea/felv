lst = []


def find_index(lst, num):
    ind = 0
    for each in lst:
        if each == num:
            break
        ind += 1
    return ind


def just_add(ele):
    print("Not in list, added as last.")
    lst.append(ele)


# add 6 before 3
# 1  2 (3) 4        # get index of 3
# 1  2 [3  4] 0     # add 0
# 1  2  3 [3  4]    # right shift
# 1  2 (6) 3  4     # set index to value
def my_append():
    ele = int(input("What element to append? "))

    if not lst:
        just_add(ele)
        return 0

    pos = int(input("Which element to compare to? "))
    if pos in lst:
        lst.append(0)
        after = int(input("Before (0) or after (1)? "))
        where = find_index(lst, pos)
        for i in range(len(lst) - 1, where + after, -1):
            lst[i] = lst[i - 1]
        lst[where + after] = ele
    else:
        just_add(ele)


def print_menu():
    print("MENU")
    print("1 Insert New")
    print("2 Display")
    print("3 Menu")
    print("4 Exit")


if __name__ == '__main__':
    print_menu()
    while True:
        inp = int(input("Menu Choice: "))
        if inp == 1:
            my_append()
        elif inp == 2:
            print(lst)
        elif inp == 3:
            print_menu()
        elif inp == 4:
            break
