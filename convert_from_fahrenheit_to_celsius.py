# Program to convert a temperature reading in degree fahrenheit to
# degree celsius using the formula c = (5/9) * (f-32)

def fahrenheit_to_celsius():
    fahrenheit = input("Enter degree in fahrenheit : ")
    celsius = 0.56 * (float(fahrenheit) - 32)  # 5/9 = 0.56

    print(f"Conversion from {fahrenheit} degree fahrenheit to celsius is {celsius.__round__(2)} degree celsius")


fahrenheit_to_celsius()
