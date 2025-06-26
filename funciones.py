# from colores_y_fuentes import FUENTE, BLANCO
# from configuracion_basica import SCREEN 
import random

# def mostrar_texto(texto, x, y, color=BLANCO):
#     """
#     Propósito: mostrar texto en la pantalla.
#     """
#     render = FUENTE.render(texto, True, color)
#     SCREEN.blit(render, (x, y))


def dibujar_cruces(errores):
    """"""



def nuevo_juego():
    """
    Propósito: retorna un número aleatorio, una lista de intentos vacía y un contador de errores en 0.
    """
    nuevo_juego = {
        "numero_para_adivinar" : random.randint(1,9),
        "lista_de_intentos" : [],
        "errores" : 0}
    return nuevo_juego # retorno el dicionario.
    

# print(nuevo_juego())


# numero, lista, errores = nuevo_juego()

# print(numero)
# print(lista)
# print(errores)

def procesar_tecla(tecla, numero_secreto, intentos, errores):
    """"""


def jugar():
    """"""

