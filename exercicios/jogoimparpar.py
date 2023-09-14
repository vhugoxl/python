from random import randint

while True:
    jogador = int(input('Digite um valor:'))
    computador = randint(0,100)
    total = jogador + computador
    tipo = '' 
    while tipo not in 'PpIi':  
        tipo = str(input('Par ou Impar ?')).stripp().upper()[0]
    print(f'Jogador jogou {jogador} e computador jogou {computador} total de {total}')