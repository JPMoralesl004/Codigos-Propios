import random

class Carta:
    class Color:
        ROJO = 'rojo'
        AMARILLO = 'amarillo'
        VERDE = 'verde'
        AZUL = 'azul'
        NINGUNO = 'ninguno'

    class Tipo:
        SALTAR = 'saltar'
        REVERSO = 'reverso'
        ROBA_DOS = 'roba_dos'
        COMODIN = 'comodin'
        COMODIN_ROBA_CUATRO = 'comodin_roba_cuatro'
        NUMERO = 'numero'

    def __init__(self, color, tipo, valor=None):
        self.color = color
        self.tipo = tipo
        self.valor = valor

    def __str__(self):
        return f"{self.color} {self.tipo} {self.valor if self.valor is not None else ''}"

class Mazo:
    def __init__(self):
        self.cartas = self.crear_mazo()

    def crear_mazo(self):
        colores = [Carta.Color.ROJO, Carta.Color.AMARILLO, Carta.Color.VERDE, Carta.Color.AZUL]
        tipos = [Carta.Tipo.SALTAR, Carta.Tipo.REVERSO, Carta.Tipo.ROBA_DOS, Carta.Tipo.COMODIN,
                 Carta.Tipo.COMODIN_ROBA_CUATRO]
        mazo = []
        for color in colores:
            for valor in range(1, 10):
                mazo.append(Carta(color, Carta.Tipo.NUMERO, valor))
            for tipo in tipos:
                mazo.append(Carta(color, tipo))
        random.shuffle(mazo)
        return mazo

    def robar_carta(self):
        return self.cartas.pop() if self.cartas else None

class Jugador:
    def __init__(self, id):
        self.id = id
        self.mano = []

    def robar_carta(self, mazo):
        carta = mazo.robar_carta()
        if carta:
            self.mano.append(carta)

    def jugar_carta(self, indice, pila_descarte):
        pila_descarte.append(self.mano.pop(indice))

    def ha_ganado(self):
        return len(self.mano) == 0

class Menu:
    @staticmethod
    def mostrar_menu():
        print("Bienvenido a UNO")

    @staticmethod
    def seleccionar_numero_jugadores():
        while True:
            try:
                num = int(input("Ingrese el número de jugadores: "))
                if num > 1:
                    return num
                else:
                    print("El número de jugadores debe ser mayor que 1.")
            except ValueError:
                print("Por favor, ingrese un número válido.")

def inicializar_juego(numero_jugadores):
    global mazo, pila_descarte, jugadores, jugador_actual, direccion_juego
    mazo = Mazo()
    pila_descarte = [mazo.robar_carta()]
    jugadores = [Jugador(i + 1) for i in range(numero_jugadores)]
    for jugador in jugadores:
        for _ in range(7):
            jugador.robar_carta(mazo)
    jugador_actual = 0
    direccion_juego = True

def puede_jugar_carta(carta_elegida, carta_superior):
    return carta_elegida.color == carta_superior.color or \
        carta_elegida.tipo == carta_superior.tipo or \
        carta_elegida.color == Carta.Color.NINGUNO

def ejecutar_efecto_carta(carta):
    global direccion_juego
    if carta.tipo == Carta.Tipo.SALTAR:
        siguiente_jugador()
    elif carta.tipo == Carta.Tipo.REVERSO:
        direccion_juego = not direccion_juego
    elif carta.tipo == Carta.Tipo.ROBA_DOS:
        siguiente_jugador()
        jugadores[jugador_actual].robar_carta(mazo)
        jugadores[jugador_actual].robar_carta(mazo)
    elif carta.tipo in [Carta.Tipo.COMODIN, Carta.Tipo.COMODIN_ROBA_CUATRO]:
        elegir_color(carta)
        if carta.tipo == Carta.Tipo.COMODIN_ROBA_CUATRO:
            siguiente_jugador()
            for _ in range(4):
                jugadores[jugador_actual].robar_carta(mazo)

def elegir_color(carta):
    colores = {1: Carta.Color.ROJO, 2: Carta.Color.AMARILLO, 3: Carta.Color.VERDE, 4: Carta.Color.AZUL}
    while True:
        try:
            eleccion_color = int(input("Elige un color: 1. ROJO 2. AMARILLO 3. VERDE 4. AZUL: "))
            if eleccion_color in colores:
                carta.color = colores[eleccion_color]
                break
            else:
                print("Elección no válida. Inténtalo de nuevo.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

def siguiente_jugador():
    global jugador_actual, direccion_juego
    if direccion_juego:
        jugador_actual = (jugador_actual + 1) % len(jugadores)
    else:
        jugador_actual = (jugador_actual - 1 + len(jugadores)) % len(jugadores)

def main():
    Menu.mostrar_menu()
    numero_jugadores = Menu.seleccionar_numero_jugadores()
    inicializar_juego(numero_jugadores)

    while True:
        jugador = jugadores[jugador_actual]
        print(f"Turno del Jugador {jugador_actual + 1}")
        print("Tus cartas:")
        for i, carta in enumerate(jugador.mano):
            print(f"{i + 1}: {carta}")
        print(f"Carta en la pila: {pila_descarte[-1]}")
        try:
            eleccion = int(input("Elige una carta para jugar o 0 para robar una carta: "))
            if eleccion == 0:
                jugador.robar_carta(mazo)
            elif 1 <= eleccion <= len(jugador.mano):
                carta_elegida = jugador.mano[eleccion - 1]
                carta_superior = pila_descarte[-1]
                if puede_jugar_carta(carta_elegida, carta_superior):
                    jugador.jugar_carta(eleccion - 1, pila_descarte)
                    ejecutar_efecto_carta(carta_elegida)
                    if jugador.ha_ganado():
                        print(f"¡El Jugador {jugador_actual + 1} ha ganado!")
                        break
                else:
                    print("No puedes jugar esa carta.")
            else:
                print("Elección no válida. Inténtalo de nuevo.")
        except ValueError:
            print("Por favor, ingrese un número válido.")
        siguiente_jugador()

if __name__ == "__main__":
    main()
