#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math
angulo = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('O ângulo de {} tem p SENO de {:.2f}'.format(angulo, seno))
print('O ângulo de {} tem p COSSENO de {:.2f}'.format(angulo, cosseno))
print('O ângulo de {} tem p TANGENTE de {:.2f}'.format(angulo, tangente))


'''from math import radians, sin, cos, tan
angulo = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('O ângulo de {} tem p SENO de {:.2f}'.format(angulo, seno))
print('O ângulo de {} tem p COSSENO de {:.2f}'.format(angulo, cosseno))
print('O ângulo de {} tem p TANGENTE de {:.2f}'.format(angulo, tangente))'''