class strError(Exception):
    pass

while True:

    try:
        str1 = str(input("Digite um texto: "))
        str2 = str(input("Digite um texto: "))

        if  len(str1) == len(str2):
            print(f"'{str1}' e '{str2}' tem a mesma quantidade de caracteres: {len(str1)}")
            break
        else:
            raise strError("Infelizmente comprimento das strings são diferentes... Tente novamente.")
        
    except strError as err:
        print(err)