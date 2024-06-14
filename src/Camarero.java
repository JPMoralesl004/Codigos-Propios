class Camarero extends Empleado {

    public void recibir(Hamburguesa hamburguesa) {
        this.hamburguesa = hamburguesa;
        this.tieneHamburguesa = true;
    }

    public void servir() {
        if (tieneHamburguesa) {
            System.out.println("Sirviendo la hamburguesa:");
            System.out.println(hamburguesa.descripcion());
            this.tieneHamburguesa = false;
        } else {
            System.out.println("No hay hamburguesa para servir.");
        }
    }
}