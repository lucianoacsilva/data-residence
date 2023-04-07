# %% [markdown]
# # Aula 3

# # Nome: Luciano Augusto Campagnoli da Silva

# %% [markdown]
# ## Exercício 8

# %%
def desconto(ano_imovel: int, ano_atual: int) -> int:
    idade: int = ano_atual - ano_imovel

    if idade < 5: return 0
    elif idade >= 5 & idade < 20: return 15
    elif idade >= 20 & idade < 40: return 25
    else: return 30

ano_imovel: int = 0
ano_atual: int = 0

print("Ano imóvel: ")
ano_imovel = int(input())

print("Ano atual: ")
ano_atual = int(input())

print("Idade imóvel: {}; Desconto: {} %".format(str(ano_atual - ano_imovel), str(desconto(ano_imovel, ano_atual))))



# %% [markdown]
# ## Exercício 9

# %%
def imc(peso: float, altura: float) -> str:
    imc: float = peso / (altura ** 2)

    if imc < 18.5: return "Baixo peso"
    elif (imc >= 18.5) & (imc < 25): return "Normal"
    elif (imc >= 25) & (imc < 30): return "Sobrepeso"
    else: return "Obesidade"

peso: float = 0
altura: float = 0

print("Peso: ")
peso = float(input())

print("Altura: ")
altura = float(input())

print("Classificação segundo IMC: {}".format(imc(peso, altura)))

# %% [markdown]
# ## Exercício 10

# %%
def ordem_crescente(numeros: list[float]) -> str:
    numeros_compare: list[float] = numeros.copy()
    numeros_compare.sort()

    if numeros == numeros_compare: return "Sim"

    return "Não"

print("Números: ")
numeros: list[float] = []

for i in range(3):
    print("Número {}".format(str(i + 1)))
    numeros.append(float(input()))

print("Estão em ordem crescente?: {}".format(ordem_crescente(numeros)))

# %% [markdown]
# ## Exercício 11

# %%
def aprovacao(frequencia: float, nota_1: float, nota_2: float) -> dict[str, any]: 
    media: float = (nota_1 + nota_2)/2

    if frequencia < 75: 
        return {
            "media": media,
            "status": "Reprovado"
        }
    
    if media < 4:
        return {
            "media": media,
            "status": "Reprovado"
        }
    
    elif (media >= 4) & (media < 6):
        return {
            "media": media,
            "status": "Exame"
        }
    
    else:
        return {
            "media": media,
            "status": "Aprovado"
        }

nota_1: float = 0
nota_2: float = 0
frequencia: float = 0
aprovado: dict[str, any] = {}

print("Nota 1: ")
nota_1 = float(input())

print("Nota 2: ")
nota_2 = float(input())

print("Frequência: ")
frequencia = float(input())

aprovado = aprovacao(frequencia, nota_1, nota_2)

print("Frequência: {}; Média: {}; Status: {}".format(str(frequencia), str(aprovado["media"]), aprovado["status"]))

# %% [markdown]
# ## Exercício 12

# %%
def divisao_polinomios(x: float) -> float | str:
    if x == 0: return "erro: não se pode dividir por 0"
    return (4 * x * x - 3 * x + 9)/x

x: float = 0
print("Valor de x: ")

x = float(input())

print("Resultado: {}".format(str(divisao_polinomios(x))))



