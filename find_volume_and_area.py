# If A Cube has its side, its volume and surface area given by
# the formulae v = a^3 and s = 6a^2. Write a program to read side (a)
# and print the volume (v) and area ( s)

def find_volume_and_area():

    a = input("Enter side : ")  # it gives string value so convert to int using int() function
    # a = side , v = volume , s = area
    a = int(a)
    v = a * a * a
    s = 6 * a * a

    print(f"Volume = {v}  and Area = {s}")


find_volume_and_area()