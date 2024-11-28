import time
import random

estrada = [0, 0]
semaforo = True
removidos = 0
tempodosemaforo = int(input("Quanto tempo deverá o semáforo ficar ligado/desligado? "))

def atualizarCor():
    global semaforo
    semaforo = not semaforo
    if semaforo:
        moverCarros()
    else:
        gerarCarros()
    removerCarros()

def gerarCarros():
    global estrada
    estrada[0] = random.randint(2, 10)

def moverCarros():
    global estrada
    estrada[1] += estrada[0]
    estrada[0] = 0

def removerCarros():
    global estrada, removidos
    remover = random.randint(2, 10)
    removidos = remover if estrada[1] - remover >= 5 else 0
    estrada[1] -= removidos

while True:
    atualizarCor()
    print(f"Semáforo {"verde" if semaforo else "vermelho"}. Carros à espera: {estrada[0]}, carros depois do semáforo: {estrada[1]}. {removidos} carros foram para outros lugares.")
    time.sleep(tempodosemaforo)