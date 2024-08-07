def logicaDificil(self):
        if not self.historial:
            return random.choices(self.colores, k=4)
        ultima_secuencia, ultimos_verificadores = self.historial[-1]
        nueva_secuencia = ultima_secuencia[:]
        for i in range(4):
            if ultimos_verificadores[i] == Fore.GREEN + ":círculo_verde_grande:" + Fore.RESET:
                continue
            elif ultimos_verificadores[i] == Fore.YELLOW + ":círculo_amarillo_grande:" + Fore.RESET:
                colores_restantes = [color for color in self.colores if color != ultima_secuencia[i]]
                nueva_secuencia[i] = random.choice(colores_restantes)
            else:
                nueva_secuencia[i] = random.choice(self.colores)
        return nueva_secuencia