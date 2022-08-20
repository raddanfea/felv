categories = {}
products = {}
customers = {}
orders = {}

product_data = ["ID", "ProductID", "Quantity", "TotalPrice", "CustomerID", "Status"]


def get_next_id(dictionary: dict):
    keys = dictionary.keys()
    if keys:
        return max(keys) + 1
    else:
        return 0


def print_options(what_to, name="MENU"):
    print(f" {name} ".center(32, '='))
    print(f'\t {"ID".ljust(3)} \t {"OPTION".ljust(5)}')
    for x, each in enumerate(what_to):
        print(f'\t {str(x).ljust(3)} \t {str(each).ljust(5)}')


def insert_category():
    cat_id = get_next_id(categories)
    cat = cat_id, input("Category Name: "), input("Description: ")
    categories[cat_id] = cat


def show_category():
    print(" CATEGORIES ".center(32, '='))
    print(f'\t ID \t {"Name".ljust(15)} \t Description')
    for cat_id, name, description in categories.values():
        print(f'\t {str(cat_id).ljust(5)} \t {name.ljust(15)} \t {description}')


def insert_product():
    prod_id = get_next_id(products)
    prod_name, prod_price = input("Product Name: "), input("Price: ")
    while True:
        cat_id = int(input("Category ID: "))
        if cat_id in categories.keys():
            break
        if cat_id == -1:
            return 0
        print("Invalid ID, try again or type -1 to quit!")
    prod = prod_id, prod_name, prod_price, cat_id
    products[prod_id] = prod


def show_products():
    print(" PRODUCTS ".center(32, '='))
    print(f'\t ID \t {"Name".ljust(15)} \t {"Price".ljust(15)} \t CategoryID')
    for product_id, name, price, cat_id in products.values():
        print(f'\t {str(product_id).ljust(5)} \t {name.ljust(15)} \t {price.ljust(15)} \t {cat_id}')


def insert_customer():
    cust_id = get_next_id(customers)
    cust = cust_id, input("Email: "), input("Number: "), input("Address: "), input("Location: "), input("Country: ")
    customers[cust_id] = cust


def show_customers():
    c_data = ["ID", "Email", "Number", "Address", "Location", "Country"]
    print(" CUSTOMERS ".center(32, '='))
    for each in c_data:
        print(each.ljust(len(each) * 3), end="")
    print("")
    for customer in customers.values():
        for i, data_point in enumerate(customer):
            print(str(data_point).ljust(len(c_data[i]) * 3), end="")
        print("")


def insert_order():
    order_id = get_next_id(orders)
    while True:
        product_id = int(input("Product ID: "))
        if product_id in products.keys():
            break
        if product_id == -1:
            return 0
        print("Invalid ID, try again or type -1 to quit!")

    quantity = int(input("Quantity: "))

    total_price = int(products[product_id][2]) * quantity

    while True:
        customer_id = int(input("Customer ID: "))
        if customer_id in customers.keys():
            break
        if customer_id == -1:
            return 0
        print("Invalid ID, try again or type -1 to quit!")

    status_types = ["Delivered", "Shipping"]

    while True:
        status = input("Status Delivered/Shipping: ").capitalize()
        if status in status_types:
            break
        print("Invalid status, try again or type -1 to quit!")

    order = order_id, product_id, quantity, total_price, customer_id, status
    orders[order_id] = order


def show_orders():
    print(" ORDERS ".center(32, '='))
    for each in product_data:
        print(each.ljust(len(each) + 3), end="")
    print("")
    for order in orders.values():
        for i, data_point in enumerate(order):
            print(str(data_point).ljust(len(product_data[i]) + 3), end="")
        print("")


def sales_by_product_id():
    total_num, total_price = 0, 0

    while True:
        product_id = int(input("Product ID: "))
        if product_id in products.keys():
            break
        if product_id == -1:
            return 0
        print("Invalid ID, try again or type -1 to quit!")

    print(" FILTERED ORDERS ".center(32, '='))
    for each in product_data:
        print(each.ljust(len(each) + 3), end="")
    print("")
    for order in orders.values():
        if order[1] == product_id:
            total_num += order[2]
            total_price += order[3]
            for i, data_point in enumerate(order):
                print(str(data_point).ljust(len(product_data[i]) + 3), end="")
            print("")
    print("TOTAL NUMBER: ", total_num, "\t", "TOTAL PRICE: ", total_price)


