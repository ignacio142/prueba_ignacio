import random

def imprimir_tablero(tablero):
    """Imprime el tablero del juego"""
    for fila in tablero:
        print(" | ".join(fila))
        print("-" * 5)

def verificar_ganador(tablero, jugador):
    """Verifica si el jugador actual ha ganado"""
    # Verificar filas y columnas
    for i in range(3):
        if all(tablero[i][j] == jugador for j in range(3)) or all(tablero[j][i] == jugador for j in range(3)):
            return True

    # Verificar diagonales
    if all(tablero[i][i] == jugador for i in range(3)) or all(tablero[i][2-i] == jugador for i in range(3)):
        return True

    return False

def tablero_lleno(tablero):
    """Verifica si el tablero está lleno"""
    return all(celda != ' ' for fila in tablero for celda in fila)

def principal():
    """Función principal del juego"""
    nombre_usuario = input("Por favor, ingresa tu nombre de usuario: ")

    while True:
        print("MENÚ:")
        print("1. Nueva Partida contra IA")
        print("2. Versus")
        print("3. Salir")
        eleccion = input("Elige una opción: ")

        if eleccion == '1':  # Nueva Partida contra IA
            jugar(0, nombre_usuario)
        elif eleccion == '2':  # Versus
            jugar(1, nombre_usuario)
        elif eleccion == '3':  # Salir
            print("¡Gracias por jugar! ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, elige nuevamente.")

def jugar(modo, nombre_usuario):
    """Función que maneja la lógica del juego según el modo seleccionado"""
    tablero = [[' ']*3 for _ in range(3)]
    jugadores = ['X', 'O']
    turno = 0

    while True:
        imprimir_tablero(tablero)
        if modo == 0 and turno == 1:  # Turno de la IA
            print(f"Turno de la IA ({jugadores[turno]}).")
            fila, columna = movimiento_ia(tablero)
        else:
            print(f"Turno de {nombre_usuario if turno == 0 else 'JUGADOR 2'} ({jugadores[turno]}).")
            fila = int(input("Ingresa fila (0, 1, o 2): "))
            columna = int(input("Ingresa columna (0, 1, o 2): "))

        if fila not in range(3) or columna not in range(3):
            print("Fila o columna inválida. Por favor, ingresa nuevamente.")
            continue

        if tablero[fila][columna] != ' ':
            print("¡Esa celda ya está ocupada! Inténtalo de nuevo.")
            continue

        tablero[fila][columna] = jugadores[turno]

        if verificar_ganador(tablero, jugadores[turno]):
            imprimir_tablero(tablero)
            print(f"¡{nombre_usuario if turno == 0 else 'JUGADOR 2'} FELICIDADES, HAS GANADO!" if modo == 1 else f"¡{nombre_usuario if turno == 0 else 'IA'} FELICIDADES, HAS GANADO!")
            break
        elif tablero_lleno(tablero):
            imprimir_tablero(tablero)
            print("¡Es un empate!")
            break

        turno = (turno + 1) % 2

def movimiento_ia(tablero):
    """Función que determina el movimiento de la IA seleccionando una celda vacía al azar"""
    celdas_vacias = [(i, j) for i in range(3) for j in range(3) if tablero[i][j] == ' ']
    return random.choice(celdas_vacias)

if __name__ == "__main__":
    principal()
