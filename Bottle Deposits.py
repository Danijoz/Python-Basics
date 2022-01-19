from unicodedata import decimal

lessoneliter = int(input('Enter number of drink containers holding one liter or less: '))
moreoneliter = int(input('Enter number of drink containers holding more than one liter: '))

Refund = float((lessoneliter*0.10) + (moreoneliter*0.25))

print("The refund amount is:$%.2f" %Refund)