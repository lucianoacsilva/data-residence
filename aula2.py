# %% [markdown]
# 

# %% [markdown]
# # Exercicios aula 2
# # Aluno: Luciano Augusto Campagnoli da Silva  

# %% [markdown]
# ## Exercicio 1

# %%
def imc (peso: float, altura: float) -> float:
    return peso/(altura * altura)

print("Peso(kg): ")
peso = float(input())

print("Altura(m): ")
altura = float(input())

print("IMC (kg/m2): ", str(imc(peso, altura)))

# %% [markdown]
# ## Exercício 2

# %%
def msParaKmh(velocidadeMetrosPorSegundo: float) -> float:
    return velocidadeMetrosPorSegundo * 3.6

print("Velocidade (m/s): ")
velocidadeMetrosPorSegundo = float(input())

print("Veloicade (km/h): ", str(msParaKmh(velocidadeMetrosPorSegundo)))

# %% [markdown]
# ## Exercicio 3

# %%
def velocidadeMedia(deslocamento: float, tempo: float) -> float:
    return deslocamento/tempo

def aceleracaoMedia(variacaoVelocidade: float, tempo: float) -> float:
    return variacaoVelocidade/tempo

trechosPista: list = []
aceleracoesEntreTrechos: list = []
distanciaTotal: float = 0
tempoTotal: float = 0
index: int = 1

for i in range(4):
    aceleracaoEntreTrechos: float = 0

    print("Distância trecho {} (m): ".format(i))
    distancia = float(input())

    print("Tempo trecho {} (m): ".format(i))
    tempo = float(input())

    velMedia = velocidadeMedia(distancia, tempo)

    distanciaTotal += distancia
    tempoTotal += tempo

    trechosPista.append({
        "distancia": distancia,
        "tempo": tempo,
        "velMedia": velMedia
    })

    if(i != 0): aceleracaoEntreTrechos = (velMedia - trechosPista[i - 1]["velMedia"])/trechosPista[i - 1]["tempo"]

    print("Dados do trecho: ")
    print("Distância (m): {}".format(str(distancia)))
    print("Tempo (s): {}".format(str(tempo)))
    print("Velocidade média (m/s): {}".format(str(velMedia)))

    if(i != 0): print("Aceleração entre trecho {} e {} (m/s²): {}".format(str(i), str(i - 1), str(aceleracaoEntreTrechos)))

    print()

print("Velocidade média de todo o percurso (m/s): {}".format(str(distanciaTotal/tempoTotal)))


# %% [markdown]
# ## Exercício 4

# %%
from math import sin, cos, pi
v0: float = 6 # velocidade inicial em m/s (constante)
teta: float = pi/3 # ângulo de inclinação em rad/s (constante)
g: float = 9.81 # aceleração do campo gravitacional da Terra a nível do mar em m/s² (constante)

def distancia(tempo: float) -> float:
    return v0 * cos(teta) * tempo

def altura(tempo: float) -> float:
    return v0 * sin(teta) * tempo - (g * tempo * tempo) / 2

tempo: float = 0

print("Instante da trajetória (s):")
tempo = float(input())

print("Distância horizontal no instante {} (m): {}".format(str(tempo), str(distancia(tempo))))
print("Altura no instante {} (m): {}".format(str(tempo), str(altura(tempo))))

# %% [markdown]
# ## Exercício 5

# %%
from math import sqrt, pow

def distanciaEuclidiana(xo: float, yo: float, xd: float, yd: float) -> float:
    return sqrt(pow(xd - xo, 2) + pow(yd - yo, 2))

xo: float = 0
yo: float = 0
xd: float = 0
yd: float = 0

print("Ponto de origem: ")
print("Coordenada x (m):")
xo = float(input())

print("Coordenada y (m):")
yo = float(input())

print("Ponto de destino: ")
print("Coordenada x (m):")
xd = float(input())

print("Coordenada y (m):")
yd = float(input())

print()
print("Distância entre origem e destino (m): {}".format(str(distanciaEuclidiana(xo, yo, xd, yd))))

# Exercícios extras aula 3

# %% [markdown]
# # Estruturas condicionais - Exercícios

# %% [markdown]
# ## Exercício 1

# %%
def avalia_triglicerides(tg: float) -> str:
    if tg < 150: return "NÍVEL DESEJADO"
    elif (tg >= 150) & (tg < 200): return "NÍVEL LÍMITROFE"
    return "NÍVEL ELEVADO"

