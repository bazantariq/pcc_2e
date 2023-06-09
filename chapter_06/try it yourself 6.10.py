favourite_numbers = {
    "Ali": ['65', '35', '67'],
    "Ahmad": ['89', '45', '56'],
    "Sana": ['24', '78', '45'],
    "Sara": ['45', '98', '89'],
    "Saba": ['34', '23', '67']
}

for name, numbers in favourite_numbers.items():
    print(name + "'s favourite numbers are:")
    for number in numbers:
        print("\t" + number)
