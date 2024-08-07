import random
import itertools  
from termcolor import colored
import time  

COLORES_DISPONIBLES = ['red', 'green', 'blue', 'yellow', 'orange', 'brown']
PELOTA = "O"

class Tablero:
    def __init__(self):
        self.tablero = [[PELOTA for _ in range(4)] for _ in range(12)]

    def actualizar_tablero(self, intento_jugador, pistas, fila_actual):
        for i in range(4):
            if pistas[i] == 'green':
                self.tablero[fila_actual][i] = colored(PELOTA, 'green')
            elif pistas[i] == 'yellow':
                self.tablero[fila_actual][i] = colored(PELOTA, 'yellow')
            else:
                self.tablero[fila_actual][i] = colored(PELOTA, 'white')

    def imprimir_tablero(self):
        for fila in self.tablero:
            print(' | '.join(fila))
            print()

class Jugador:
    def obtener_intento_jugador(self):
        intento = []
        print("Introduce tus colores (elige entre: red, green, blue, yellow, orange, brown):")
        for i in range(4):
            color = input(f"Color {i+1}: ").strip().lower()
            while color not in COLORES_DISPONIBLES:
                print("Color no válido. Intenta de nuevo.")
                color = input(f"Color {i+1}: ").strip().lower()
            intento.append(color)
        return intento

class Secuencia:
    @staticmethod
    def generar_secuencia_correcta():
        return random.sample(COLORES_DISPONIBLES, 4)

    @staticmethod
    def comparar_secuencias(secuencia_correcta, intento_jugador):
        pistas = ['default'] * 4
        secuencia_correcta_temp = secuencia_correcta[:]
        intento_jugador_temp = intento_jugador[:]

        for i in range(4):
            if intento_jugador[i] == secuencia_correcta[i]:
                pistas[i] = 'green'
                secuencia_correcta_temp[i] = None
                intento_jugador_temp[i] = None

        for i in range(4):
            if intento_jugador_temp[i] is not None:
                if intento_jugador_temp[i] in secuencia_correcta_temp:
                    pistas[i] = 'yellow'
                    secuencia_correcta_temp[secuencia_correcta_temp.index(intento_jugador_temp[i])] = None

        return pistas

class MaquinaEstratega:
    def __init__(self):
        self.colores = COLORES_DISPONIBLES
        self.historial = []

    def trampas(self):
        if not self.historial:
            return random.choices(self.colores, k=4)
        ultima_secuencia, ultimos_verificadores = self.historial[-1]
        nueva_secuencia = ultima_secuencia[:]
        for i in range(4):
            if ultimos_verificadores[i] == 'green':
                continue
            elif ultimos_verificadores[i] == 'yellow':
                colores_restantes = [color for color in self.colores if color != ultima_secuencia[i]]
                nueva_secuencia[i] = random.choice(colores_restantes)
            else:
                nueva_secuencia[i] = random.choice(self.colores)
        return nueva_secuencia