def sales_by_category():
    total_num, total_price = 0, 0

    while True:
        category_id = int(input("Category ID: "))
        if category_id in categories.keys():
            break
        if category_id == -1:
            return 0
        print("Invalid ID, try again or type -1 to quit!")

    print(" FILTERED ORDERS ".center(32, '='))
    for each in product_data:
        print(each.ljust(len(each) + 3), end="")
    print("")
    for order in orders.values():
        prod_id = order[1]
        if products[prod_id][2] == category_id:
            total_num += order[2]
            total_price += order[3]
            for i, data_point in enumerate(order):
                print(str(data_point).ljust(len(product_data[i]) + 3), end="")
            print("")
    print("TOTAL NUMBER: ", total_num, "\t", "TOTAL PRICE: ", total_price)


def sales_by_location():
    total_num, total_price = 0, 0

    location = input("Location: ")

    print(" FILTERED ORDERS ".center(32, '='))
    for each in product_data:
        print(each.ljust(len(each) + 3), end="")
    print("")
    for order in orders.values():
        customer_id = order[4]
        if customers[customer_id][4] == location:
            total_num += order[2]
            total_price += order[3]
            for i, data_point in enumerate(order):
                print(str(data_point).ljust(len(product_data[i]) + 3), end="")
            print("")
    print("TOTAL NUMBER: ", total_num, "\t", "TOTAL PRICE: ", total_price)


options_outer = ["Categories", "Products", "Customers", "Orders", "Sales"]
options_inner = ["Add", "Show"]
options_sales = ["ProductID", "Category", "Sort", "Location"]
options_sort = ["Low to high", "High to low"]

def test():
    categories[0] = (0, "name1", "description1")
    categories[1] = (1, "name2", "description2")
    products[0] = ("test1", 5, 0)
    products[1] = ("test2", 10, 1)
    customers[0] = (1, 2, 3, 4, "loc2", 6)
    customers[1] = (1, 2, 3, 4, "loc1", 6)
    orders[0] = (0, 0, 3, 15, 0, "status")
    orders[1] = (1, 0, 4, 20, 0, "status")
    orders[3] = (3, 1, 4, 40, 1, "status")


def sales_sorted_by_price(reverse):
    print(" SORTED ORDERS ".center(32, '='))
    for each in product_data:
        print(each.ljust(len(each) + 3), end="")
    print("")
    for order in sorted(orders.values(), key=lambda x: x[3], reverse=reverse):
        for i, data_point in enumerate(order):
            print(str(data_point).ljust(len(product_data[i]) + 3), end="")
        print("")


if __name__ == '__main__':
    # test() # adding some default data for testing
    while True:
        print_options(options_outer)
        folder = int(input("Choose Instruction:  "))
        match folder:
            case 0:
                print_options(options_inner, name=options_outer[folder])
                sub_folder = int(input("Choose Instruction:  "))
                if sub_folder:
                    show_category()
                else:
                    insert_category()
            case 1:
                print_options(options_inner, name=options_outer[folder])
                sub_folder = int(input("Choose Instruction:  "))
                if sub_folder:
                    show_products()
                else:
                    insert_product()
            case 2:
                print_options(options_inner, name=options_outer[folder])
                sub_folder = int(input("Choose Instruction:  "))
                if sub_folder:
                    show_customers()
                else:
                    insert_customer()
            case 3:
                print_options(options_inner, name=options_outer[folder])
                sub_folder = int(input("Choose Instruction:  "))
                if sub_folder:
                    show_orders()
                else:
                    insert_order()
            case 4:
                print_options(options_sales, name=options_outer[folder])
                sub_folder = int(input("Choose Instruction:  "))
                match sub_folder:
                    case 0:
                        sales_by_product_id()
                    case 1:
                        sales_by_category()
                    case 2:
                        print_options(options_sort, "SORT")
                        sub_folder = int(input("Choose Instruction:  "))
                        sales_sorted_by_price(sub_folder)
                    case 3:
                        sales_by_location()
