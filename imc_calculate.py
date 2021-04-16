"""
Fazer o cálculo do IMC, onde:
- Deverá ser feito um pergunta ao usuário;
- Mostrar resposta na tela;
"""

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
anoAtual = 2020
nascimento = anoAtual - idade
imc = peso / (altura * altura)

if imc < 17:
    print(f"{nome} tem {idade} anos, nasceu no ano {nascimento}, pesa {peso:.2f}kg, \n"
          f"mede {altura:.2f}m de altura e seu IMC é {imc:.2f}, ou seja, está muito baixa, \n"
          f"precisa se alimentar muito melhor")
elif imc == 17 or imc < 18.5:
    print(f"{nome} tem {idade} anos, nasceu no ano {nascimento}, pesa {peso:.2f}kg, \n"
          f"mede {altura:.2f}m de altura e seu IMC é {imc:.2f}, ou seja, está baixa, \n"
          f"precisa se alimentar melhor")
elif imc == 18.5 or imc < 25:
    print(f"{nome} tem {idade} anos, nasceu no ano {nascimento}, pesa {peso:.2f}kg, "
          f"mede {altura:.2f}m de altura e seu IMC é {imc:.2f}, ou seja, está normal, "
          f"parabéns! Está em ótima forma!")
elif imc == 25 or imc < 30:
    print(f"{nome} tem {idade} anos, nasceu no ano {nascimento}, pesa {peso:.2f}kg, \n"
          f"mede {altura:.2f}m de altura e seu IMC é {imc:.2f}, ou seja, está acima do peso, \n"
          f"cuidado! Esta é a hora de freiar um pouco com a comida!")
elif imc == 30 or imc < 35:
    print(f"{nome} tem {idade} anos, nasceu no ano {nascimento}, pesa {peso:.2f}kg, \n"
          f"mede {altura:.2f}m de altura e seu IMC é {imc:.2f}, ou seja, está com obesidade de grau I, \n"
          f"não exagere com a alimentação!")
elif imc == 35 or imc < 40:
    print(f"{nome} tem {idade} anos, nasceu no ano {nascimento}, pesa {peso:.2f}kg, \n"
          f"mede {altura:.2f}m de altura e seu IMC é {imc:.2f}, ou seja, está obesidade de grau II, \n"
          f"chega de exageros e vamos perder alguns quilinhos!")
else:
    print(f"{nome} tem {idade} anos, nasceu no ano {nascimento}, pesa {peso:.2f}kg, \n"
          f"mede {altura:.2f}m de altura e seu IMC é {imc:.2f}, ou seja, está obesidade de grau III, \n"
          f"você vai entrar em um regime forçado! Isso é para seu próprio bem!")
