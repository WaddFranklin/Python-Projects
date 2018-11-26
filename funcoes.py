# mostra a lista de participantes e seus sorteados
def print_duplas(duplas):
    print('+' + '-' * 33 + '+')
    for dupla in duplas:
        print('{:-<15}> {}'.format(dupla[0] + ' ', dupla[1]))
    print('+' + '-' * 33 + '+')


# limpa a tela do console
def limpa_tela(): print('\n' * 100)


# busca um participante e seu amigo secreto com base em um nome fornecido pelo usuario
def busca_amigos(duplas, nome):
    for dupla in duplas:
        if dupla[0] == nome:
            return dupla

# título
def titulo():
    print('+-----------------------+')
    print('|---- AMIGO SECRETO ----|')
    print('+-----------------------+')
    print()
