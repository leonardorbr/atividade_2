try:
    n = int(input("Digite um número inteiro não nulo: "))
    divisao = 10 / n
    print(f"O resultado da divisão '10/{n}' é igual à {divisao:.2f}")

except ZeroDivisionError:
    print("Amigão, você tentou dividir um número por 0, e isso não funciona")