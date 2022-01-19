
import math

a = int(input("Enter a:"))
b = int(input("Enter b:"))
difference = b - a
product = a * b
quotient = a // b
remainder = a % b
log = math.log(a,10)
power = math.pow(a,b)

print("Difference between a and b:",difference)
print("Product of a and b:",product)
print("Quotient of a/b:",quotient)
print("Remainder a/b:",remainder)
print("Log a:",log)
print("a ^ b:",power)