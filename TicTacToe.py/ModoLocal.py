from Funções import *


# Modo Jogador 1 vs Jogador 2.
def ModoLocal():
    print("\nModo local:\n" +
          "Jogador um: 1\n" +
          "Jogador dois: 2\n")

    ans = 'S'
    pontuacoes = [0, 0, 0]


    # Laço de repetição que permite que se jogue quantas vezes desejar.
    while ans == 'S':

        Placar(pontuacoes)

        m = GerarMatriz()
        resultado = ['', '', '', '']

        diagonal1_j = 0
        diagonal2_j = 0
        diagonal1_m = 0
        diagonal2_m = 0

        print('\n')

        # Bloco de código para verificação se as coordenadas escolhidas estão fora dos limites da matriz (menor que 0
        # ou maior que 2). Ou se estão livres, ou seja, se já não foram escolhidas anteriormente por um dos jogadores.
        while True:

            # Bloco de código para a escolha da posição do jogador 1.
            print('Jogador 1:')
            (l1, c1) = Pergunta()

            while (l1 < 0 or l1 > 2) or (c1 < 0 or c1 > 2):

                if (l1 < 0 or l1 > 2) or (c1 < 0 or c1 > 2):
                    print('Favor digitar coordenadas entre 0 e 2\n')

                (l1, c1) = Pergunta()

            if m[l1][c1] == 2 or m[l1][c1] == 1:
                (l1, c1) = VerificarPosicao(m, l1, c1)

            m[l1][c1] = 1

            print('\n')
            ImprimirMatriz(m)

            # Bloco de código para verificação se o jogador 1 ganhou o jogo na rodada atual.
            resultado = VerificaResultado(m, resultado, diagonal1_j, diagonal2_j, diagonal1_m, diagonal2_m)
            print("\n")

            if (resultado[0] or resultado[1] or resultado[2] or resultado[3]) is not None:
                break

            # Bloco de código para a escolha da posição do jogador 2.
            print('Jogador 2:')
            (l2, c2) = Pergunta()

            while (l2 < 0 or l2 > 2) or (c2 < 0 or c2 > 2):

                if (l2 < 0 or l2 > 2) or (c2 < 0 or c2 > 2):
                    print('Favor digitar coordenadas entre 0 e 2\n')

                (l2, c2) = Pergunta()

            if m[l2][c2] == 2 or m[l2][c2] == 1:
                (l2, c2) = VerificarPosicao(m, l2, c2)

            m[l2][c2] = 2

            print('\n')
            ImprimirMatriz(m)

            # Bloco de código para verificação se o jogador 2 ganhou o jogo na rodada atual.
            resultado = VerificaResultado(m, resultado, diagonal1_j, diagonal2_j, diagonal1_m, diagonal2_m)
            print("\n")

            if (resultado[0] or resultado[1] or resultado[2] or resultado[3]) is not None:
                break

        print('\nFIM DE JOGO!\n')

        if resultado.__contains__('um'):
            print('Parabéns, você venceu a rodada!')
            pontuacoes[0] += 1

        elif resultado.__contains__('dois'):
            print('Infelizmente você perdeu a rodada!')
            pontuacoes[1] += 1
            
        else:
            print('Deu velha!')
            pontuacoes[2] += 1

        
        ans = input('\nDeseja jogar novamente? (S/N)\n').upper()


    # Bloco de código que exibe o resultado final de quem venceu mais rodadas.
    print('\nRESULTADO FINAL:')

    if pontuacoes[0] > pontuacoes[1]:
        print('O jogador um venceu o jogo!\n')

    elif pontuacoes[1] > pontuacoes[0]:
        print('O jogador dois venceu o jogo!\n')
    
    else:
        print('Houve um empate!')