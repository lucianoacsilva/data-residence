# %% [markdown]
# # Aula 4

# %% [markdown]
# ## Exercício 1

# %%
def intervalo(inferior: int, superior: int) -> None:
    for i in range(inferior, superior + 1):
        print(i)

inferior: int = 0
superior: int = 0

print("Limite inferior: ")
inferior = int(input())

print("Limite superior: ")
superior = int(input())

print("Números entre {} e {}: ".format(str(inferior), str(superior)))
intervalo(inferior, superior)

# %% [markdown]
# ## Exercício 2

# %%
def media(valores: list[float]) -> float:
    media: float = 0

    for val in valores:
        media += val

    return media/len(valores)

valores: list[float] = []
tamanho_valores: int = 0

print("Quantidade de valores: ")
tamanho_valores = int(input())

print("Insira valores: ")

for i in range(tamanho_valores):
    valores.append(float(input()))

print("Media: {}".format(str(media(valores))))


# %% [markdown]
# ## Exercício 3

# %%
def media(valores: list[float]) -> float:
    media: float = 0

    for val in valores:
        media += val

    return media/len(valores)

def valor_minimo(valores: list[float]) -> float:
    val_minimo: float = valores[0]

    for val in valores:
        if val_minimo > val: val_minimo = val

    return val_minimo

def valor_maximo(valores: list[float]) -> float:
    val_maximo: float = valores[0]

    for val in valores:
        if val_maximo < val: val_maximo = val

    return val_maximo

valores: list[float] = []
tamanho_valores: int = 0

print("Quantidade de valores: ")
tamanho_valores = int(input())

print("Insira valores: ")

for i in range(tamanho_valores):
    valores.append(float(input()))

print("Media: {}; Mínimo: {}; Máximo: {}".format(
    str(media(valores)), 
    str(valor_minimo(valores)), 
    str(valor_maximo(valores))
))

# %% [markdown]
# ## Exercício 4

# %%
def fatorial(numero: int) -> int:
    if (numero == 1)| (numero == 0): return 1
    else: return numero * fatorial(numero - 1)

numero: int = 0

print("Número: ")
numero = int(input())

print("Fatorial: de {}: {}".format(str(numero), str(fatorial(numero))))


# %% [markdown]
# ## Exercício 5

# %%
def tabuada(numero: int) -> None:
    for i in range(11):
        print(str(numero * i))

numero: int = 0

print("Número: ")
numero = int(input())

print("Tabuada do {}: ".format(str(numero)))
tabuada(numero)

# %% [markdown]
# ## Exercício 6

# %%
def temperatura(dia: int) -> float:
    return 0.011 * dia ** 3 - 0.3 * dia ** 2 + 0.04 * dia

def menor_dia_temperatura(limite_superior: int) -> int:
    dia: int = 0
    menor_temperatura: float = temperatura(0)

    for i in range(1,limite_superior + 1):
        if temperatura(i) < menor_temperatura: dia = i

    return dia

def main() -> str:
    limite_superior: int = 0

    print("Dia de limite superior: ")
    limite_superior = int(input())

    if limite_superior > 30: return "Limite superior não pode ultrapassar o dia 30!"

    return "Dia com menor temperatura: {}".format(str(menor_dia_temperatura(limite_superior)))

print(main())



# %% [markdown]
# ## Exercício 7

# %%
import random

def adivinha(numero_jogador: int, numero_computador: int) -> str:
    if numero_jogador > numero_computador: return "O seu número é MAIOR que o do computador"
    elif numero_jogador < numero_computador:return "O seu número é MENOR que o do computador"

    return "PARABÉNS, VOCÊ ACERTOU O NÚMERO"

numero_computador: int = random.randint(0,100)

print("\n**********************************")
print("JOGO: ADIVINHE O NÚMERO (0 a 100)\n")

numero_jogador: int = -1

while numero_jogador != numero_computador:
    numero_jogador = int(input("DIGITE UM NÚMERO: "))

    print(adivinha(numero_jogador, numero_computador))

# %% [markdown]
# ## Exercício 8

# %%
import random

def adivinha(numero_jogador: int, numero_computador: int) -> str:
    if numero_jogador > numero_computador: return "O seu número é MAIOR que o do computador"
    elif numero_jogador < numero_computador: return "O seu número é MENOR que o do computador"

    return "PARABÉNS, VOCÊ ACERTOU O NÚMERO"

numero_computador: int = random.randint(0,100)
numero_jogador: int = 0
tentativas: int = 0

print("\n**********************************")
print("JOGO: ADIVINHE O NÚMERO (0 a 100)\n")

while numero_jogador != numero_computador:
    numero_jogador = int(input("DIGITE UM NÚMERO: "))

    print(adivinha(numero_jogador, numero_computador))
    tentativas += 1

print("Tentativas: {}".format(str(tentativas)))

# %% [markdown]
# ## Exercício 9

# %%
import random

def adivinha(numero_jogador: int, numero_computador: int) -> str:
    if numero_jogador > numero_computador: return "O seu número é MAIOR que o do computador"
    elif numero_jogador < numero_computador: return "O seu número é MENOR que o do computador"

    return "PARABÉNS, VOCÊ ACERTOU O NÚMERO"

