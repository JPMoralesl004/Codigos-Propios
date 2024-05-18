public class ArbolDecision {
    NodoDecision raiz;

    public ArbolDecision() {
        this.raiz = null;
    }

    public void insertar(String pregunta, String respuestaSi, String respuestaNo) {
        raiz = insertarRecursivo(raiz, pregunta, respuestaSi, respuestaNo);
    }

    private NodoDecision insertarRecursivo(NodoDecision actual, String pregunta, String respuestaSi, String respuestaNo) {
        if (actual == null) {
            return new NodoDecision(pregunta, null);
        }

        if (respuestaSi != null) {
            actual.setSiNodo(insertarRecursivo(actual.siNodo, pregunta, respuestaSi, null));
        } else if (respuestaNo != null) {
            actual.setNoNodo(insertarRecursivo(actual.noNodo, pregunta, respuestaNo, null));
        }

        return actual;
    }

    public void iniciarArbol() {
        insertar("¿El paciente tiene síntomas de COVID-19?", "Sí", "No");
        insertar("¿El paciente ha estado en contacto con alguien diagnosticado con COVID-19?", "Sí", "No");
    }

    public void tomarDecision(NodoDecision nodo) {
        if (nodo != null) {
            System.out.println(nodo.pregunta);
        }
    }

    public void casoAsintomaticoPositivo() {
        NodoDecision nodoAsintomatico = new NodoDecision(
            "¿La persona ha dado positivo por COVID-19 y no tiene síntomas?",
            "Aíslese en casa y use máscara hasta el día 10 desde el día del resultado de la prueba negativa."
        );
        raiz.setSiNodo(nodoAsintomatico);
    }

    public void expandirArbolConNuevoFlujo() {
        NodoDecision nodoVacunado = new NodoDecision("¿Está la persona vacunada?", "Continuar trabajando con precauciones");
        NodoDecision nodoNoVacunado = new NodoDecision("¿Está la persona no vacunada?", "Quedarse en casa y cuarentena");
        NodoDecision nodoSintomas = new NodoDecision("¿Tiene síntomas?", "Buscar atención médica y hacerse la prueba");
        nodoVacunado.setSiNodo(nodoSintomas);
        nodoNoVacunado.setNoNodo(nodoSintomas);
        raiz.setSiNodo(nodoVacunado);
        raiz.setNoNodo(nodoNoVacunado);
    }

    public void agregarNotasCuarentenaAislamiento() {
        NodoDecision nodoNota1 = new NodoDecision("Nota 1", "Acción para nota 1");
        NodoDecision nodoNota2 = new NodoDecision("Nota 2", "Acción para nota 2");
        raiz.setSiNodo(nodoNota1);
        raiz.setNoNodo(nodoNota2);
    }

    public void agregarRecomendacionesPruebasCuarentena() {
        NodoDecision nodoPruebaAntigeno = new NodoDecision("¿Se ha realizado una prueba de antígeno?", "Seguir las recomendaciones basadas en el resultado");
        NodoDecision nodoPruebaPCR = new NodoDecision("¿Se ha realizado una prueba PCR?", "Seguir las recomendaciones basadas en el resultado");
        NodoDecision nodoPruebaHogar = new NodoDecision("¿Se ha realizado una prueba en el hogar?", "Usar la Guía de Pruebas Gratuitas para interpretar el resultado");
        nodoPruebaAntigeno.setSiNodo(nodoPruebaPCR);
        nodoPruebaAntigeno.setNoNodo(nodoPruebaHogar);
        raiz.setSiNodo(nodoPruebaAntigeno);
    }
}