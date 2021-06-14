# Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

nome = str(input('Em que cidade você nasceu? ')).strip()
print('Seu nome tem Silva? {}'.format('SILVA' in nome.upper()))