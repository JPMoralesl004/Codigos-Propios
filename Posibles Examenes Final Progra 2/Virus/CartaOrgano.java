class CartaOrgano extends Carta {
    public CartaOrgano(String nombre, String color) {
        super(nombre, "Organo", color);
    }

    @Override
    public void jugar(Jugador jugador) {
        System.out.println("Carta Órgano jugada: " + getNombre() + " de color " + getColor());
        jugador.agregarOrgano(getNombre());
    }
}
