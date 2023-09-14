from datetime import date

nome = str(input("Olá qual é seu nome?\nDigite seu nome: "))
mes = int(input("Digite o seu mes de nascimento: "))
dia = int(input("Digite o dia do seu nascimento: "))
anonascimento = int(input("Digite o ano do seu nascimento: "))
anoatual= date.today().year
idade = anoatual - anonascimento
print(f"O nome é: {nome}")
print(f"Data de nascimento é: {dia}/{mes}/{anonascimento} e sua idade é {idade}")