class JuegoMastermind:
    def __init__(self):
        self.tablero = Tablero()
        self.jugador = Jugador()
        self.secuencia = Secuencia()

    def jugador_adivina(self):
        secuencia_correcta = self.secuencia.generar_secuencia_correcta()
        intentos_restantes = 12
        fila_actual = 0

        while intentos_restantes > 0:
            intento_jugador = self.jugador.obtener_intento_jugador()
            pistas = self.secuencia.comparar_secuencias(secuencia_correcta, intento_jugador)
            self.tablero.actualizar_tablero(intento_jugador, pistas, fila_actual)
            self.tablero.imprimir_tablero()

            if pistas == ['green', 'green', 'green', 'green']:
                print("¡Felicidades! Adivinaste la secuencia correcta.")
                break

            fila_actual += 1
            intentos_restantes -= 1
            print(f"Te quedan {intentos_restantes} intentos.\n")

        if intentos_restantes == 0:
            print("Se te acabaron los intentos. La secuencia correcta era:", secuencia_correcta)

    def maquina_adivina(self):
        secuencia_correcta = self.jugador.obtener_intento_jugador()
        intentos_restantes = 12
        fila_actual = 0

        while intentos_restantes != 0:
            posibles_combinaciones = [list(seq) for seq in set(itertools.permutations(COLORES_DISPONIBLES, 4))]
            intento_maquina = random.choice(posibles_combinaciones)
            print(f"La máquina intenta: {intento_maquina}")
            pistas = self.secuencia.comparar_secuencias(secuencia_correcta, intento_maquina)
            self.tablero.actualizar_tablero(intento_maquina, pistas, fila_actual)
            self.tablero.imprimir_tablero()

            if intento_maquina == secuencia_correcta:
                print("¡La máquina adivinó tu secuencia!")
                break

            posibles_combinaciones = [comb for comb in posibles_combinaciones if self.secuencia.comparar_secuencias(intento_maquina, comb) == pistas]

            fila_actual += 1
            intentos_restantes -= 1
            print(f"La máquina tiene {intentos_restantes} intentos restantes.\n")
            time.sleep(1)

        if intentos_restantes == 0:
            print("La máquina no pudo adivinar tu secuencia.")

    def maquina_estratega(self):
        secuencia_correcta = self.jugador.obtener_intento_jugador()
        intentos_restantes = 12
        fila_actual = 0

        estrategia = MaquinaEstratega()

        while intentos_restantes > 0:
            intento_maquina = estrategia.trampas()
            print(f"La máquina intenta: {intento_maquina}")
            pistas = self.secuencia.comparar_secuencias(secuencia_correcta, intento_maquina)
            estrategia.historial.append((intento_maquina, pistas))
            self.tablero.actualizar_tablero(intento_maquina, pistas, fila_actual)
            self.tablero.imprimir_tablero()

            if pistas == ['green', 'green', 'green', 'green']:
                print("¡La máquina adivinó tu secuencia!")
                break

            fila_actual += 1
            intentos_restantes -= 1
            print(f"La máquina tiene {intentos_restantes} intentos restantes.\n")
            time.sleep(1)

        if intentos_restantes == 0:
            print("La máquina no pudo adivinar tu secuencia.")

    def maquina_demon(self):
        secuencia_correcta = self.jugador.obtener_intento_jugador()
        intentos_restantes = 12
        fila_actual = 0

        # Primer intento aleatorio
        intento_maquina = random.choices(COLORES_DISPONIBLES, k=4)
        print(f"La máquina intenta: {intento_maquina}")
        pistas = self.secuencia.comparar_secuencias(secuencia_correcta, intento_maquina)
        self.tablero.actualizar_tablero(intento_maquina, pistas, fila_actual)
        self.tablero.imprimir_tablero()

        fila_actual += 1
        intentos_restantes -= 1
        print(f"La máquina tiene {intentos_restantes} intentos restantes.\n")
        time.sleep(1)

        # Segundo intento usando la secuencia correcta
        intento_maquina = secuencia_correcta
        print(f"La máquina intenta: {intento_maquina}")
        pistas = self.secuencia.comparar_secuencias(secuencia_correcta, intento_maquina)
        self.tablero.actualizar_tablero(intento_maquina, pistas, fila_actual)
        self.tablero.imprimir_tablero()

        if pistas == ['green', 'green', 'green', 'green']:
            print("¡La máquina adivinó tu secuencia!")
        else:
            print("La máquina no pudo adivinar tu secuencia, pero debería haberlo hecho.")

    def iniciar_juego(self):
        print("Bienvenido al juego de Mastermind!")
        modo = input("¿Quieres ser el creador del código o el adivinador? (creador/adivinador): ").strip().lower()

        if modo == 'creador':
            modo_maquina = input("Elige el modo de la maquina (Aleatorio/Estratega/Hell): ").strip().lower()
            if modo_maquina == 'aleatorio':
                self.maquina_adivina()
            elif modo_maquina == 'estratega':
                self.maquina_estratega()
            elif modo_maquina == 'hell':
                self.maquina_demon()
        elif modo == 'adivinador':
            self.jugador_adivina()
        else:
            print("Opción no válida. Por favor, reinicia el juego e ingresa una opción válida.")

if __name__ == "__main__":
    juego = JuegoMastermind()
    juego.iniciar_juego()
