def fizzbuzz(numero_max: int):

    lista = []

    for numero in range(1, numero_max+1):
        imprimiu_palavra = False
        palavra = ''

        if numero % 2 == 0:
            palavra += 'fizz'
            imprimiu_palavra = True

        if numero % 5 == 0:
            palavra += 'buzz'
            imprimiu_palavra = True

        if not imprimiu_palavra:
            palavra += str(numero)
        
        lista.append(palavra)
    
    return lista


if __name__ == "__main__":
    print(fizzbuzz(15))
