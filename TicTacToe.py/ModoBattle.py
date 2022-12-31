from Funções import *


# Modo Jogador vs Máquina.
# Lógica da jogada da máquina feita com módulo random.
def ModoBattle():
    print("\nModo battle:\n" +
          "Jogador: 1\n" +
          "Máquina: 2\n")

    points = {
        "vitoria": 0,
        "derrota": 0,
        "empate": 0
    }

    ans = 'S'

    # Laço de repetição que permite que se jogue quantas vezes desejar.
    while ans == "S":

        Placar(points)

        m = GerarMatriz()
        resultado = {
            "horizontal": "",
            "vertical": "",
            "diagonal": "",
            "velha": "",
        }

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
            resultado = VerificaResultado(m, resultado)
            print("\n")

            if Break(resultado) == "fim":
                ImprimirMatriz(m)
                break

            m = JogadaMaquina(m, l, c)
            ImprimirMatriz(m)

            # Bloco de código para verificação se a máquina ganhou o jogo na rodada atual.
            resultado = VerificaResultado(m, resultado)
            print("\n")

            if Break(resultado) == "fim":
                break

        print('\nFIM DE JOGO!\n')

        if (list(resultado.values())).__contains__("um"):
            print('Parabéns, você venceu a rodada!')
            points["vitoria"] += 1

        elif (list(resultado.values())).__contains__("dois"):
            print('Infelizmente você perdeu a rodada!')
            points["derrota"] += 1

        else:
            print('Deu velha!')
            points["empate"] += 1

        ans = input('\nDeseja jogar novamente? (S/N)\n').upper()

    # Bloco de código que exibe o resultado final de quem venceu mais rodadas.
    print('\nRESULTADO FINAL:')

    if points["vitoria"] > points["derrota"]:
        print('Parabéns, você venceu!\n')

    elif points["derrota"] > points["vitoria"]:
        print('Infelizmente, você perdeu!\n')

    else:
        print('Houve um empate!')
