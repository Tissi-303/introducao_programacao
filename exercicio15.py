#Faça um programa que receba um número e que calcule a tabuada desse número.

#for

numero = int(input('Digite o numero da tabuada'))

for m in range(1, 11):
    print(f'{numero} x {m} = {numero * m}')

#while

ciclos = 1

while ciclos <= 10:
    resultado= numero * ciclos
    print (f'{numero} x {ciclos} = {resultado}')
    #incremento
    ciclos += 1