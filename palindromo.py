# 6 - Verificando se uma palavra é um palídromo

palavra = input("Digite uma palavra: ").strip().lower() # Remove espaços extras e converte para minúsculas

if palavra == palavra[::-1]:
    print("A palavra digitada é um palídromo!")
else:
    print("A palavra digitada não é um palídromo!")