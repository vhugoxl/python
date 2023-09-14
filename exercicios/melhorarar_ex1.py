from datetime import date

nome = str(input("Olá qual é seu nome \n Digite  seu nome:"))
dianasc = int(input("Digite o dia que você nasceu: "))
mesnasc = int(input("Digite o mês que você nasceu: "))
anonasc = int(input("Digite o ano que você nasceu: "))
diaatual = int(date.today().day)
mesatual = int(date.today().month)
anoatual = int(date.today().year)

ano = anoatual - anonasc
if(mesnasc > mesatual):
    print(f'Sua idade é: {ano} anos')
ano = ano -1
if(mesnasc >mesatual):
    print(f'Sua idade é {ano} anos')
ano = anoatual-anonasc
if(mesnasc == mesatual and dianasc < diaatual):
    print(f'Sua idade é: {ano} anos')
ano = anoatual - anonasc
ano = ano -1
if(mesnasc == mesatual and dianasc > diaatual):
    print(f'Sua idade é {ano} anos')
ano = anoatual - anonasc
if(mesnasc ==mesatual and dianasc == diaatual):
    print('Sua idade é {ano} anos')
    
    
    
    