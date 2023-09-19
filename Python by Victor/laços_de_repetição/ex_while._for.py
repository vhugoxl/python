soma = 0  
for numero in range (1,5):
    soma += float(input(f'Digite a nota do Bimestre {numero}: ').replace(',',','))
print(f'A soma de tudo é {soma}')  
print(f'Sua média é {soma / 4}')
