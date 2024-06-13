class CartaTratamiento extends Carta {
    public CartaTratamiento(String nombre, String color) {
        super(nombre, "Tratamiento", color);
    }

    @Override
    public void jugar(Jugador jugador) {
        System.out.println("Carta Tratamiento jugada: " + getNombre() + " de color " + getColor());
        jugador.aplicarTratamiento(getNombre());
    }
}
