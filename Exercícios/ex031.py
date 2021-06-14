#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

distancia = float(input('Digite a distancia do destino: '))
print('Viagem de {:.2f}Km'.format(distancia))
if distancia <= 200:
    valor = distancia * 0.50
    print('Valor da passagem é R${:.2f}'.format(valor))
else:
    valor = distancia * 0.45
    print('Valor da passagem é R${:.2f}'.format(valor))
