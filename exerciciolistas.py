#Exercício python sobre listas, dicionários e tuplas

"""
-> É uma lista de listas de números inteiros;
-> As listas internas tem o tamanho de 10 elementos;
-> As listas internas contém números de 01 à 10 e eles podem ser duplicados.

Exercício:

-> Crie uma função que encontra o primeiro número duplicado considerando o segundo número como duplicação.
Retorne o número duplicado.
    Requisitos:
        A ordem do número duplicado é considerada a partir da segunda ocorrência do número, ou seja, o número
        duplicado em si.
        Exemplo: [1, 2, 3, ->3<-, 2, 1] -- os números nesta lista são duplicados, portanto o primeiro número duplicado
        é 3 e este deve ser retornado.
        [1, 2, 3, 4, 5] -- não temos números duplicados nesta lista, portanto deve ser retornado -1.
"""
listaint = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [1, 2, 1, 4, 1, 7, 7, 8, 9, 9],
    [2, 2, 3, 4, 4, 6, 4, 8, 9, 10],
    [1, 5, 3, 4, 5, 6, 2, 8, 9, 1],
    [3, 3, 3, 4, 5, 6, 6, 8, 4, 10],
    [1, 2, 7, 4, 5, 10, 7, 8, 9, 10],
    [7, 2, 9, 9, 5, 10, 7, 8, 9, 10],
]

def duplicado(stop_listint):
    duplicate = set()
    firstduplicate = -1

    for numero in stop_listint:
        if numero in duplicate:
            firstduplicate = numero
            break

        duplicate.add(numero)

    return firstduplicate

for listas_inteiros in listaint:
    print(listas_inteiros, duplicado(listas_inteiros))
