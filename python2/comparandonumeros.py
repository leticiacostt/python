'''
DESAFIO 38
Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
– O primeiro valor é maior
– O segundo valor é maior
– Não existe valor maior, os dois são iguais
'''
numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
if numero1 > numero2:
    print('O primeiro valor é maior!')
elif numero1 < numero2:
    print('O segundo número é maior!')
else:
    print('Os número são iguais!')
