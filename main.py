# Author: Fransiskus Agapa

# ========================
# simple program to pratice sort
# data is in tuple of lists, tuple has to be made a list before sort its data
# ========================

name = lambda the_name: the_name[0]
color = lambda the_color: the_color[1]
age = lambda the_age: the_age[2]

wild_animal = (("Cobra", "Green", 3),
               ("Tiger", "White", 4),
               ("Eagle", "Brown", 2),
               ("Goat", "Gray", 5),
               ("Crocodile", "Black", 1))

print("\n== Wild Animal Database ==")
print("1. Display data")
print("2. Display - Sort by name")
print("3. Display - Sort by color")
print("4. Display - Sort by age")
print("e. Exit")
choice = input("choice: ").lower()

while choice != 'e':
    if choice == '1':
        print("\n = Display Data =\n")
        for i in wild_animal:
            print(i)

    elif choice == '2':
        print("\n = Display - Sort by name =\n")
        sorted_list = sorted(wild_animal, key=name)            # since the type is tuple, so it has be made a list first
        for i in sorted_list:
            print(i)

    elif choice == '3':
        print("\n = Display - Sort by color =\n")
        sorted_list = sorted(wild_animal, key=color)
        for i in sorted_list:
            print(i)

    elif choice == '4':
        print("\n = Display - Sort by age =\n")
        sorted_list = sorted(wild_animal, key=age)
        for i  in sorted_list:
            print(i)

    else:
        print("\n[ Invalid choice ]")

    choice = input("\nchoice: ")

print("\n== Exit Program ==")
