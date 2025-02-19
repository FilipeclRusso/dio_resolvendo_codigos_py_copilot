# 3 - Operações matemáticas simples

numero1 = int(input("Insira um número inteiro: "))
numero2 = int(input("Insira outro número inteiro: "))

operacao = input("Digite uma operação (+ | - | * | /): ")

if operacao == "+":
    print(numero1 + numero2)
elif operacao == "-":
    print(numero1 - numero2)
elif operacao == "*":
    print(numero1 * numero2)
elif operacao == "/":
    if numero2 != 0: # Verificação para não dividir por 0
        print(numero1 / numero2)
    else:
        print("Não é possível dividir por zero")
else:
    print("Operação inválida")