from colores_y_fuentes import FUENTE, BLANCO
from configuracion_basica import SCREEN 

def mostrar_texto(texto, x, y, color=BLANCO):
    """
    Propósito: mostrar texto en la pantalla.
    """
    render = FUENTE.render(texto, True, color)
    SCREEN.blit(render, (x, y))


def dibujar_cruces(errores):
    """"""



def nuevo_juego():
    """"""



def procesar_tecla(tecla, numero_secreto, intentos, errores):
    """"""


def jugar():
    """"""


