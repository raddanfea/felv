# pizza 200
# burger 150
# pasta 180
# exit


items = ["Pizza", "Burger", "Pasta", "Exit"]
cost = [200, 150, 180, ""]

ordered_number = [0] * len(items)
total_sum = 0


def show_menu():
    print("ID", "NAME", "COST")
    for x, each in enumerate(items):
        print(x + 1, each, cost[x])


while True:
    show_menu()
    item = eval(input("What would you like to order?"))

    if type(item) is not int:
        print("Invalid input")
        continue

    if item == len(items):
        break

    if not 0 <= item <= len(items):
        print("Item doesn't exist.")
        continue

    amount = eval(input("How many?"))
    if type(amount) is not int:
        print("Invalid input")
        continue

    ordered_number[item - 1] += int(amount)

for x, number in enumerate(ordered_number):
    if number == 0: continue

    print(items[x], number, number * cost[x])
    total_sum += number * cost[x]

print("----------")
print("SUM:", total_sum, "$")
