lst = [[""] * 3]
email_endings = [".co", ".com", ".in", ".org"]


# 0=name, 1=phone 2=email
def check_if_exists(phone, i):
    for x, each in enumerate(lst):
        if each[i] == phone:
            return x
    return False


def my_append():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    while check_if_exists(phone, 1):
        print("Not unique number!")
        phone = input("INVALID! Enter Valid Phone Number:")

    email = input("Enter Email Address: ")
    if not check_good_email(email):
        return 0

    if not has_numbers(name) or len(phone) != 10:
        print("Wrong data!")
        return 0

    lst.append([name, phone, email])
    print("ADDED:", *lst[-1])


def print_phone_book():
    for each in ["NAME", "PHONE", "EMAIL"]:
        print(each.center(15), end='\t')
    print('')
    for each in lst[1:]:
        for s in each:
            print(s.center(15), end='\t')
        print("")


def has_numbers(string):
    return any(char.isdigit() for char in string)


def print_menu():
    print("Phonebook")
    print("1 Insert")
    print("2 Delete")
    print("3 Search")
    print("4 Update")
    print("5 Display")
    print("6 Exit")


def delete_by_phone():
    phone = str(input("Enter Phone Number to Delete: "))
    x = check_if_exists(phone, 1)
    if x:
        del lst[x]
        print("Entry Deleted!")
    else:
        print("Not found!")


def check_good_email(email):
    good_email = False
    for each in email_endings:
        if email.endswith(each):
            good_email = True
            break
    if not good_email:
        print("Invalid email! Must end with one of following:", *email_endings)
        return False
    return True


def update_by_phone():
    phone = str(input("Enter Phone Number to Update: "))
    x = check_if_exists(phone, 1)
    if x:
        name = input("Change name? Leave emtpy for no.")
        if name:
            if not has_numbers(name):
                lst[x][0] = name
            else:
                print("Invalid Name!")
                return 0
        phone = input("Change phone number? Leave emtpy for no.")
        if len(phone) == 10:
            if check_if_exists(phone, 1):
                print("Not unique number!")
                return 0
            lst[x][1] = phone
        email = input("Change email? Leave emtpy for no.")
        if not check_good_email(email):
            return 0
        if email:
            lst[x][2] = email
        print("ENTRY UPDATED:", *lst[x])
    else:
        print("Not found!")


def search_by_phone():
    phone = str(input("Enter Phone Number to Search: "))
    x = check_if_exists(phone, 1)
    if x:
        for each in ["NAME", "PHONE", "EMAIL"]:
            print(each.center(15), end='\t')
        print('')
        for s in lst[x]:
            print(s.ljust(15), end='\t')
        print("")
    else:
        print("Not found!")


if __name__ == '__main__':
    while True:
        print_menu()
        inp = int(input("Menu Choice: "))
        if inp == 1:
            print("ADDING NEW:")
            my_append()
        elif inp == 2:
            delete_by_phone()
        elif inp == 3:
            search_by_phone()
        elif inp == 4:
            update_by_phone()
        elif inp == 5:
            print_phone_book()
        elif inp == 6:
            break
