import random

opções = ['pedra', 'papel', 'tesoura']

computador = random.choice(opções)

jogada = input('\nEscolha pedra, papel ou tesoura: ')

print(f'\nO computador escolheu {computador}\n')

if jogada == computador:
    print('empate\n')
elif (jogada == 'pedra' and computador == 'tesoura') or (jogada == 'papel' and computador == 'pedra') or (jogada == 'tesoura' and computador == 'papel'):
    print('você ganhou\n')
else:
    print('você perdeu\n')