class CartaOrgano extends Carta {
    public CartaOrgano(String nombre) {
        super(nombre, "Organo");
    }

    @Override
    public void jugar(Jugador jugador) {
        System.out.println("Carta Órgano jugada: " + getNombre());
        jugador.agregarOrgano(getNombre());
    }
}
