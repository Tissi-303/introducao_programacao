nome_arquivo = 'arquivo.txt'
numero = int(input('digite o número desejado: '))

with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:

    for m in range(1, 11):
        resultado = numero * m
        arquivo.write(f'{numero} x {x} = {resultado}\n')
    print('programa finalizado')