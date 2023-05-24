sandwich_orders = ['chicken sandwich', 'tikka sandwich', 'vegetable sandwich', 'pastrami sandwich', 'egg sandwich',
                   'pastrami sandwich', 'cheese sandwich', 'pastrami sandwich']
finished_sandwiches = []

print(sandwich_orders)

print("\nDeli has run out of pastrami sandwich.\n")

while "pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("pastrami sandwich")

print(sandwich_orders)
