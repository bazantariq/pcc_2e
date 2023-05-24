dream_vacations = {}

polling_active = True

while polling_active:
    place = input("If you could vist one place in the world, where would you go? :")

    dream_vacations[place] = place
    repeat = input("do you want any other to take chance? (yes/no):")
    if repeat == 'no':
        polling_active = False


print("\n--- poll result ---")
for place, place in dream_vacations.items():
    print("I would like to go " + place)
