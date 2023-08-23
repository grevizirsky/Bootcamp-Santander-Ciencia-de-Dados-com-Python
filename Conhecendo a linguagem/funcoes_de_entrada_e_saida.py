#A funcao PRINT recebe um argumento obrigatorio do tipo varargs de objetos e 4 argumentos opcionais (sep, end, file e flush), Todos os objetos sao convertidos para string, separados por sep e terminados por end
nome = input("Informe seu nome: ")
idade = input("Informe sua idade: ")

print(nome, idade)
print(nome, idade, end="... \n")
print(nome, idade, sep="#")