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
        limpa_tela()
        nome = input('Digite o seu nome: > ').lower()
        if nome in amigos:
            dupla = busca_amigos(duplas, nome)
            print('{:-<15}> {}'.format(dupla[0] + ' ', dupla[1]))
            time.sleep(2)
            limpa_tela()
        else:
            print('Esse nome não consta na lista de participantes!')
            limpa_tela()
    elif opcao == 'debug':
        limpa_tela()
        print_duplas(duplas)
    elif opcao == 'sair':
        break
    else:
        limpa_tela()
        print('Entrada inválida!')

print('\n*--- Desenvolvido por Wadd Franklin ---*')
