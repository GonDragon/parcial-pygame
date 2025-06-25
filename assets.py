import pygame, os

ASSETS_PATH = os.path.join(os.getcwd(), "assets")

IMAGEN = {}
SONIDO = {}

def init():
    SONIDO["error"] = pygame.mixer.Sound(os.path.join(ASSETS_PATH,"sonidos", "error.wav")) # Cargo Sonido y lo guardo en el Dic

    personaje = pygame.image.load(os.path.join(ASSETS_PATH, "img", "dvd-logo.png")) # Cargar imagen de personaje
    altura_maxima = 100 # Definir una altura máximo
    ancho, alto = personaje.get_size() # Capturo el tamaño de la imagen
    
    if alto > altura_maxima: # Si es mas alta que la maxima definida, achicar la imagen
        factor_escalado = altura_maxima / alto # Factor de escalado para mantener el ratio de la imagen
        new_size = (int(ancho * factor_escalado), altura_maxima) # Nuevo tamaño de la imagen
        personaje = pygame.transform.scale(personaje, new_size) # Escalo la imagen para que tenga el nuevo tamaño

    IMAGEN["personaje"] = personaje # Guardo el personaje en el Dic
