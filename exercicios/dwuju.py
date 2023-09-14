from random import randint

while True:
    jogador = int(input('Digite um valor: '))
    computador = randint (0,20)
    total = jogador + computador
    tipo = ''
    while tipo not in 'PpIi':
        tipo = str(input('Par ou Impar? ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}')
