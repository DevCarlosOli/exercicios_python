""" Exercício 01
nome = input("Digite seu nome: ")
altura = input("Digite sua altura: ")
peso = input("Digite seu peso: ")

altura_float = float(altura)
peso_int = int(peso)

imc = peso_int / altura_float ** 2

print(f'{nome}, seu imc é de: {imc:.2f}')
"""

""" Exercício 02
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

if nome and idade:
    print(f"Seu nome é {nome}")
    print(f"Seu nome invertido é {nome[::-1]}")

    if ' ' in nome:
        print(f'Seu nome contém espaços em branco')
    else:
        print(f'Seu nome não tem espaços em branco')

    print(f"Seu nome contém {len(nome)} letras")
    print(f"A primeira letra do seu nome é {nome[0]}")
    print(f"A última letra do seu nome é {nome[-1]}")
else:
    print("Desculpe, você deixou campos vazios!")
"""

""" Exercício 03
try:
    numero1 = input('Digite um número inteiro: ')

    numero1_int = int(numero1)

    if numero1_int:
        if numero1_int % 2 == 0:
            print('Este número é par.')
        else:
            print('Este número é ímpar.')
except:
    print("O valor digitado não é um número inteiro!")
"""

""" Exercício 04
hora = input('Digite apenas a hora atual: ')

hora_int = int(hora)

if hora_int == 0 or hora_int <= 11:
    print('Bom dia')
elif hora_int ==12 or hora_int <= 17:
    print('Boa tarde')
elif hora_int == 18 or hora_int <= 23:
    print('Boa noite')
else:
    print('A hora digitada não existe!')
"""

"""Exercício 05
nome = input('Digite seu primeiro nome: ')

if len(nome) <= 4:
    print('Seu nome é curto')
elif len(nome) == 5 or len(nome) <= 6:
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande') 
"""