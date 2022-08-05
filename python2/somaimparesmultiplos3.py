''' DESAFIO 48
Faça um programa que calcule a soma entre todos os números que são múltiplos de três e 
que se encontram no intervalo de 1 até 500.
'''
#exercicio com conceito de acumulador e contador
soma = 0 #somma vai começar com 0
cont = 0 #começar a contar do 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c #soma = soma + c
        cont += 1 #cont = cont + 1
print("A soma de todos os {} valores solicitados é {}".format(cont, soma)) 
       