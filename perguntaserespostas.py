"""
Programa de perguntas e respostas
"""

#Aplicação de Dicionários

perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2+2? ',
        'respostas': {
            'a': '1',
            'b': '4',
            'c': '5',
        },
        'resposta_certa': 'b',
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 3*2? ',
        'respostas': {
            'a': '4',
            'b': '10',
            'c': '6',
        },
        'resposta_certa': 'c',
    },
    'Pergunta 3': {
        'pergunta': 'Quanto é 5*5? ',
        'respostas': {
            'a': '25',
            'b': '50',
            'c': '100',
        },
        'resposta_certa': 'a',
    },
    'Pergunta 4': {
        'pergunta': 'Quanto é 100-80? ',
        'respostas': {
            'a': '40',
            'b': '20',
            'c': '2',
        },
        'resposta_certa': 'b',
    },
    'Pergunta 5': {
        'pergunta': 'Quanto é 8/2? ',
        'respostas': {
            'a': '4',
            'b': '10',
            'c': '6',
        },
        'resposta_certa': 'a',
    },
}

#Fim da aplicação

#Laço de repetição for
print()

respostas_certas = 0

for pk, pv in perguntas.items(): # O .items() permite acessar tanto a chave da pergunta quanto o valor.
    print(f'{pk}: {pv["pergunta"]}')

    print()

    print('Escolhas entre as opções abaixo')
    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')

    resposta_usuario = input('\nSua resposta: ')

    if resposta_usuario == pv['resposta_certa']:
        print('EHHHHHH!!! Você acertou')
        respostas_certas += 1
    else:
        print('VISHHHHH!!! Você errou!')

    print()

qtd_perguntas = len(perguntas)
porc_acerto = respostas_certas / qtd_perguntas * 100

print(f'Você acertou {respostas_certas} resposta(as)')
print(f'Sua porcentagem de acerto foi de {porc_acerto}')
