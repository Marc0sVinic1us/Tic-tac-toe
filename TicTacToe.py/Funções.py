import random


# Função que gera a matriz inicial do jogo, com todas as posições preenchidas com 0.
def GerarMatriz():

    linha = [0] * 3
    matriz = [linha] * 3

    print("   0  1  2")

    for i in range(0, 3, 1):
        linha = []

        for j in range(0, 3, 1):
            linha.append(0)

        matriz[i] = linha
        print(i, matriz[i])

    return matriz


# Função que determina a quantidade de vitórias dos jogadores ao fim de cada rodada.
def Placar(pontuacoes):

    print('\nPlacar:\n' +
          'Jogador um: ', pontuacoes[0])
    print('Jogador dois: ', pontuacoes[1])
    print('Empates: ', pontuacoes[2], '\n')


# Função que armaneza as coordenadas da posição a ser preenchida, inseridas pelo jogador.
def Pergunta():
    l = int(input("Digite a coordenada da linha: "))
    c = int(input("Digite a coordenada da coluna: "))

    return l, c


# Função que sorteia uma coordenada aleatória para jogada da máquina, porém, que impossibilita que a coordenada
# sorteada já tenha sido jogada anteriormente.
def JogadaMaquina(m, l, c):
    limitador = 0

    m_linha = round(random.random() * 2)
    m_coluna = round(random.random() * 2)

    while (m_linha == l and m_coluna == c) or (m[m_linha][m_coluna] == 1 or m[m_linha][m_coluna] == 2):

        m_linha = round(random.random() * 2)
        m_coluna = round(random.random() * 2)

        limitador += 1
        if limitador > 19:
            break

    if limitador != 20:
        m[m_linha][m_coluna] = 2

    return m


# Função que verifica se a posição escolhida pelo jogador já está preenchida.
def VerificarPosicao(m, l, c):

    while m[l][c] == 2 or m[l][c] == 1:
        if m[l][c] == 2 or m[l][c] == 1:
            print('\n')
            print('Escolha outras coordenadas!')
            (l, c) = Pergunta()

    return l, c


def VerificaResultado(m, resultado, diagonal1_j, diagonal2_j, diagonal1_m, diagonal2_m):

    resultado[0] = VerificarHorizontal(m)
    resultado[1] = VerificarVertical(m)
    resultado[2] = VerificaDiagonal(m, diagonal1_j, diagonal2_j, diagonal1_m, diagonal2_m)
    resultado[3] = VerificaEmpate(m)

    return resultado


# Função que verifica se há algum caso de vitória de algum jogador nas horizontais da matriz.
def VerificarHorizontal(m):
    horizontal_j = 0
    horizontal_m = 0

    for i in range(0, 3, 1):
        for j in range(0, 3, 1):

            if m[i][j] == 1:
                horizontal_j += 1

            elif m[i][j] == 2:
                horizontal_m += 1

        if horizontal_j > 2:
            resultado = "um"
            return resultado

        elif horizontal_m > 2:
            resultado = "dois"
            return resultado

        horizontal_j = 0
        horizontal_m = 0


# Função que verifica se há algum caso de vitória de algum jogador nas verticais da matriz.
def VerificarVertical(m):
    vertical_j = 0
    vertical_m = 0

    for i in range(0, 3, 1):
        for j in range(0, 3, 1):

            if m[j][i] == 1:
                vertical_j += 1

            elif m[j][i] == 2:
                vertical_m += 1

        if vertical_j > 2:
            resultado = "um"
            return resultado

        elif vertical_m > 2:
            resultado = "dois"
            return resultado

        vertical_j = 0
        vertical_m = 0


# Função que verifica se há algum caso de vitória de algum jogador nas diagonais da matriz.
def VerificaDiagonal(m, diagonal1_j, diagonal2_j, diagonal1_m, diagonal2_m):
    for i in range(0, 3, 1):
        for j in range(0, 3, 1):

            if m[i][j] == 1:

                if i == j:
                    diagonal1_j += 1

                if (i == 0 and j == 2) or (i == 2 and j == 0) or (i == 1 and j == 1):
                    diagonal2_j += 1

            elif m[i][j] == 2:

                if i == j:
                    diagonal1_m += 1

                if (i == 0 and j == 2) or (i == 2 and j == 0) or (i == 1 and j == 1):
                    diagonal2_m += 1

    if diagonal1_j > 2 or diagonal2_j > 2:
        resultado = "um"
        return resultado

    elif diagonal1_m > 2 or diagonal2_m > 2:
        resultado = "dois"
        return resultado


# Função que verifica se houve empate, ou seja, se todas as posições da matriz estão preenchidas e sem casos de vitória.
def VerificaEmpate(m):
    cont = 0

    for i in range(0, 3, 1):
        for j in range(0, 3, 1):

            if m[i][j] == 0:
                cont += 1

    if cont == 0:
        resultado = 'empate'
        return resultado


def ImprimirMatriz(m):

    for i in range(0, 3, 1):
        print(m[i])

