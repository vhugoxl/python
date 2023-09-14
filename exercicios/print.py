#Exercicio 1

from datetime import date
nome = str(input("Olá qual é seu nome?\nDigite seu nome: "))
mes = int(input("Digite o seu mes de nascimento: "))
dia = int(input("Digite o dia do seu nascimento: "))
anonascimento = int(input("Digite o ano do seu nascimento: "))
anoatual= date.today().year
idade = anoatual - anonascimento
print(f"O nome é: {nome}")
print(f"Data de nascimento é: {dia}/{mes}/{anonascimento} e sua idade é {idade}")

#Exercicio 2

co = float(input("Digite o valor da base do catetto oposto: ").replace(",","."))
ca = float(input("Digite o valor do cateto adjacente: ").replace(",","."))
r = (ca*co)/2
print("\n**************************\n")

#Exercicio 3

print(f"O valor da base de um triângulo retângulo é: {r:.2f}m²")
peso = float(input("Digite o valor do seu peso: "))
altura = float(input("Digite o valor da sua altura: "))
r = (peso/altura**2)
print("\n**************************\n")
print(f"O valor do seu IMC: {r:.1f} ")

#Exercicio 4

celsius = float(input("Digite o numero em graus celsius: "))
print(f"Seu numero em farenheit é: {celsius*1.8+32}")

 #Exercicio 5

farenheit = float(input("Digite o numero em farenheit: "))
print(f"Seu numero em graus é: {farenheit-32/1.8}")

#Exercicio 6

a = int(input("A:"))
b = int(input("B:"))
c = int(input("C:"))
delta = float(pow(pow(b,2)-4*a*c,1/2))
print(delta)
v1 = (-b + delta)/2*a
v2 = (-b - delta)/2*a
print(f"v1 = {v1:.2f} e v2 = {v2:.2f}")