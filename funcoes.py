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


def printa_quadro(nome, tamanho_quadro):
    tamanho_nome = len(nome)
    espaco_branco = (tamanho_quadro - tamanho_nome)
    metade = espaco_branco // 2
    # print(tamanho_nome, espaco_branco, metade)
    print('+' + '-' * tamanho_quadro + '+')
    print('|' + ' ' * metade + nome.upper() + ' ' * (espaco_branco - metade) + '|')
    print('+' + '-' * tamanho_quadro + '+')


# título
def titulo():
    printa_quadro('AMIGO SECRETO', 38)
    print('*--- Desenvolvido por Wadd Franklin ---*')
    print()