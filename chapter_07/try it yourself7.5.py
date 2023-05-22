
person_age = int(input("Enter your age: "))

while person_age:

    if person_age <= 3:
        print("your ticket is free.")

    elif person_age <= 12:
        print("your ticket is 10$.")

    elif person_age > 12:
        print("your ticket is 15$.")
    break

