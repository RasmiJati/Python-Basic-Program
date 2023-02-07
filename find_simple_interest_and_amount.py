# Program to find simple interest and amount

def find_simple_interest_and_amount():
    principal = input("Enter the principal : ")
    rate = input("Enter the rate : ")
    time = input("Enter the time : ")
    principal = int(principal)
    rate = int(rate)
    time = int(time)
    interest = (principal * rate * time) / 100
    amount = principal + interest

    print(f"Simple Interest = {interest} and Amount = {amount} from the value of principal {principal}  rate {rate} % and time ={time} days ")


find_simple_interest_and_amount()

