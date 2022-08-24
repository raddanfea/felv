import random

ten_dc = ["15", "20", "25"]
five_dc = ["10", "08", "05"]
one_dc = ["03", "04", "05"]

products = {
    "Fluid": 500,
    "Oil": 600,
    "Kakukk": 2000,
    "Fapapucs": 1200,
    "StillWater": 400,
    "Domestos": 285,
}

cart = {}


def print_prods():
    print("PRODUCTS".center(100, '_'))
    print("NAME: ", end="")
    for each in products.keys():
        print(str(each).center(15), end="")
    print("\nPRICE:", end="")
    for each in products.values():
        print(str(each).center(15), end="")
    print("")


def print_cart():
    l = ["NAME", "NUMBER", "SUM"]
    total = 0
    print("CART".center(45, '_'))

    for each in l:
        print(each.center(15), end="")
    print("")

    for name, db in cart.items():
        total += db * products[name]
        print(f'{str(name).center(15)}{str(db).center(15)}{str(db * products[name]).center(15)}')
    print("="*45)
    print(f'TOTAL:', total)
    return total


def checkout():
    total = print_cart()
    code = ""
    dc = ""

    if total > 10000:
        code = "TEN"
        dc = random.choice(ten_dc)
    elif total > 5000:
        code = "FIVE"
        dc = random.choice(five_dc)
    elif total > 1000:
        code = "ONE"
        dc = random.choice(one_dc)

    print("Discount code available: ", code+dc)
    response = input("Would you like to use it? y/n: ")
    if response == 'y':
        total = int(total*((100-int(dc))*0.01))
        print("TOTAL AFTER DISCOUNT: ", total)

    print("Thank you for your purchase!")

print("Welcome! \n"
      "\t Type \"list\" to list all products,\n "
      "\t \"cart\" to show cart, \n "
      "\t enter the name of a product to add to \"cart, \n"
      "\t or checkout to check out!")

while True:
    prod = input("Input: ")

    if prod == 'list':
        print_prods()
    elif prod in products.keys():
        db = int(input("How many would you like to add? "))
        if prod in cart.keys():
            cart[prod] += db
        else:
            cart[prod] = db
    elif prod in "cart":
        print_cart()
    elif prod in "checkout":
        checkout()
