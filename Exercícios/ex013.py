#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento

sal = float(input('Qual é o salário do funcionário? R$'))
novo = sal+(sal*15/100)
print('O funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(sal, novo))