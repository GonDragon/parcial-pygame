from colores_y_fuentes import FUENTE, BLANCO

def mostrar_texto():
    """
    Propósito: mostrar texto en la pantalla.
    """
    texto = FUENTE.render("Cantidad de fallos: ", True, BLANCO)
    return texto