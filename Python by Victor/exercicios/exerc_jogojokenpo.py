from random import randint
from time import sleep
from colorama import init

contagemdepontos = 0
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint (0,2)
print('BEM VINDO AO JOGO JOKENPO')
print('#'*30)
print('''Escolha uma opção:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
print ('#'*30)
jogador = int(input("Escolha sua Jogada: "))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
print('Computador jogou: {}' .format(itens[computador]))
print('Jogador jogou: {}' .format(itens[jogador]))

if computador == 0: #Computador Jogou Pedra
    if jogador == 0: #Jogador Jogou Pedra
        print('EMPATE!')
    if jogador == 1: #Jogador jogou Papel
        print('VENCEU!')
        contagemdepontos +1
        print(f'Sua Pontuação é: {contagemdepontos}')
    if jogador == 2: # Jogador jogou Tesoura
        print('PERDEU!')
    

elif computador == 1: #Computador Jogou Papel
    if jogador == 0: #Jogador  Jogou Pedra
        print('PERDEU!')
    if jogador == 1: #Jogaodor Jogou Papel
        print('EMPATE!') 
    if jogador == 2: # Jogador Jogou Tesoura
        print('GANHOU!')   
     
    
elif computador == 2: #Computador Jogou Tesoura
    if jogador == 0: #Jogador Jogou Pedra
        print('PERDEU')
    if jogador == 1: #Jogador Jogou Papel
        print('GANHOU!')
    if jogador == 2: #jogador jogou tesoura
        print('EMPATE')   
    


