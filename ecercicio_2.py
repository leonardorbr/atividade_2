class caseError(Exception):
    pass

while True:

    try:
        texto = str(input("Digite um texto: "))
        if texto.lower() == texto:
            print(f"'{texto}', tem apenas letras minusculas")
            break
        else:
            raise caseError("Infelizmente o text digitado é contém letras MAIUSCULAS. tente novamente...")
        
    except caseError as err:
        print(err)