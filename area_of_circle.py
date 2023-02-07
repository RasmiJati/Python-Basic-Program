# program to find area of circle


def area_of_circle():
    radius = input("Enter radius of circle : ")
    # area = pi * r^2 so
    pi = 3.14  # 22/7 equivalent to 3.14
    radius = float(radius)
    area = pi * radius * radius

    print("Area of circle is ", area)


area_of_circle()
