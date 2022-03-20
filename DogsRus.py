""" getting the names of dogs that are staying at the boarding house
"""


def main():
    print("********** DogsRus **********")
    while(True):
        response = input("Do you want to use our services? (Y/N): ").upper()
        if response == "N":
            print("Have a nice day")
            return
        elif response == "Y":
            use_service()
        else:
            print("That isn't Yes or No")


def use_service():
    while(True):
        print("Chose one of the following options:")
        print("""
        1. Dog drop off
        2. Pick one up 
        3. Print a list of all dogs currently staying
        4. Calculate the amount to charge for the stay 
        5. Exit the program
        """)
        choice = int(input(">>> "))
        if choice == 1:
            drop_off_dog()
        elif choice == 2:
            pick_one_up()
        elif choice == 3:
            print_dog_list()
        elif choice == 4:
            charge_amount()
        elif choice == 5:
            print("Have a nice day")
        else:
            print("That wasn't a valid answer")


def drop_off_dog():
    name = input("What is the dogs' name? ")
    lists = [name, ]
    print(f"Dropped of {lists}")
    return

def pick_one_up():
    name2 = input("What is the dogs' name? ")
    print("Here you go")
    if name2 !=


def print_dog_list():
    dog_list = input(f"{lists}")
    return

def charge_amount():
    return


main()
