pizzas = ['Lazania', 'Tikka', 'Fagita']
friend_pizzas = pizzas[:]

pizzas.append('Paproni')
friend_pizzas.append('Achari')
print("My favourite pizzas are:")
for pizza in pizzas:
    print(pizza)
print("\nMy friend's favourite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
