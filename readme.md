## funcion crear tablero
    crea un tablero de 4 columnas y 12 filas

## funcion de generar secuencia correcta
    la maquina genera una secuancia de colores usando una libreria

## funcion obtener intento del jugador 
    obtienen la secuencia del jugador mediante un input y la valida con los colores disponibles para que no se ingrese un color valido

## funcion comparar secuencias
    compara la secuencia del jugador con la secuencia secreta para validae el gane y 
    se asigna 'green' a las posiciones correctas
    se asigna 'yellow' a los colores correctos en posiciones incorrectas

## funcion actualizar tablero 
    actualiza el tablero con los colores correspondientes

## funcion imprimir tablero
    imprime el tablero

## funcion jugador adivina
    le da 12 intentos al jugador de adivinar la secuencia y valida la secuencia del jugador con la secuencia secreta
    generada aleatoriamente para dar pistas o dar el gane

## funcion maquina adivina
    le da a la maquina 12 intentos para adivinar la secuencia puesta por el jugador, la maquina lo hace de forma aleatoria y se logra ver la decicion de la maquina y tambien le genera pistas

## funcion maquina demon (PERSONAL)
    le da a la maquina 12 intentos de adivinar la secuencia pero lo hace en 2 intentod ya que en el segundo intento le digo que el intento maquina sea igual al codigo secreto

## funcion mastermind 
    maneja el flujo del juego de forma que divide los roles de adivinador y creador del codigo secreto



## Instrucciones Generales
    Iniciar el Juego:
    Al comenzar, se te pedirá que elijas el rol que deseas: creador o adivinador.

    Elegir el Modo de Juego:
    Si eliges creador, también podrás elegir el modo en el que la máquina adivinadora operará: aleatorio, estratega, o hell.

## Modo: Creador
    Establecer la Secuencia Secreta:

    Como creador, debes elegir una secuencia de 4 colores. Los colores disponibles son: red, green, blue, yellow, orange, brown.
    Escribe cada color cuando se te pida. Esta será la secuencia que la máquina intentará adivinar.
    Jugar Contra la Máquina:

    La máquina intentará adivinar tu secuencia en 12 intentos.
    Después de cada intento, el tablero se actualizará y mostrará las pistas sobre qué tan cerca estuvo la máquina de adivinar tu secuencia.

## Modo: Adivinador
    Intentar Adivinar la Secuencia Secreta:

    Como adivinador, debes intentar adivinar una secuencia de 4 colores que ha sido creada por la máquina.
    Introduce tu secuencia de colores cuando se te pida.
    Recibir Pistas:

    Después de cada intento, el tablero se actualizará y te proporcionará pistas sobre cuántos colores están en la posición correcta (verde) y cuántos están en la secuencia pero en la posición incorrecta (amarillo).
    Ganancia o Pérdida:

    Si adivinas la secuencia correcta dentro de los 12 intentos, ganarás el juego.
    Si se acaban los intentos sin adivinar la secuencia, el juego te mostrará cuál era la secuencia correcta.


## Modos de Juego para la Máquina (Cuando Eres el Creador)

    ## Modo Aleatorio:
        La máquina adivinará secuencias de colores de forma aleatoria en cada intento.

    ## Modo Estratega:
        La máquina utilizará una estrategia de adivinanza más avanzada para tratar de reducir las opciones posibles y adivinar la secuencia correcta.

    ## Modo Hell:
        En este modo, la máquina intentará adivinar la secuencia correcta de manera más agresiva, usando un enfoque que puede parecer menos aleatorio pero más específico para tratar de encontrar la secuencia.


## Visualización en el Juego
    El tablero principal muestra tus intentos y las pistas en forma de colores.
    El tablero secundario muestra el progreso de la máquina o del jugador en términos de aciertos (🟢) o fallos (⚪).

## Resumido:
    Elige tu rol (creador o adivinador).
    Si eres el creador: Establece la secuencia secreta y selecciona el modo de la máquina.
    Si eres el adivinador: Intenta adivinar la secuencia correcta en 12 intentos.
    Sigue las pistas proporcionadas y usa la estrategia adecuada para ganar.
    ¡Diviértete jugando a Mastermind!