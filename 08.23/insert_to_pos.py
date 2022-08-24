def print_menu():
    print("MENU")
    print("1 Insert New")
    print("2 Display")
    print("3 Menu")
    print("4 Exit")


def my_insert():
    global lst
    ele = int(input("Ele:\t"))
    if lst:
        pos = int(input("Index:\t"))
        if 0 <= pos < len(lst)+1:
            lst.append(0)
            # right shift without list[:]
            for i in range(len(lst) - 1, pos - 1, -1):
                lst[i] = lst[i - 1]

            lst[pos] = ele
        else:
            print("Wrong index!")
    else:
        lst.append(ele)
    print(*lst)

lst = []

if __name__ == '__main__':
    while True:
        print_menu()
        inp = int(input("Menu Choice: "))
        if inp == 1:
            my_insert()
        elif inp == 2:
            print(lst)
        elif inp == 3:
            print_menu()
        elif inp == 4:
            break
