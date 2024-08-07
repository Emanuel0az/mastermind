import random
import itertools
import time
from termcolor import colored

COLORES_DISPONIBLES = ['red', 'green', 'blue', 'yellow', 'orange', 'brown']
PELOTA = "O"

class Tablero :
    def __init__(self):
        self.tablero = [[PELOTA for _ in range(4)] for _ in range(12)]
    
    def actualizar_tablero(self, intento_jugador, pistas, fila_actual):
        for i in range(4):
            if pistas[i] == "green":
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
            color = input(f"color {i+1}: ").strip().lower()
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
    def comparar_secuencia(secuencia_correcta, intento_jugador):
        pistas =['default'] +4
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
    
class MaquinaEstratega :
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


        
        
        

        