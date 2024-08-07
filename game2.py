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
            
    
        