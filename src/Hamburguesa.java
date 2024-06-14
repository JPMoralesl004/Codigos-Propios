package restaurante;

public class Hamburguesa {
    private Pan panSuperior;
    private Pan panInferior;
    private Carne carne;
    private Extras[] extras;

    public Hamburguesa(Pan panSuperior, Pan panInferior, Carne carne, int numExtras) {
        this.panSuperior = panSuperior;
        this.panInferior = panInferior;
        this.carne = carne;
        this.extras = new Extras[numExtras];
    }

    public void agregarExtra(Extras extra) {
        for (int i = 0; i < extras.length; i++) {
            if (extras[i] == null) {
                extras[i] = extra;
                break;
            }
        }
    }

    public String descripcion() {
        StringBuilder descripcion = new StringBuilder();
        descripcion.append(panSuperior.getDescripcion()).append("\n");
        descripcion.append(carne.getDescripcion()).append("\n");
        for (Extras extra : extras) {
            if (extra != null) {
                descripcion.append(extra.getDescripcion()).append("\n");
            }
        }
        descripcion.append(panInferior.getDescripcion()).append("\n");
        return descripcion.toString();
    }
}