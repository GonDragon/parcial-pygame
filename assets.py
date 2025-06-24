import pygame, os

ASSETS_PATH = os.path.join(os.getcwd(), "assets")

IMAGEN = {}
SONIDO = {}

def init():
    error = pygame.mixer.Sound(os.path.join(ASSETS_PATH,"sonidos", "error.wav"))

    SONIDO["error"] = error
