import random
import itertools  
from termcolor import colored
import time  

COLORES_DISPONIBLES = ['red', 'green', 'blue', 'yellow', 'orange', 'brown']
PELOTA = "O"

class Tablero:
    def __init__(self, filas=12, columnas=4):
        self.filas = filas
        self.columnas = columnas
        self.tablero = [[PELOTA for _ in range(columnas)] for _ in range(filas)]

    def actualizar(self, intento, pistas, fila):
        for i in range(self.columnas):
            if pistas[i] == 'green':
                self.tablero[fila][i] = colored(PELOTA, 'green')
            elif pistas[i] == 'yellow':
                self.tablero[fila][i] = colored(PELOTA, 'yellow')
            else:
                self.tablero[fila][i] = colored(PELOTA, 'white')

    def imprimir(self, tablero_secundario=None):
        for fila_secundaria, fila_principal in zip(tablero_secundario.tablero, self.tablero):
            fila_completa = ' | '.join(fila_secundaria) + "    " + ' | '.join(fila_principal)
            print(fila_completa)
            print()

class TableroSecundario:
    def __init__(self, filas=12, columnas=4):
        self.filas = filas
        self.columnas = columnas
        self.tablero = [["⚪" for _ in range(columnas)] for _ in range(filas)]

    def marcar_fila_ganadora(self, fila):
        for i in range(self.columnas):
            self.tablero[fila][i] = "🟢"

class Jugador:
    def __init__(self):
        pass

    def obtener_intento(self):
        intento = []
        print("Introduce tus colores (elige entre: red, green, blue, yellow, orange, brown):")
        for i in range(4):
            color = input(f"Color {i+1}: ").strip().lower()
            while color not in COLORES_DISPONIBLES:
                print("Color no válido. Intenta de nuevo.")
                color = input(f"Color {i+1}: ").strip().lower()
            intento.append(color)
        return intento

class Maquina:
    def __init__(self):
        self.historial = []

    def generar_secuencia(self):
        return random.sample(COLORES_DISPONIBLES, 4)

    def logica_dificil(self):
        if not self.historial:
            return random.choices(COLORES_DISPONIBLES, k=4)
        ultima_secuencia, ultimos_verificadores = self.historial[-1]
        nueva_secuencia = ultima_secuencia[:]
        for i in range(4):
            if ultimos_verificadores[i] == 'green':
                continue
            elif ultimos_verificadores[i] == 'yellow':
                colores_restantes = [color for color in COLORES_DISPONIBLES if color != ultima_secuencia[i]]
                nueva_secuencia[i] = random.choice(colores_restantes)
            else:
                nueva_secuencia[i] = random.choice(COLORES_DISPONIBLES)
        return nueva_secuencia

    def adivinar(self, modo='estratega', secuencia_correcta=None):
        if modo == 'estratega':
            return self.logica_dificil()
        elif modo == 'hell':
            if len(self.historial) == 0:
                return random.choices(COLORES_DISPONIBLES, k=4)
            else:
                return secuencia_correcta
        else:
            return random.sample(COLORES_DISPONIBLES, 4)

class Juego:
    def __init__(self):
        self.tablero = Tablero()
        self.tablero_secundario = TableroSecundario()
        self.jugador = Jugador()
        self.maquina = Maquina()

    def comparar_secuencias(self, secuencia_correcta, intento):
        pistas = ['default'] * 4
        secuencia_correcta_temp = secuencia_correcta[:]
        intento_temp = intento[:]

        for i in range(4):
            if intento[i] == secuencia_correcta[i]:
                pistas[i] = 'green'
                secuencia_correcta_temp[i] = None
                intento_temp[i] = None

        for i in range(4):
            if intento_temp[i] is not None:
                if intento_temp[i] in secuencia_correcta_temp:
                    pistas[i] = 'yellow'
                    secuencia_correcta_temp[secuencia_correcta_temp.index(intento_temp[i])] = None

        return pistas

    def jugador_adivina(self):
        secuencia_correcta = self.maquina.generar_secuencia()
        intentos_restantes = 12
        fila_actual = 0

        while intentos_restantes > 0:
            intento_jugador = self.jugador.obtener_intento()
            pistas = self.comparar_secuencias(secuencia_correcta, intento_jugador)
            self.tablero.actualizar(intento_jugador, pistas, fila_actual)
            if pistas == ['green', 'green', 'green', 'green']:
                self.tablero_secundario.marcar_fila_ganadora(fila_actual)
            self.tablero.imprimir(tablero_secundario=self.tablero_secundario)

            if pistas == ['green', 'green', 'green', 'green']:
                print("¡Felicidades! Adivinaste la secuencia correcta.")
                break

            fila_actual += 1
            intentos_restantes -= 1
            print(f"Te quedan {intentos_restantes} intentos.\n")

        if intentos_restantes == 0:
            print("Se te acabaron los intentos. La secuencia correcta era:", secuencia_correcta)

    def maquina_adivina(self, modo='estratega'):
        secuencia_correcta = self.jugador.obtener_intento()
        intentos_restantes = 12
        fila_actual = 0

        while intentos_restantes > 0:
            intento_maquina = self.maquina.adivinar(modo=modo, secuencia_correcta=secuencia_correcta)
            print(f"La máquina intenta: {intento_maquina}")
            pistas = self.comparar_secuencias(secuencia_correcta, intento_maquina)
            self.maquina.historial.append((intento_maquina, pistas))
            self.tablero.actualizar(intento_maquina, pistas, fila_actual)
            if pistas == ['green', 'green', 'green', 'green']:
                self.tablero_secundario.marcar_fila_ganadora(fila_actual)
            self.tablero.imprimir(tablero_secundario=self.tablero_secundario)

            if pistas == ['green', 'green', 'green', 'green']:
                print("¡La máquina adivinó tu secuencia!")
                break

            fila_actual += 1
            intentos_restantes -= 1
            print(f"La máquina tiene {intentos_restantes} intentos restantes.\n")
            time.sleep(1)

        if intentos_restantes == 0:
            print("La máquina no pudo adivinar tu secuencia.")

    def iniciar(self):
        print("Bienvenido al juego de Mastermind!")
        modo = input("¿Quieres ser el creador del código o el adivinador? (creador/adivinador): ").strip().lower()

        if modo == 'creador':
            modo_maquina = input("Elige el modo de la maquina (aleatorio/estratega/hell): ").strip().lower()
            self.maquina_adivina(modo=modo_maquina)
        elif modo == 'adivinador':
            self.jugador_adivina()
        else:
            print("Opción no válida. Por favor, reinicia el juego e ingresa una opción válida.")

if __name__ == "__main__":
    juego = Juego()
    juego.iniciar()
