"""
Exercício sobre compreensão de listas
"""

#Variável
string = '0123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789'
n = 10
ex = [string[i: i + n] for i in range(0, len(string), n)]
retorno = '.'.join(ex) #.join permite que variáveis possam ser juntas com o que estiver sendo aplicado antes do .join.

print(retorno)
