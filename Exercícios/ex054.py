#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date
atual = date.today().year
maior = 0
menor = 0
for c in range(1, 8):
    ano = int(input('Em que ano a {}º pessoa nasceu? '.format(c)))
    idade = atual - ano
    if idade >=18:
        maior += 1
    else:
        menor += 1
print('MAIOR IDADE {}'.format(maior))
print('MENOR DE IDADE {}'.format(menor))
