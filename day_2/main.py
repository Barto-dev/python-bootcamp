print("Welcome to the tip calculator")

bill = float(input("What was the total bill?\n$"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15\n"))
people = int(input("How many people to split the bill?\n"))

# another way to calculate
# bill_with_tip = tip / 100 * bill + bill;
# bill_per_person = round(bill_with_tip / people, 2)

total_tip_amount = bill / 100 * tip
bill_with_tip = bill + total_tip_amount;
bill_per_person = "{:.2f}".format(bill_with_tip / people)

print(f"Each person should pay: ${bill_per_person}")