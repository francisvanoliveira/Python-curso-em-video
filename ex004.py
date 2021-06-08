#Faça um programa que leia algo do teclado e mostre na tela:
#O tipo primitivo
#E todas as outras informações possíveis sobre ele

x = input('Digite algo: ')
print('O tipo primitivo desse valor é ',type(x))
print('So tem espaço? ', x.isspace())
print('É um número ', x.isnumeric())
print('É alfabético ', x.isalpha())
print('É alfanumérico ', x.isalnum())
print('Está em maisculas? ', x.isupper())
print('Está em minúsculas? ', x.islower())
print('Está capitalizada? ', x.istitle())