def avalia_colesterol_total(ct: float) -> str:
    if ct < 200: return "NÍVEL DESEJADO"
    elif (ct >= 200) & (ct < 240): return "NÍVEL LÍMITROFE"
    return "NÍVEL ELEVADO" 

triglicerides: float = 0
colesterol_total: float = 0

print("Triglicérides: ")
triglicerides = float(input())

print("Colesterol total: ")
colesterol_total = float(input())

print("Avaliação triglicérides: {}; avaliação colesterol total: {}".format(
    str(avalia_triglicerides(triglicerides)),
    str(avalia_colesterol_total(colesterol_total))
))

# %% [markdown]
# ## Exercício 2

# %%
def adicao(num_a: float, num_b: float) -> float:
    return num_a + num_b

def subtracao(num_a: float, num_b: float) -> float:
    return num_a - num_b

def mulitplicacao(num_a: float, num_b: float) -> float:
    return num_a * num_b

def divisao(num_a: float, num_b: float) -> float | str:
    if num_b == 0: return "ERRO! NÃO SE PODE DIVIR POR 0!"

    return num_a/num_b

op_1: float = 0
operacao: str = ""
op_2: float = 0
resultado: float | str = 0

print("Primeiro operando: ")
op_1 = float(input())

print("Operacao: ")
operacao = str(input())

print("Segundo operando: ")
op_2 = float(input())

match operacao:
    case "+":
        resultado = adicao(op_1, op_2)

    case "-":
        resultado = subtracao(op_1, op_2)

    case "*":
        resultado = mulitplicacao(op_1, op_2)

    case "/":
        resultado = divisao(op_1, op_2)

print("Resultado: {}".format(str(resultado)))


# %% [markdown]
# ## Exercício 3

# %%
def compara_numeros(num_1: float, num_2: float) -> str:
    if num_1 == num_2: return "números iguais!"
    elif num_1 > num_2: return "primeiro número é maior!"
    return "segundo número é maior!"

num_1: float = 0
num_2: float = 0

print("Primeiro número: ")
num_1 = float(input())

print("Segundo número: ")
num_2 = float(input())

print("Comparação: {}".format(compara_numeros(num_1, num_2)))

# %% [markdown]
# ## Exercício 4

# %%
def compara_numeros_3(num_1: float, num_2: float, num_3: float) -> float:
    # Assume-se que o primeiro número é o maior e compara-se com os outros dois
    resultado: str = "primeiro número é o maior!"
    
    if num_2 > num_1: 
        num_1 = num_2
        resultado = "segundo número é o maior!"

    if num_3 > num_1: 
        num_1 = num_3
        resultado = "terceiro número é o maior!"

    return resultado

num_1: float = 0
num_2: float = 0
num_3: float = 0

print("Primeiro número: ")
num_1 = float(input())

print("Segundo número: ")
num_2 = float(input())

print("Terceiro número: ")
num_3 = float(input())

print("Maior número: {}".format(compara_numeros_3(num_1, num_2, num_3)))

# %% [markdown]
# # Exercícios extras

# %% [markdown]
# ## 1

# %%
def valida_senha(senha: str) -> str:
    senha_correta: str = "ABBA"
    return "ACESSO PERMITIDO" if senha == senha_correta else "ACESSO NEGADO"

print("Senha: ")
senha = input()

print(valida_senha(senha))

# %% [markdown]
# ## 2

# %%
def tipo_triangulo(lado_1: float, lado_2: float, lado_3: float) -> str:
    # Verifica se triângulo pode existir (a soma dos dois maiores lados tem que exceder o maior)
    lados: list = [lado_1, lado_2, lado_3]
    tipos: list = ["escaleno", "isósceles", "equilátero"]
    lados.sort()

    if lados[2] >= lados[0] + lados[1]: return "triângulo não pode existir!"
    
    tipo_indice: int = 0

    if lado_1 == lado_2: tipo_indice += 1
    if lado_1 == lado_3: tipo_indice += 1
    # Caso equilátero
    if tipo_indice == 2: return tipos[tipo_indice]
    
    if lado_2 == lado_3: tipo_indice += 1 

    return tipos[tipo_indice]

lado_1: float = 0
lado_2: float = 0
lado_3: float = 0

print("Lados do triângulo: ")
print("Primeiro lado: ")
lado_1 = float(input())

