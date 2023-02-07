# Program to convert entered seconds into hours, minutes and remaining second

def second_converter():
    seconds = input("Enter time in second : ")
    hour = int(seconds) / 3600
    minutes = int(seconds) / 60
    remaining_second = int(seconds) % 60

    print(f"Hours = {hour.__round__(2)}  Minutes = {minutes.__round__(2)}  and  Remaining Seconds = {remaining_second}")


second_converter()


