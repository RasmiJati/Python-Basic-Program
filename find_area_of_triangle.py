# Take base and height from user and print area of triangle

def area_of_triangle():
    base = input("Enter value for base of triangle : ")
    height = input("Enter value for height of triangle : ")
    area = float(base) * float(height) * 0.5  # 1/2 = 0.5

    print("Area of triangle is ", area)


area_of_triangle()
