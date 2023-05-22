sandwich_orders = ['chicken sandwich', 'vegetable sandwich', 'tikka sandwich', 'egg sandwich', 'cheese sandwich']
finished_sandwiches = []

while sandwich_orders:
    for each_sandwich in sandwich_orders:
        print("I made your " + each_sandwich)
        break

    finished_sandwich = sandwich_orders.pop()
    finished_sandwiches.append(finished_sandwich)

for finished_sandwich in finished_sandwiches:
    print(finished_sandwich + " was made.")
