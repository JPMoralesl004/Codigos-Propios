public class JuegoVirus {
    public static void main(String[] args) {
        Juego juego = new Juego();
        Jugador jugador1 = new Jugador("Alice");
        Jugador jugador2 = new Jugador("Bob");

        juego.agregarJugador(jugador1);
        juego.agregarJugador(jugador2);
        juego.iniciarJuego();

        for (int i = 0; i < 5; i++) {
            juego.siguienteTurno();
        }

        Jugador ganador = juego.determinarGanador();
        if (ganador != null) {
            System.out.println("El ganador es: " + ganador.getNombre());
        } else {
            System.out.println("El juego ha terminado en empate.");
        }
    }
}