class Cancion:
    def __init__(self, titulo, duracion):
        self.titulo = titulo
        self.duracion = duracion
        self.siguiente = None

    def __str__(self):
        return f"{self.titulo} ({self.duracion})"

class Playlist:
    def __init__(self, nombre, artista):
        self.nombre = nombre
        self.artista = artista
        self.canciones = None

    def agregar_cancion(self, titulo, duracion):
        nueva_cancion = Cancion(titulo, duracion)
        if not self.canciones:
            self.canciones = nueva_cancion
        else:
            actual = self.canciones
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nueva_cancion

    def mostrar_canciones(self):
        actual = self.canciones
        if not actual:
            print("La playlist está vacía.")
        while actual:
            print(actual)
            actual = actual.siguiente

    def __str__(self):
        return f"{self.nombre} - {self.artista}"

class SistemaReproduccionMusica:
    def __init__(self):
        self.playlists = []

    def agregar_playlist(self, playlist):
        self.playlists.append(playlist)

    def mostrar_playlists(self):
        if not self.playlists:
            print("No hay playlists disponibles.")
            return
        print("Playlists disponibles:")
        for i, playlist in enumerate(self.playlists):
            print(f"{i + 1}. {playlist}")

    def iniciar(self):
        while True:
            print("\nOpciones del sistema de reproducción:")
            print("1. Mostrar playlists")
            print("2. Salir")

            seleccion = input("Elige una opción: ")

            if seleccion == "1":
                self.mostrar_playlists()
            elif seleccion == "2":
                print("Saliendo del sistema de reproducción...")
                break
            else:
                print("Opción inválida. Por favor, elige una opción válida.")

sistema = SistemaReproduccionMusica()

playlist_predeterminada.agregar_cancion("Caraluna - Bacilos", "4:26")
playlist_predeterminada.agregar_cancion("STAY (with Justin Bieber) - The Kid LAROI, Justin Bieber", "2:22")
playlist_predeterminada.agregar_cancion("It's My Life - Bon Jovi", "3:44")
playlist_predeterminada.agregar_cancion("Karma Chameleon - Culture Club", "4:12")
playlist_predeterminada.agregar_cancion("Nunca es Suficiente - Los Angeles Azules, Natalia Lafourcade", "4:26")
playlist_predeterminada.agregar_cancion("Carry on Wayward Son - Kansas", "5:23")
playlist_predeterminada.agregar_cancion("Somebody To Love - Queen", "4:56")
playlist_predeterminada.agregar_cancion("Bam Bam (feat. Ed Sheeran) - Camila Cabello, Ed Sheeran", "3:26")
playlist_predeterminada.agregar_cancion("THAT'S WHAT I WANT - Lil Nas X", "2:24")
playlist_predeterminada.agregar_cancion("Yo Viviré - Celia Cruz", "4:31")
playlist_predeterminada.agregar_cancion("Jump - Van Halen", "4:02")
playlist_predeterminada.agregar_cancion("Nothing's Gonna Stop Us Now - Starship", "4:30")
playlist_predeterminada.agregar_cancion("Livin' On a Prayer - Bon Jovi", "4:09")
playlist_predeterminada.agregar_cancion("Under The Influence - Chris Brown", "3:05")
playlist_predeterminada.agregar_cancion("Flowers - Miley Cyrus", "3:20")
playlist_predeterminada.agregar_cancion("CUFF IT - Beyoncé", "3:45")
playlist_predeterminada.agregar_cancion("I Ain't Worried - OneRepublic", "2:28")
playlist_predeterminada.agregar_cancion("Live Is Life - Opus", "4:15")
playlist_predeterminada.agregar_cancion("Another Love - Tom Odell", "4:04")
playlist_predeterminada.agregar_cancion("Venite Volando - Los Iracundos", "2:36")
playlist_predeterminada.agregar_cancion("Just Us - James Arthur", "3:35")
playlist_predeterminada.agregar_cancion("Rasputin - Boney M.", "3:41")
playlist_predeterminada.agregar_cancion("Born In The U.S.A - Bruce Springsteen", "4:39")
playlist_predeterminada.agregar_cancion("Eye Of The Tiger - Survivor", "4:04")
playlist_predeterminada.agregar_cancion("Thank You For The Music - ABBA", "3:49")

sistema.agregar_playlist(playlist_predeterminada)

sistema.iniciar()
