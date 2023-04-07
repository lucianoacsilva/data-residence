# %% [markdown]
# # Aula 5

# %% [markdown]
# ## Exercício 1

# %%
def media(valores: list[int]) -> float:
    soma: int = 0

    for n in valores:
        soma += n
    
    return soma/len(valores)

def maximo(valores: list[int]) -> int:
    maximo: int = valores[0]

    for n in range(1, len(valores) - 1):
        if valores[n] > maximo: maximo = valores[n]

    return maximo

def minimo(valores: list[int]) -> int:
    minimo: int = valores[0]

    for n in range(1, len(valores) - 1):
        if valores[n] < minimo: minimo = valores[n]

    return minimo

quantidade_numeros: int = 0
numeros: list[int] = []

print("Quantidade de números: ")
quantidade_numeros = int(input())

print("Digite os números: ")

for i in range(quantidade_numeros):
    numeros.append(int(input()))

print("Média: {}; Máximo: {}; Mínimo: {}".format(
    str(media(numeros)),
    str(maximo(numeros)),
    str(minimo(numeros))
))


# %% [markdown]
# ## Exercício 2:

# %%
def imprime_reverso(valores: list[int]) -> None:
    for n in range(len(valores) -1, -1, -1):
        print(valores[n])

quantidade_numeros: int = 0
valores: list[int] = []

print("Quantidade de números: ")
quantidade_numeros = int(input())

print("Digite os números: ")

for i in range(quantidade_numeros):
    valores.append(int(input()))

imprime_reverso(valores)

# %% [markdown]
# ## Exercício 3

# %%
def media(valores: list[float]) -> float:
    soma: int = 0

    for n in valores:
        soma += n
    
    return soma/len(valores)

numero_alunos: int = 0
notas: list[list[float]] = []
medias: list[float] = []

print("Número de alunos: ")
numero_alunos = int(input())

print("Notas dos alunos: ")

for i in range(numero_alunos):
    notas_aluno: list[float] = []
    print("Aluno {}: ".format(str(i)))

    for j in range(4):
        print("Prova {}: ".format(str(j)))
        notas_aluno.append(float(input()))

    notas.append(notas_aluno)
    medias.append(media(notas_aluno))

print("Notas dos alunos: {}".format(str(notas)))
print("Média dos alunos: {}".format(str(medias)))






# %% [markdown]
# ## Exercício 4

# %%
def ordenar(valores: list[int]) -> None:
    valores.sort()

quantidade_numeros: int = 0
valores: list[int] = []

print("Quantidade de números: ")
quantidade_numeros = int(input())

print("Digite os números: ")

for i in range(quantidade_numeros):
    valores.append(int(input()))

ordenar(valores)
print(str(valores))

# %% [markdown]
# ## Exercício 8

# %%
def is_cadastrado(nomes: list[str], nome_consulta: str) -> str:
    return "CADASTRADO" if nome_consulta in nomes else "NÃO CADASTRADO"

nomes: list[str] = []
numero: int = 0
nome_consulta: str = ""

print("Número: ")
numero = int(input())

print("Digite os nomes; ")

for i in range(numero):
    nomes.append(input())

print("Nome a consultar: ")
nome_consulta = input()

print("Nomes: {}".format(str(nomes)))
print("Status de {}: {}".format(nome_consulta, is_cadastrado(nomes, nome_consulta)))



# %% [markdown]
# ## Exercício 9

# %%
def meia_piramide(numero: int) -> None:
    for i in range(numero + 1):
        print("*" * i)

numero: int = 0

print("Número:")
numero = int(input())

print("Meia pirâmide: ")
meia_piramide(numero)

# %% [markdown]
# ## Exercício 10

# %%
def meia_piramide(numero: int) -> None:
    for i in range(1, numero + 1):
        borda: int = numero - i
        print(" " * borda + "*" * (2 * i - 1) + " " * borda)

numero: int = 0

print("Número:")
numero = int(input())

print("Pirâmide completa: ")
meia_piramide(numero)


