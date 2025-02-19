# 5 - Calcular média

nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))
nota3 = float(input("Informe a terceira nota: "))

calcular_media = (nota1 + nota2 + nota3) / 3

# Limitando a casa decimal de forma simples com round
#print("Sua média foi: ", round(calcular_media, 1))

# Limitando casa decimal com f-strings
print(f"Sua média foi: {calcular_media:.1f}")