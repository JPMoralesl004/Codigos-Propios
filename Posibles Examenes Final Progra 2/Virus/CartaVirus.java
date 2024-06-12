class CartaVirus extends Carta {
    public CartaVirus(String nombre) {
        super(nombre, "Virus");
    }

    @Override
    public void jugar(Jugador jugador) {
        System.out.println("Carta Virus jugada: " + getNombre());
        jugador.infectarOrganos();
    }
}