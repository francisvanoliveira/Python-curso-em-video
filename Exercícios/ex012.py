#Faça um algoritimo que leia o preço de um produto e mostre seu novo preço com 5% de desconto

preco = float(input('Qual é o preco do produto? R$'))
novo = preco-(preco*5/100)
print('O produto que custava R${:.2f}, na promoção de 5% vai custar R${:.2f}'.format(preco, novo))