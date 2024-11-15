class SistemaReproduccionMusica:
    def __init__(self):
        self.playlists = []
        self.inicializar_playlist_predeterminada()

    def inicializar_playlist_predeterminada(self):
        """Crea una playlist predeterminada con canciones iniciales."""
        playlist_predeterminada = Playlist("Favoritas", "Varios Artistas")
        
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
        
        self.agregar_playlist(playlist_predeterminada)

    def agregar_playlist(self, playlist):
        """Agrega una playlist a la lista del sistema."""
        self.playlists.append(playlist)

    def mostrar_playlists(self):
        """Muestra todas las playlists disponibles en el sistema."""
        if not self.playlists:
            print("No hay playlists disponibles.")
        else:
            print("\nPlaylists disponibles:")
            for i, playlist in enumerate(self.playlists, 1):
                print(f"{i}. {playlist.nombre}")

    def seleccionar_playlist(self):
        """Permite al usuario seleccionar una playlist por número."""
        self.mostrar_playlists()
        if not self.playlists:
            return None
        try:
            seleccion = int(input("\nSelecciona una playlist por número: ")) - 1
            if 0 <= seleccion < len(self.playlists):
                return self.playlists[seleccion]
            else:
                print("Número inválido.")
        except ValueError:
            print("Entrada inválida.")
        return None

    def ver_cancion_actual(self):
        """Muestra la canción que se está reproduciendo actualmente."""
        print("Mostrando la canción actual...")

    def reproducir_siguiente_cancion(self):
        """Reproduce la siguiente canción en la playlist actual."""
        print("Reproduciendo la siguiente canción...")

    def ver_cola_reproduccion(self):
        """Muestra la cola de canciones en reproducción."""
        print("Mostrando la cola de reproducción...")

    def ver_favoritos(self):
        """Muestra las canciones marcadas como favoritas."""
        print("Mostrando canciones favoritas...")

    def crear_playlist(self):
        """Permite crear una nueva playlist."""
        nombre = input("Ingresa el nombre de la nueva playlist: ")
        artista = input("Ingresa el nombre del artista o descripción: ")
        nueva_playlist = Playlist(nombre, artista)
        self.agregar_playlist(nueva_playlist)
        print(f"Playlist '{nombre}' creada.")

    def eliminar_playlist(self):
        """Elimina una playlist seleccionada."""
        playlist = self.seleccionar_playlist()
        if playlist:
            self.playlists.remove(playlist)
            print(f"Playlist '{playlist.nombre}' eliminada.")

    def buscar_cancion(self):
        """Permite buscar una canción en todas las playlists."""
        termino = input("Ingresa el nombre de la canción a buscar: ")
        for playlist in self.playlists:
            if playlist.buscar_cancion(termino):
                print(f"Canción '{termino}' encontrada en la playlist '{playlist.nombre}'.")
                return
        print("Canción no encontrada.")

    def agregar_cancion_playlist(self):
        """Agrega una canción a una playlist seleccionada."""
        playlist = self.seleccionar_playlist()
        if playlist:
            nombre_cancion = input("Ingresa el nombre de la canción: ")
            duracion = input("Ingresa la duración de la canción (minutos:segundos): ")
            playlist.agregar_cancion(nombre_cancion, duracion)
            print(f"Canción '{nombre_cancion}' agregada a la playlist '{playlist.nombre}'.")

    def iniciar(self):
        """Inicia el sistema con un menú interactivo."""
        while True:
            print("\nOpciones del sistema de reproducción:")
            print("1. Mostrar playlists")
            print("2. Ver canción actual")
            print("3. Reproducir siguiente canción")
            print("4. Ver cola de reproducción")
            print("5. Ver favoritos")
            print("6. Crear nueva playlist")
            print("7. Eliminar una playlist")
            print("8. Buscar una canción")
            print("9. Agregar canción a una playlist")
            print("10. Salir")

            seleccion = input("Elige una opción: ")

            if seleccion == "1":
                self.mostrar_playlists()
            elif seleccion == "2":
                self.ver_cancion_actual()
            elif seleccion == "3":
                self.reproducir_siguiente_cancion()
            elif seleccion == "4":
                self.ver_cola_reproduccion()
            elif seleccion == "5":
                self.ver_favoritos()
            elif seleccion == "6":
                self.crear_playlist()
            elif seleccion == "7":
                self.eliminar_playlist()
            elif seleccion == "8":
                self.buscar_cancion()
            elif seleccion == "9":
                self.agregar_cancion_playlist()
            elif seleccion == "10":
                print("Saliendo del sistema de reproducción...")
                break
            else:
                print("Opción inválida. Por favor, elige una opción válida.")

class Playlist:
    def __init__(self, nombre, artista):
        self.nombre = nombre
        self.artista = artista
        self.canciones = []

    def agregar_cancion(self, nombre_cancion, duracion):
        self.canciones.append((nombre_cancion, duracion))

    def mostrar_canciones(self):
        if not self.canciones:
            print(f"La playlist '{self.nombre}' no tiene canciones.")
        else:
            print(f"Canciones en '{self.nombre}':")
            for nombre_cancion, duracion in self.canciones:
                print(f"{nombre_cancion} - {duracion}")

    def buscar_cancion(self, termino):
        for nombre_cancion, _ in self.canciones:
            if termino.lower() in nombre_cancion.lower():
                return True
        return False

sistema = SistemaReproduccionMusica()
sistema.iniciar()
