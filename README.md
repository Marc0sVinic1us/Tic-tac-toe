  # Tic tac toe

  ## Descrição detalhada do projeto:

 Trata-se de um jogo da velha em linguagem de programação Python que funciona no próprio console do código. Tem como base uma matriz 3x3 como tabuleiro do jogo, que se inicia com todos os campos preenchidos com 0, e que com o decorrer o jogo vão sendo substituidos com 1 e 2. O número 1 representa o espaço escolhido pelo jogador, e o número 2 representa o espaço escolhido pela máquina. 
 
 Há também algumas limitações no código, por exemplo, o programa impossibilita que o jogador insira uma posição fora do tabuleiro para não ocorrer erro de posição fora de limites da matriz. Bem também como, não possibilita que o jogador ou a máquina escolha uma posição que já foi preenchida anteriomente por ambos, desta forma não há chances de forçar uma vitória. 

 Outra funcionalidade é que o programa dá a opção do usuário jogar quantas vezes quiser sem ter que reinicia-lo. 
 Além também de mostrar o placar do jogo, ou seja, quantas rodadas cada jogador já venceu.
 Ao fim, imprime o resultado final, ou seja, informa qual jogador venceu mais rodadas em seu determinado modo de jogo.

 O código está todo comentado para facilitar a compreensão das lógicas que utilizei.

 
 
### O jogo possui 3 possibilidades de fim:

 Caso um: Para isso deverá haver uma linha, coluna, ou diagonal totalmente preenchida com o número 1. 

 Caso dois: Análoga à anterior, porém com os espaços preenchidas pelo número 2. 

 Empate: Ocorre se nenhuma das condições anteriores forem atendidas e se todas as posições da matriz estiverem preenchidas com 1 ou 2.



### O jogo possui 2 modos: 

Modo battle: trata-se de um modo que jogam o usuário e o própria máquina. Neste modo, o usuário pode escolher qualquer posição do tabuleiro que desejar. Já as posições do programa são escolhidas aleatóriamente para tentar impedir que o usuário vença.

Modo local: trata-se de um modo onde dois usuários podem jogar localmente no mesmo computador, escolhendo livremente as posições que jogam. Possui os mesmos métodos de verificação de vitória do modo de jogo anterior.

O programa dá a opção do usuário alternar entre os modos de jogo durante a execução do programa, ao fim de cada rodada. Desta forma pode ser jogado de todas as formas possíveis com uma só execução, ou seja, não é necessário reiniciar o programa para jogar outro modo, 



### Planejamentos futuros para o projeto:

Por enquanto, o modo battle está com um módulo random para a escolha da posição da máquina em sua jogada. Este é um módulo aleatório e torna simples que o jogador vença, porém pretendo estudar e implementar uma IA (inteligência artificial) para tomar esta decisão, dificultando a  vitória para o jogador independente de qual estratégia que utilizar, e com a intenção de complementar cada vez mais o projeto.
 