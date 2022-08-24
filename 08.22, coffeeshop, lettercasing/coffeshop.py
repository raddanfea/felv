# Rádi Dániel 2022.08.22, coffeeshop, lettercasing 18:20

print("Welcome to the CoffeeShop :TM:")

size_options = ["small", "medium", "large"]
coffee_type_options = ["brew", "espresso", "cold brew"]
flavor_options = ["none", "hazelnut", "vanilla", "caramel"]

size, coffee_type, flavor = "", "", ""
while size.lower() not in size_options:
    size = input("Select size: Small, Medium, Large: ").upper()
while coffee_type.lower() not in coffee_type_options:
    coffee_type = input("Type: Brew, Espresso, Cold brew: ").upper()
while flavor.lower() not in flavor_options:
    flavor = input("Flavoring: None, Hazelnut, Vanilla, Caramel: ").upper()

print("Your order:")
print("Size: ", size)
print("Type: ", coffee_type)
print("Flavor: ", flavor)

cost = 0
if size == "small".upper():
    cost += 2
elif size == "medium".upper():
    cost += 3
else:
    cost += 4

if coffee_type == "Espresso".upper():
    cost += 0.5
elif coffee_type == "Cold brew".upper():
    cost += 1

if flavor != "none".upper():
    cost += 0.5


print("Cost before service: ", f'{cost} $', " \t Service charge 15% \n \t    Total Price: ", f"{round(cost * 1.15, 2)} $")
