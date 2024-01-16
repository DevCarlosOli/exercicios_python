"""
Faça um jogo para o usuário adivinar qual a palavra secreta.
-> Deve ser proposto uma palavra secreta qualqer e vai dar a possibilidade para o usuário digitar apenas uma letra.
-> A letra que o usuário digitar será conferida com a letra que está na palavra secreta.
    ->-> Se a letra digitada estiver na palavra secreta; exiba a letra;
    ->-> Se a letra digitada não estiver na palavra secreta; exiba asterico ( * ).
Faça a contagem de tentativas do usuário.
"""

import os

print('######## Jogo Palavra Secreta ########\n')

palavra_secreta = input('Digite a palavra secreta: ')
os.system('cls')
letras_corretas = ''
tentativas = 0
sair_jogo = 'sair'

while True:    
    letra_digitada = input('Digite uma letra da palavra secreta: ')
    tentativas += 1

    if letra_digitada == sair_jogo or palavra_secreta == sair_jogo:
        break
    elif len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue

    if letra_digitada in palavra_secreta:
        letras_corretas += letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_corretas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print(palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system('cls')
        print('VOCÊ GANHOU!!! PARABÉNS!')
        print('A palavra era: ', palavra_secreta)
        print('Tentativas = ', tentativas)
        letras_corretas = ''
        tentativas = 0
        
        print('\nCaso queira sair do jogo digite a palavra = sair')
        palavra_secreta = input('Digite a palavra secreta: ')
        os.system('cls')
        if palavra_secreta == sair_jogo:
            break