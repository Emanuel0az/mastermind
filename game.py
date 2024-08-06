import random
import itertools  
from termcolor import colored
import time  


COLORES_DISPONIBLES = ['red', 'green', 'blue', 'yellow', 'orange', 'brown']


PELOTA = "O"


def crear_tablero():
    return [[PELOTA for _ in range(4)] for _ in range(6)]


def generar_secuencia_correcta():
    return random.sample(COLORES_DISPONIBLES, 4)


def obtener_intento_jugador():
    intento = []
    print("Introduce tus colores (elige entre: red, green, blue, yellow, orange, brown):")
    for i in range(4):
        color = input(f"Color {i+1}: ").strip().lower()
        while color not in COLORES_DISPONIBLES:
            print("Color no válido. Intenta de nuevo.")
            color = input(f"Color {i+1}: ").strip().lower()
        intento.append(color)
    return intento

# Compara la secuencia del jugador con la secuencia correcta
def comparar_secuencias(secuencia_correcta, intento_jugador):
    pistas = ['default'] * 4
    secuencia_correcta_temp = secuencia_correcta[:]
    intento_jugador_temp = intento_jugador[:]

    # se asigna 'green' a las posiciones correctas
    for i in range(4):
        if intento_jugador[i] == secuencia_correcta[i]:
            pistas[i] = 'green'
            secuencia_correcta_temp[i] = None  # se marca el color como usado
            intento_jugador_temp[i] = None  # se marca el color como usado

    # se asigna 'yellow' a los colores correctos en posiciones incorrectas
    for i in range(4):
        if intento_jugador_temp[i] is not None:
            if intento_jugador_temp[i] in secuencia_correcta_temp:
                pistas[i] = 'yellow'
                secuencia_correcta_temp[secuencia_correcta_temp.index(intento_jugador_temp[i])] = None

    return pistas


def actualizar_tablero(tablero, intento_jugador, pistas, fila_actual):
    for i in range(4):
        if pistas[i] == 'green':
            tablero[fila_actual][i] = colored(PELOTA, 'green')
        elif pistas[i] == 'yellow':
            tablero[fila_actual][i] = colored(PELOTA, 'yellow')
        else:
            tablero[fila_actual][i] = colored(PELOTA, 'white')


def imprimir_tablero(tablero):
    for fila in tablero:
        print(' '.join(fila))
        print()


def jugador_adivina():
    secuencia_correcta = generar_secuencia_correcta()
    tablero = crear_tablero()
    intentos_restantes = 6
    fila_actual = 0

    while intentos_restantes > 0:
        intento_jugador = obtener_intento_jugador()
        pistas = comparar_secuencias(secuencia_correcta, intento_jugador)
        actualizar_tablero(tablero, intento_jugador, pistas, fila_actual)
        imprimir_tablero(tablero)

        if pistas == ['green', 'green', 'green', 'green']:
            print("¡Felicidades! Adivinaste la secuencia correcta.")
            break

        fila_actual += 1
        intentos_restantes -= 1
        print(f"Te quedan {intentos_restantes} intentos.\n")

    if intentos_restantes == 0:
        print("Se te acabaron los intentos. La secuencia correcta era:", secuencia_correcta)


def maquina_adivina():
    secuencia_correcta = obtener_intento_jugador()  
    tablero = crear_tablero()
    intentos_restantes = 6
    fila_actual = 0
    posibles_combinaciones = [list(seq) for seq in set(itertools.permutations(COLORES_DISPONIBLES, 4))]

    while intentos_restantes > 0 and posibles_combinaciones:
        intento_maquina = random.choice(posibles_combinaciones)
        print(f"La máquina intenta: {intento_maquina}")
        pistas = comparar_secuencias(secuencia_correcta, intento_maquina)
        actualizar_tablero(tablero, intento_maquina, pistas, fila_actual)
        imprimir_tablero(tablero)

      
        if intento_maquina == secuencia_correcta:
            print("¡La máquina adivinó tu secuencia!")
            break


        posibles_combinaciones = [comb for comb in posibles_combinaciones if comparar_secuencias(intento_maquina, comb) == pistas]

        fila_actual += 1
        intentos_restantes -= 1
        print(f"La máquina tiene {intentos_restantes} intentos restantes.\n")
        time.sleep(1)  # se añade un tiempo de espera de 1 segundo

    if intentos_restantes == 0:
        print("La máquina no pudo adivinar tu secuencia.")

# función principal que controla el flujo del juego
def mastermind():
    print("Bienvenido al juego de Mastermind!")
    modo = input("¿Quieres ser el creador del código o el adivinador? (creador/adivinador): ").strip().lower()

    if modo == 'creador':
        maquina_adivina()
    elif modo == 'adivinador':
        jugador_adivina()
    else:
        print("Opción no válida. Por favor, reinicia el juego e ingresa una opción válida.")


if __name__ == "__main__":
    mastermind()
