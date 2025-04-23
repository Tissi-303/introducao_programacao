#Entrada de dados
clubes = [
    'Malasia',
    'China',
    'Gabão',
    'Malta'
]

seleçao = input('Digite a seleção desejada: ')
find = False

for i in range(len(clubes)):

    if clubes.upper() == clubes[i].upper():
        print('A seleção encontrada foi {clubes}')
        find = True

#Saída de dados

if find:
    print('Achei!')
else:
    print('Não achei!')