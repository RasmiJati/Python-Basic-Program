# program to input an arbitrary number and find out whether it is positive or negative


def find_positive_or_negative():
    num = input("Enter a number : ")

    if int(num) >= 0:
        print(f"{num} is positive number!! ")
    else:
        print(f"{num} is negative number!!")


find_positive_or_negative()

