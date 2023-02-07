def find_quotient_and_remainder():
    num1 = input("Enter 1st number : ")
    num2 = input("Enter 2nd number : ")
    quotient = int(num1) / int(num2)
    remainder = int(num1) % int(num2)

    print(f"Quotient of {num1} and {num2} is {quotient.__round__(4)}")
    print(f"Remainder of {num1} and {num2} is {remainder}")


find_quotient_and_remainder()
