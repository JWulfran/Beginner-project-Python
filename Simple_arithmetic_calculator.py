# Python calculator

operator = input("Veuillez choisir un opérateur (+, -, *, /):")
num1 = float(input("Entrez un nombre: "))
num2 = float(input("Entrez un autre nombre: "))

if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    result = num1 / num2
else:
    print("Opérateur invalide : Veuillez choisir un des opérateurs suivants: +, -, *, /")

print(f"{num1} {operator} {num2} = {result}")