import random

class Personaje:
    def __init__(self, nombre, caracteristicas):
        self.nombre = nombre
        self.caracteristicas = caracteristicas

class JuegoQuienEsQuien:
    def __init__(self, personajes):
        self.personajes = personajes
        self.personaje_secreto = random.choice(self.personajes)
        self.caracteristicas_disponibles = self.obtener_caracteristicas_disponibles()

    def obtener_caracteristicas_disponibles(self):
        todas_caracteristicas = set()
        for personaje in self.personajes:
            todas_caracteristicas.update(personaje.caracteristicas)
        return todas_caracteristicas

    def hacer_pregunta(self, pregunta):
        personajes_con_caracteristica = []
        for personaje in self.personajes:
            if pregunta in personaje.caracteristicas:
                personajes_con_caracteristica.append(personaje.nombre)

        print(f"Personajes que tienen '{pregunta}': {', '.join(personajes_con_caracteristica)}")

        if len(personajes_con_caracteristica) == 1:
            print(f"El personaje secreto tiene la característica '{pregunta}'.")
        elif len(personajes_con_caracteristica) == len(self.personajes):
            print(f"Ningún personaje tiene la característica '{pregunta}'.")
        else:
            self.caracteristicas_disponibles.remove(pregunta)

    def adivinar_personaje(self):
        adivinanza = input("¿Quién crees que es el personaje secreto?: ")
        if adivinanza.lower() == self.personaje_secreto.nombre.lower():
            print("¡Correcto! Has adivinado el personaje secreto.")
        else:
            print(f"No, el personaje secreto no es {adivinanza}.")

personajes = [
    Personaje("Mario", ["bigote", "gorra", "trabajador"]),
    Personaje("Luigi", ["bigote", "sombrero verde", "trabajador"]),
    Personaje("Peach", ["vestido rosa", "corona", "princesa"]),
    Personaje("Bowser", ["caparazón", "colmillos", "villano"]),
    Personaje("Yoshi", ["dinosaurio", "huevo", "amigo"]),
]

juego = JuegoQuienEsQuien(personajes)

while True:
    print("\nCaracterísticas disponibles:", ", ".join(juego.caracteristicas_disponibles))
    pregunta = input("Haz una pregunta sobre el personaje secreto (o 'fin' para adivinar): ")
    if pregunta.lower() == 'fin':
        juego.adivinar_personaje()
        break
    elif pregunta in juego.caracteristicas_disponibles:
        juego.hacer_pregunta(pregunta)
    else:
        print("Característica inválida o ya preguntada. Por favor, elige otra.")