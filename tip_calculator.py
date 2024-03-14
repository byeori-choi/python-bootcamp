print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip_percent = int(input("How much tip would you like to give? 10, 12, or 15? "))
split = int(input("how many people to split the bill? "))
tip = tip_percent / 100
total = bill * (1 + tip)
each_pay = round(total/split,2)
print(f"Each person should pay: ${each_pay}")