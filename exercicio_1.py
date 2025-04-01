class imparError(Exception):
    pass

try:
    n = int(input("Digite um número: "))
    if n % 2 == 0:
        print(f"{n} é par.")
    elif n % 2 != 0:
        raise imparError("Infelizmente o número digitado é impar, aqui só trabalhamos com números pares. Tenta denovo...")
    
except imparError as err:
    print(err)
