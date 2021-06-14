#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

num = int(input('Digite um número: '))
if (num % 2) == 0:
    print('Numero {} é PAR'.format(num))
else:
    print('Numero {} é IMPAR'.format(num))