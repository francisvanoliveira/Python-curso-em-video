#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#– Até 9 anos: MIRIM
#– Até 14 anos: INFANTIL
#– Até 19 anos: JÚNIOR
#– Até 25 anos: SÊNIOR
#– Acima de 25 anos: MASTER

from datetime import date
atual = date.today().year
ano = int(input('Data de nascimento: '))
idade = atual-ano
print('O atelta tem {} anos'.format(idade))
if idade <= 9:
    print('Atelta MIRIM')
elif idade <= 14:
    print('Atelta INFANTIL')
elif idade <= 19:
    print('Atelta JÚNIOR')
elif idade <= 25:
    print('Atleta SÊNIOR')
else:
    print('Atleta MASTER')
