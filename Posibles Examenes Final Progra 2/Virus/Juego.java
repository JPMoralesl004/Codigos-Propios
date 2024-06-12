import java.util.ArrayList;

class Juego {
    private ArrayList<Jugador> jugadores;
    private Baraja baraja;

    public Juego() {
        jugadores = new ArrayList<>();
        baraja = new Baraja();
    }

    public void agregarJugador(Jugador jugador) {
        jugadores.add(jugador);
    }

    public void iniciarJuego() {
        System.out.println("El juego ha comenzado.");
        for (Jugador jugador : jugadores) {
            for (int i = 0; i < 5; i++) {
                jugador.agregarCartaAMano(baraja.robarCarta());
            }
        }
    }

    public void siguienteTurno() {
        for (Jugador jugador : jugadores) {
            System.out.println("Turno de " + jugador.getNombre());
            if (!jugador.getMano().isEmpty()) {
                jugador.jugarCarta(0);
            }
        }
    }

    public Jugador determinarGanador() {
        for (Jugador jugador : jugadores) {
            if (jugador.getOrganosInfectados().isEmpty()) {
                return jugador;
            }
        }
        return null;
    }
}