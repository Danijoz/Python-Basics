deposited = int(input("Enter the amount of money deposited:"))
interest = 4
amount_year1 = float(((interest*deposited) / 100) + deposited)
amount_year2 = float(((interest*amount_year1) / 100) + amount_year1)
amount_year3 = float(((interest*amount_year2) / 100) + amount_year2)
print("Balance after first year:$%.2f" %amount_year1)
print("Balance after second year:$%.2f" %amount_year2)
print("Balance after three year:$%.2f" %amount_year3)