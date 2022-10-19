from Funções import *


# Modo Jogador vs Máquina.
# Lógica da jogada da máquina feita com módulo random.
def ModoBattle():
    print("\nModo battle:\n" +
          "Jogador: 1\n" +
          "Máquina: 2\n")

    ans = 'S'
    pontuacoes = [0, 0, 0]


    # Laço de repetição que permite que se jogue quantas vezes desejar.
    while ans == "S":

        Placar(pontuacoes)

        m = GerarMatriz()
        resultado = ['', '', '', '']

        diagonal1_j = 0
        diagonal2_j = 0
        diagonal1_m = 0
        diagonal2_m = 0

        print('\n')

        # Bloco de código para verificação se as coordenadas escolhidas estão fora dos limites da matriz (menor que 0
        # ou maior que 2). Ou se estão livres, ou seja, se já não foram escolhidas anteriormente pelo jogador ou pela
        # máquina.
        while True:

            (l, c) = Pergunta()

            while (l < 0 or l > 2) or (c < 0 or c > 2):

                if (l < 0 or l > 2) or (c < 0 or c > 2):
                    print('Favor digitar coordenadas entre 0 e 2\n')

                (l, c) = Pergunta()

            if m[l][c] == 2 or m[l][c] == 1:
                (l, c) = VerificarPosicao(m, l, c)

            m[l][c] = 1

            # Bloco de código para verificação se o jogador ganhou o jogo na rodada atual.
            resultado = VerificaResultado(m, resultado, diagonal1_j, diagonal2_j, diagonal1_m, diagonal2_m)
            print("\n")

            if (resultado[0] or resultado[1] or resultado[2] or resultado[3]) is not None:
                ImprimirMatriz(m)
                break

            m = JogadaMaquina(m, l, c)
            ImprimirMatriz(m)

            # Bloco de código para verificação se a máquina ganhou o jogo na rodada atual.
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