numero_computador: int = random.randint(0,100)
numero_jogador: int = 0
tentativas: int = 0

print("\n**********************************")
print("JOGO: ADIVINHE O NÚMERO (0 a 100)\n")

while numero_jogador != numero_computador:
    numero_jogador = int(input("DIGITE UM NÚMERO (PARA DESISTIR, DIGITE -1): "))

    if numero_jogador == -1:
        print("ATÉ MAIS")
        break

    print(adivinha(numero_jogador, numero_computador))
    tentativas += 1

print("Tentativas: {}".format(str(tentativas)))

# %% [markdown]
# ## Exercício 10

# %%
import random

def adivinha(numero_jogador: int, numero_computador: int) -> str:
    if numero_jogador > numero_computador: return "O seu número é MAIOR que o do computador"
    elif numero_jogador < numero_computador: return "O seu número é MENOR que o do computador"

    return "PARABÉNS, VOCÊ ACERTOU O NÚMERO"

numero_computador: int = random.randint(0,100)
numero_jogador: int = 0
tentativas: int = 0
quer_jogar: bool = True

print("\n**********************************")
print("JOGO: ADIVINHE O NÚMERO (0 a 100)\n")

while quer_jogar:
    while numero_jogador != numero_computador:
        numero_jogador = int(input("DIGITE UM NÚMERO (PARA DESISTIR, DIGITE -2; PARA INICIAR NOVA PARTIDA, -1): "))

        if numero_jogador == -1:
            print("OK! VAMOS REINICIAR")
            tentativas = 0
            break

        if numero_jogador == -2:
            print("ATÉ MAIS!")
            quer_jogar = False
            break

        print(adivinha(numero_jogador, numero_computador))
        tentativas += 1

    print("Tentativas: {}".format(str(tentativas)))
    numero_jogador = -999999

# %% [markdown]
# ## Exercício 11

# %%
def multiplos_de_tres(inferior: int, superior: int) -> list[int]:
    multiplos: list[int] = []

    for n in range(inferior, superior + 1):
        if n % 3 == 0: multiplos.append(n)

    return multiplos

inferior: int = 0
superior: int = 0

print("Limite inferior: ")
inferior = int(input())

print("Limite superior: ")
superior = int(input())

print("Multiplos de 3 no intervalo: {}".format(str(multiplos_de_tres(inferior, superior))))




# %% [markdown]
# ## Exercício 12

# %%
def multiplos_de_tres(inferior: int, superior: int, divisor: int) -> list[int] | str:
    if divisor == 0: return "Não se pode dividir por 0!"

    multiplos: list[int] = []

    for n in range(inferior, superior + 1):
        if n % divisor == 0: multiplos.append(n)

    return multiplos

inferior: int = 0
superior: int = 0
divisor: int = 0

print("Limite inferior: ")
inferior = int(input())

print("Limite superior: ")
superior = int(input())

print("Limite divisor: ")
divisor = int(input())

print("Multiplos de 3 no intervalo: {}".format(str(multiplos_de_tres(inferior, superior, divisor))))




# %% [markdown]
# ## Exercício 13

# %%
def imprime() -> None:
    lista = ["GUARANI", "SÃO PAULO", "PALMEIRAS", "CRUZEIRO", "SANTOS", "FERROVIÁRIA",
             "JUVENTUS", "GOIÁS", "ÍBIS", "SINOP"]
    
    for i in range(len(lista)):
        print("{} - {}".format(str(i), lista[i]))

imprime()

# %% [markdown]
# ## Exercício 14

# %%
from random import randint

def jankepo(humano: int, computador: int) -> str:
    matriz_verdade: list[list[int]] = [
        [0, -1, 1], 
        [1, 0, -1],
        [-1, 1, 0]
    ]

    resultado: int = matriz_verdade[humano][computador]

    match resultado:
        case -1:
            return "VOCÊ PERDEU!"
        
        case 0:
            return "EMPATE!"
        
        case 1:
            return "VOCÊ GANHOU!"

computador: int = int(randint(0,301)/100)
humano: int = 0

print("Palpite: (0 para PEDRA, 1 para PAPEL e 2 para TESOURA)")
humano = int(input())

print("Computador: {}".format(str(computador)))
print(jankepo(humano, computador))


# %% [markdown]
# ## Exercício 15

# %%
from random import randint

def jankepo(humano: int, computador: int) -> str:
    matriz_verdade: list[list[int]] = [
        [0, -1, 1], 
        [1, 0, -1],
        [-1, 1, 0]
    ]

    resultado: int = matriz_verdade[humano][computador]

    match resultado:
        case -1:
            return "VOCÊ PERDEU!"
        
        case 0:
            return "EMPATE!"
        
        case 1:
            return "VOCÊ GANHOU!"
        
def main() -> str:
    computador: int = int(randint(0,301)/100)
    humano: int = 0

    print("Palpite: (0 para PEDRA, 1 para PAPEL e 2 para TESOURA)")
    humano = int(input())

    print("Humano: {}".format(str(humano)))
    if (humano < 0) | (humano > 2): return "OPÇÃO INVÁLIDA!"

    print("Computador: {}".format(str(computador)))

    return jankepo(humano, computador)

print(main())



