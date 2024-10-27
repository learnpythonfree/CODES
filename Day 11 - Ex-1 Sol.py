# calculator solution

print('calculator by me')

intA = int(input("Enter First Number: "))
sign = input("Enter Your Operation: ")
intB = int(input("Enter Second Number: "))

if sign == '+':
    print(intA+intB)
elif sign == '*':
    print(intA*intB)
elif sign == '-':
    print(intA-intB)
elif sign == '/':
    print(intA/intB)
else:
    print("Error4000004")

input()