print("Segundo lado: ")
lado_2 = float(input())

print("Terceiro lado: ")
lado_3 = float(input())

print("Tipo de triângulo: {}".format(tipo_triangulo(lado_1, lado_2, lado_3)))

# %% [markdown]
# ## 3

# %%
def paridade(numero: int) -> str:
    return "PAR" if numero % 2 == 0 else "ÍMPAR"

numero: int = 0
print("Número: ")

numero = int(input())
print("Paridade: {}".format(str(paridade(numero))))

# %% [markdown]
# ## 4

# %%
def divisivel(num_1: int, num_2: int) -> int:
    if num_2 == 0: return "ERRO: NENHUM NÚMERO É DIVISÍVEL POR 0"

    return "DIVISÍVEL" if num_1 % num_2 == 0 else "INDIVISÍVEL"

num_1: int = 0
num_2: int = 0

print("Primeiro número: ")
num_1 = int(input())

print("Segundo número: ")
num_2 = int(input())

print(divisivel(num_1, num_2))

# %% [markdown]
# ## 5

# %%
def weighted_average(nota_1: float, nota_2: float) -> list[str]: 
    # Pesos internos da função (fixos), não são parâmetros de entrada
    peso_1: float = 3
    peso_2: float = 4

    media: float = (nota_1 * peso_1 + nota_2 * peso_2)/(peso_1 + peso_2)

    if media < 5: return ["REPROVADO", ""]
    else:
        aprovacao: str = "APROVADO"
        if media < 8: return [aprovacao, ""]
        if (media >= 8) & (media < 9): return [aprovacao, "PARABÉNS, O DESEMPENHO FOI MUITO BOM"]

        return [aprovacao, "PARABÉNS, VOCÊ FOI APROVADO COM LOUVOR"]

print("Teste 1: {}".format(weighted_average(0, 0)))
print("Teste 2: {}".format(weighted_average(4, 5.7)))
print("Teste 3: {}".format(weighted_average(4, 5.75)))
print("Teste 4: {}".format(weighted_average(7, 8.7)))
print("Teste 5: {}".format(weighted_average(7, 8.75)))
print("Teste 6: {}".format(weighted_average(8, 9.7)))
print("Teste 7: {}".format(weighted_average(8, 9.75)))


# %% [markdown]
# ## 6

# %%
def farenheit_to_celsius(temp_farenheit: float) -> float:
    return  5 * (temp_farenheit - 32)/9

def kelvin_to_celsius(temp_kelvin: float) -> float:
    return temp_kelvin - 273.15

def reaumur_to_celsius(temp_reaumur: float) -> float:
    return 5 * temp_reaumur / 4

def rankine_to_celsius(temp_rankine: float) -> float:
    return 5 * temp_rankine/9 - 273.15

escala: str = ""
temperatura: float = 0
resultado: str = ""
simbolos_escalas: dict[str, str] = {
    "FAR": "ºF",
    "KEL": "K",
    "REA": "ºRe",
    "RAN": "ºRa"
}

while(True):
    print("Escala: ")
    escala = input()

    if escala == "EXIT":
        print("Adeus!")
        break

    if simbolos_escalas.keys().__contains__(escala) == False:
        print("Escala não aceita!")
        break

    print("Temperatura: ")
    temperatura = float(input())

    match escala:
        case "FAR":
            resultado = farenheit_to_celsius(temperatura)
        
        case "KEL":
            resultado = kelvin_to_celsius(temperatura)

        case "REA":
            resultado = reaumur_to_celsius(temperatura)

        case "RAN":
            resultado = rankine_to_celsius(temperatura)

    print("Resultado conversão: {} {} = {} ºC".format(str(temperatura), str(simbolos_escalas[escala]), str(resultado)))








# %% [markdown]
# ## 12

# %%
def divisao_polinomios(x: float) -> float | str:
    if x == 0: return "erro: não se pode dividir por 0"
    return (4 * x * x - 3 * x + 9)/x

x: float = 0
print("Valor de x: ")

x = float(input())

print("Resultado: {}".format(str(divisao_polinomios(x))))


# %% [markdown]
# ## 13

# %%
def e_bissexto(ano: int) -> bool:
    return ((ano % 4 == 0) & (ano % 100 != 0)) | (ano % 400 == 0) 

ano: int = 0

print("Ano: ")
ano = int(input())

print("É bissexto? {}".format(str(e_bissexto(ano))))



