lst = []


def find_index(lst, num):
    ind = 0
    for each in lst:
        if each >= num:
            break
        ind += 1
    if ind > len(lst):
        return False
    return ind


def just_add(ele):
    print("No larger number found, added as last.")
    lst.append(ele)


def my_append():
    ele = int(input("What element to append? "))
    where = find_index(lst, ele)

    if not lst or type(where) is bool:
        just_add(ele)
        return 0

    lst.append(0)
    for i in range(len(lst) - 1, where - 1, -1):
        lst[i] = lst[i - 1]

    lst[where] = ele


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
