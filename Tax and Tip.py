Meal_price = float(input("Enter the price of meal:"))

tax_price = (7 * Meal_price) / 100

tip_price = (18 * Meal_price) / 100

total_price = Meal_price + tax_price + tip_price

print("Meal Price:$%.2f" %Meal_price)
print("Tax Price :$%.2f" %tax_price)
print("Tip       :$%.2f" %tip_price)
print("Total Price:$%.2f" %total_price)