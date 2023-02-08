# program to calculate weight based on the input.
# If weight in kg then convert to lbs and vice-versa.


def weight_calculator():
    weight = input("enter your weight : ")
    unit = input("Enter unit (K) for kg or (L) for Lbs : ")
    weight = float(weight)
    if unit.upper() == "K":
        converted_weight = weight / 0.45
        print(f"Weight in Lbs : {converted_weight.__round__(2)}")

    else:
        converted_weight = weight * 0.45
        print(f"Weight in Kgs : {converted_weight.__round__(2)}")


weight_calculator()