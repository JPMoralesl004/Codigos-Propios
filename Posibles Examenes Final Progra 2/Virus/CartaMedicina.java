class CartaMedicina extends Carta {
    public CartaMedicina(String nombre) {
        super(nombre, "Medicina");
    }

    @Override
    public void jugar(Jugador jugador) {
        System.out.println("Carta Medicina jugada: " + getNombre());
        jugador.curarOrganos();
    }
}