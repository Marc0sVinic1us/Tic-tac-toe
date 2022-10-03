## Este arquivo que deve ser rodado para a execução completa do programa.

from ModoBattle import *
from ModoLocal import *

print("\nBem vindo ao Jogo da Velha!")

modo = 'S'

## Menu principal que dá acesso aos modos de jogo individualmente.
while modo == 'S':

      ans = int(input('\nInsira o modo de jogo:\n' +
                  '<1> - Modo battle (Jogador vs Máquina)\n' +
                  '<2> - Modo local (Jogador 1 vs Jogador 2)\n'))

      if ans == 1:
            
            print('\n')
            ModoBattle()

      elif ans == 2:

            print('\n')
            ModoLocal()

      ## Dá a opção do jogador alternar entre os modos depois de cada rodada quando quiser.
      modo = input('\nDeseja mudar o modo de jogo? (S/N)\n').upper()

print('\nObrigado por jogar!\n')