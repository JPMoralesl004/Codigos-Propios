public class NodoDecision {
    String pregunta;
    NodoDecision siNodo;
    NodoDecision noNodo;
    String accion;

    public NodoDecision(String pregunta, String accion) {
        this.pregunta = pregunta;
        this.accion = accion;
        this.siNodo = null;
        this.noNodo = null;
    }

    public void setSiNodo(NodoDecision siNodo) {
        this.siNodo = siNodo;
    }

    public void setNoNodo(NodoDecision noNodo) {
        this.noNodo = noNodo;
    }

    public String getAccion() {
        return accion;
    }

    public void setAccion(String accion) {
        this.accion = accion;
    }
}