import random

# primeiro digito cpf
nove_digitos = ''

for i in range(9):
    nove_digitos += str(random.randint(0, 9))

contador_regressivo_1 = 10
primeiro_digito = 0

for digito in nove_digitos:
    primeiro_digito += int(digito) * contador_regressivo_1
    contador_regressivo_1 += 1

digito1 = (primeiro_digito * 10) % 11
digito1 = digito1 if digito1 <= 9 else 0

# segundo digito cpf
dez_digitos = nove_digitos + str(digito1)
contador_regressivo_2 = 11
segundo_digito = 0

for digito in dez_digitos:
    segundo_digito += int(digito) * contador_regressivo_2
    contador_regressivo_2 -= 1

digito2 = (segundo_digito * 10) % 11
digito2 = digito2 if digito2 <= 9 else 0

calculo_cpf = f'{nove_digitos}{digito1}{digito2}'

print(calculo_cpf)