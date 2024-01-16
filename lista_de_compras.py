"""
Faça uma lista de compras com listas
O usuário deve ter a possibilidade de inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com erros de índices inexistentes na lista
"""

import os

lista_compras = []

while True:
    valor_selecao = input('Digite uma das opções: [i]nserir, [a]pagar, [l]istar, [e]ncerrar: ')

    if valor_selecao == 'i':
        item = input('Valor: ') 
        lista_compras.append(item)
    elif valor_selecao == 'a':
        indice = input('Indice: ')

        try:
            valor_indice = int(indice)
            del lista_compras[valor_indice]
        except:
            print('Indice não existe na lista de compras')                
    elif valor_selecao == 'l':
        os.system('cls')

        if len(lista_compras) == 0:
            print('Nada para listar!')

        for indice, nome in enumerate(lista_compras):
            print(indice, nome)
    elif valor_selecao == 'e':
        os.system('cls')
        print('ATÉ A PRÓXIMA!')
        break
    else:
        print('Opção inexistente, tente novamente!')
        os.system('cls')