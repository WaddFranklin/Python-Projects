import random
import time
from funcoes import *

amigos = []
aux = []
duplas = []

titulo()

# adiciona os participantes na lista 'amigos'
num_amigos = int(input('Quantas pessoas participarão? > '))
for i in range(num_amigos):
    nome = input('Digite o nome do participante {}: > '.format(i + 1)).lower()
    amigos.append(nome)

aux = amigos[:] # copia a lista 'amigos' em 'aux'

print('\nEmbaralhando os participantes...\n')
random.shuffle(amigos) # embaralha os participantes
random.shuffle(aux) # embaralha a lista 'aux'

print('Sorteando...\n')

# para cada participante de 'amigos', sorteia um candidato de 'aux'
i = 0
while i < len(amigos):
    if len(aux) == 1 and amigos[i] == aux[0]:
        # print('entrou')
        aux = amigos[:]
        duplas = []
        i = 0
        continue

    while True:
        sorteado = random.choice(aux)
        # print('sorteado = {}'.format(sorteado))
        if amigos[i] == sorteado:
            # print('sorteou o mesmo')
            continue
        else:
            # print('ok')
            duplas.append([amigos[i], sorteado])
            aux.remove(sorteado)
            break
    i += 1

print('Sorteio realizado com sucesso!\n')

opcao = ''
while True:
    opcao = input("Digite 'cons' para consultar o seu amigo ou 'sair' para finalizar o programa: > ").lower()
    if opcao == 'cons':
        while True:
            limpa_tela()
            nome = input('Digite o seu nome ou \'sair\' para finalizar a consulta: > ').lower()
            if nome in amigos:
                dupla = busca_amigos(duplas, nome)
                print('\n\nO nome do seu amigo secreto será exibido em 5 segundos...\n\n')
                time.sleep(5)
                printa_quadro(dupla[1].upper(), 40)
                # print('\n----- {} -----\n\n'.format(dupla[1].upper()))
                print('Aguarde o nome do seu amigo desaparecer...\n\n')
                # print('{:-<15}> {}'.format(dupla[0].upper() + ' ', dupla[1].upper()))
                time.sleep(7)
                limpa_tela()
            elif nome == 'sair':
                limpa_tela()
                break
            else:
                print('Esse nome não consta na lista de participantes!')
                time.sleep(2)
                limpa_tela()
    elif opcao == 'debug':
        limpa_tela()
        print_duplas(duplas)
    elif opcao == 'sair':
        break
    else:
        limpa_tela()
        print('Entrada inválida!')
        time.sleep(2)
