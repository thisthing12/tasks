""" to get children sorted into two programs
"""


def fun_in_sun():
    number2 = int(input("Enter the childs age: "))
    if number2 == 5:
        roll.append(1)
    elif number2 == 6:
        roll.append(1)
    elif number2 == 7:
        roll.append(1)
    elif number2 == 8:
        roll.append(1)
    elif number2 == 9:
        roll.append(1)
    elif number2 == 10:
        roll.append(1)
    elif number2 == 11:
        roll.append(1)
    elif number2 == 12:
        roll.append(1)
    elif number2 == 13:
        roll.append(1)
    elif number2 == 14:
        roll.append(1)
    elif number2 == 15:
        roll.append(1)
    elif 5 > number2:
        print("Your child is too young")
    else:
        print("Your child is too old")
    return main


def active_kidz():
    number3 = int(input("Enter the childs age: "))
    if number3 == 5:
        roll.append(1)
    elif number3 == 6:
        roll.append(1)
    elif number3 == 7:
        roll.append(1)
    elif number3 == 8:
        roll.append(1)
    elif number3 == 9:
        roll.append(1)
    elif number3 == 10:
        roll.append(1)
    elif number3 == 11:
        roll.append(1)
    elif number3 == 12:
        roll.append(1)
    elif number3 == 13:
        roll.append(1)
    elif number3 == 14:
        roll.append(1)
    elif number3 == 15:
        roll.append(1)
    elif 5 > number3:
        print("Your child is too young")
    else:
        print("Your child is too old")
        return main


def display_children():
    print(f"{roll}")


# Main routine
roll = []
main = roll

print("------------------------------------------------------------------")
print("Welcome to Kidz fun what holiday program would you like to do?")
print("------------------------------------------------------------------")
print("1 Fun in the sun")
print("2 Active kidz")
print("3 Display number of children")
number = int(input("Enter a number between 1 and 3: "))
if number == 1:
    fun_in_sun()
elif number == 2:
    active_kidz()
elif number == 3:
    display_children()
else:
    print("That is not a number between 1 and 3")
