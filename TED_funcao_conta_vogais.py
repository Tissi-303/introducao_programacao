def conta_vogais(frase):
    vogais = 'aeiouAEIOU'
    contador = 0
    for letra in frase:
        if letra in vogais:
            contador += 1
    return contador

frase = input ("digite uma frase ou palavra: ")
resultado = conta_vogais(frase)
print('Número de vogais:', resultado)
