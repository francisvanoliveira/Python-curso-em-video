#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

medida = float(input('Uma distância em metros: '))
mm = medida*1000
cm = medida*100
dm = medida*10
dam = medida/10
hm = medida/100
km = medida/1000

print('A medida de {}m'.format(medida))
print('Quilômetro {:.0f}Km'.format(km))
print('Hectômetro {:.0f}hm'.format(hm))
print('Decâmetro {:.0f}Km'.format(dam))
print('Decímetro {:.0f}dm'.format(dm))
print('Centímetro {:.0f}cm'.format(cm))
print('Milímetro {:.0f}mm'.format(mm))