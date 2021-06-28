# Utilizando  os  conceitos  aprendidos  até dicionários,  crie  um  programa  onde  4 jogadores joguem um dado e tenham resultados aleatórios.
from random import randint
from time import sleep
import os

listap1 = []
listap2 = []
listap3 = []
listap4 = []

vencedor = dict()

play1 = dict()
play1['Pontuacao'] = 0
play2 = dict()
play2['Pontuacao'] = 0
play3 = dict()
play3['Pontuacao'] = 0
play4 = dict()
play4['Pontuacao'] = 0

print("\n\033[3;7m ============ BEM VINDO AO JOGO DO DADO, VAMOS TESTAR A SOLTE DE NOSSOS JOGADORES ============ \033[0;0m\n")

rodadas = int(input("\033[37;1mQuantas rodadas você deseja jogar? \033[0;0m"))

print("\nJOGADORES PREPARADOS...", end=" "), print("VAMOS LÁ")
sleep(1)
os.system("cls")

for j1 in range (rodadas):
    player1 = dict()
    player2 = dict()
    player3 = dict()
    player4 = dict()
    
    print("\033[34;1;3m\nPLAYER 1 JOGOU O DADO\033[0;0m")
    sleep(0.5), print("...", end=" "), sleep(0.5), print("...", end=" "), sleep(0.5), print("...", end=" ")
    
    dado = randint(1,6)
    print(f'\nO DADO CAIU NO NÚMERO {dado}')
    sleep(1.5)
    
    player1['Jogadas'] = dado
    listap1.append(player1['Jogadas'])

    print("\033[35;1;3m\nPLAYER 2 JOGOU O DADO\033[0;0m")
    
    sleep(0.5), print("...", end=" "), sleep(0.5), print("...", end=" "), sleep(0.5), print("...", end=" ")
    dado = randint(1,6)
    
    print(f'\nO DADO CAIU NO NÚMERO {dado}')
    sleep(1.5)
    
    player2['Jogadas'] = dado
    listap2.append(player2['Jogadas'])

    print("\033[36;1;3m\nPLAYER 3 JOGOU O DADO\033[0;0m")
    sleep(0.5), print("...", end=" "), sleep(0.5), print("...", end=" "), sleep(0.5), print("...", end=" ")
    
    dado = randint(1,6)
    print(f'\nO DADO CAIU NO NÚMERO {dado}')
    sleep(1.5)
    
    player3['Jogadas'] = dado
    listap3.append(player3['Jogadas'])

    print("\033[30;1;3m\nPLAYER 4 JOGOU O DADO\033[0;0m")
    sleep(0.5), print("...", end=" "), sleep(0.5), print("...", end=" "), sleep(0.5), print("...", end=" ")
    
    dado = randint(1,6)

    print(f'\nO DADO CAIU NO NÚMERO {dado}')
    sleep(1.5)

    player4['Jogadas'] = dado
    listap4.append(player4['Jogadas'])

    os.system("cls")
    if player1['Jogadas'] > player2['Jogadas'] and player1['Jogadas'] > player3['Jogadas'] and player1['Jogadas'] > player4['Jogadas']:
        play1['Pontuacao'] += 1
        print("\033[34;3;1mPLAYER 1 VENCEU A RODADA\033[0;0m")

    elif player2['Jogadas'] > player1['Jogadas'] and player2['Jogadas'] > player3['Jogadas'] and player2['Jogadas'] > player4['Jogadas']:
        play2['Pontuacao'] += 1
        print("\033[35;3;1mPLAYER 2 VENCEU A RODADA\033[0;0m")

    elif player3['Jogadas'] > player1['Jogadas'] and player3['Jogadas'] > player2['Jogadas'] and player3['Jogadas'] > player4['Jogadas']:
        play3['Pontuacao'] += 1
        print("\033[36;3;1mPLAYER 3 VENCEU A RODADA\033[0;0m")

    elif player4['Jogadas'] > player1['Jogadas'] and player4['Jogadas'] > player2['Jogadas'] and player4['Jogadas'] > player3['Jogadas']:
        play4['Pontuacao'] += 1
        print("\033[30;3;1mPLAYER 4 VENCEU A RODADA\033[0;0m")

    else:
        print("\033[37;3mHOUVE UM EMPATE,\033[0;0m \033[31;1;3mNINGUÉM\033[0;0m \033[37;3mRECEBEU PONTOS\033[0;0m")

os.system("cls")
print('O GRANDE VENCEDOR FOI')
sleep(0.8), print("...", end=" "), sleep(0.8), print("...", end=" "), sleep(0.8), print("...")
if play1['Pontuacao'] > play2['Pontuacao'] and play1['Pontuacao'] > play3['Pontuacao'] and play1['Pontuacao'] > play4['Pontuacao']:
        print(f"\033[34;3;1mPLAYER 1\033[0;0m \033[32;1mVENCEU O JOGO\033[0;0m COM {play1['Pontuacao']} RODADAS VENCIDAS")

elif play2['Pontuacao'] > play1['Pontuacao'] and play2['Pontuacao'] > play3['Pontuacao'] and play2['Pontuacao'] > play4['Pontuacao']:
        print(f"\033[35;3;1mPLAYER 2\033[0;0m \033[32;1mVENCEU O JOGO\033[0;0m COM {play2['Pontuacao']} RODADAS VENCIDAS")

elif play3['Pontuacao'] > play1['Pontuacao'] and play3['Pontuacao'] > play2['Pontuacao'] and play3['Pontuacao'] > play4['Pontuacao']:
        print(f"\033[36;3;1mPLAYER 3\033[0;0m \033[32;1mVENCEU O JOGO\033[0;0m {play3['Pontuacao']} RODADAS VENCIDAS")

elif play4['Pontuacao'] > play1['Pontuacao'] and play4['Pontuacao'] > play3['Pontuacao'] and play4['Pontuacao'] > play3['Pontuacao']:
        print(f"\033[30;3;1mPLAYER 1\033[0;0m \033[32;1mVENCEU O JOGO\033[0;0m {play4['Pontuacao']} RODADAS VENCIDAS")
else:
    print("\033[31mHOUVE UM EMPATE, DADO A ISSO NÃO TEMOS UM VENCEDOR NESTA PARTIDA!")
