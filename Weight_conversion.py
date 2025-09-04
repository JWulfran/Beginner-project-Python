# Python Weight Conversion

weight = float(input("Entrez le poids: "))
unit = input("Choisissez une unité (K pour kilogrammes, L pour livres): ")

if unit == 'K':
    weight = weight * 2.20462
    unit = 'Lbs'
elif unit == 'L':
    weight = weight / 2.20462
    unit = 'Kg'
else:
    print(f"{unit} n'est pas valide")

print(f"Le poids est de {round(weight, 2)} {unit}")