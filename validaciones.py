

def validar_estado_de_juego(estado_juego):
    """
    Valida que el diccionario del estado del juego contenga las claves necesarias.

    Args:
        estado_juego (dict): Diccionario que representa el estado actual del juego.

    Raises:
        KeyError: Si faltan las claves 'numero_para_adivinar', 'lista_de_intentos' o 'errores'.
    """

    atributos_juego = ["numero_para_adivinar", "lista_de_intentos", "errores"] # Claves  que tiene que tener el Dic

    # Generamos un iter preguntando si cada una de las claves falta, el any da True si falta alguna
    if any(clave not in estado_juego for clave in atributos_juego):
        raise KeyError("El diccionario 'estado_juego' debe contener las claves 'numero_para_adivinar', 'lista_de_intentos' y 'errores'.")