print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip_as_percent = int(input("How much tip would you like to give? 10, 12, or 15? "))
split = int(input("how many people to split the bill? "))
tip = tip_as_percent / 100
total_bill = bill * (1 + tip)
bill_per_person = round(total_bill/split,2)
print(f"Each person should pay: ${bill_per_person}")