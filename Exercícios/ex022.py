#Crie um programa que leia o nome completo de uma pessoa e moste:
#-O nome com todas as letras maiúsculas e minúsculas.
#-Qunatas letras ao todos. (sem considerar espaços)
#-Quantas letras tem o primeiro nome.


nome = str(input('Digite seu nome completo: ')).strip()
print('Analizando seu nome...')
print('Seu nome em maiúsculo é {}'.format(nome.upper()))
print('Seu nome em minúsculo é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa=nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))
