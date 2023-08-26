MAIORIDADE = 18
IDADE_ESPECIAL = 12 

idade = int(input("Digite sua idade: "))

# if idade >= MAIORIDADE:
#     print("Maior de idade, pode tirar a CNH")

# if idade <= MAIORIDADE:
#     print("Menor de idade, nao pode tirar CNH")

# if idade >= MAIORIDADE:
#     print("Maior de idade, pode tirar a CNH")
# else:
#     print("Menor de idade, nao pode tirar CNH")

if idade >= MAIORIDADE:
    print("Maior de idade, pode tirar a CNH")
elif idade == IDADE_ESPECIAL:
    print("Pode fazer aula teorica, porem nao pode fazer aula pratica")
else:
    print("Menor de idade, nao pode tirar CNH")