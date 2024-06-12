class CartaTratamiento extends Carta {
    public CartaTratamiento(String nombre) {
        super(nombre, "Tratamiento");
    }

    @Override
    public void jugar(Jugador jugador) {
        System.out.println("Carta Tratamiento jugada: " + getNombre());
        jugador.aplicarTratamiento(getNombre());
    }
}