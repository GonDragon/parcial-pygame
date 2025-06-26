import pygame
import assets
# Diccionario del personaje
pygame.mixer.init()  # Inicializa el mezclador de sonido
PERSONAJE = {
    "velocidad": 10,
    "ancho": 50,
    "alto": 50,
    "imagen": assets.IMAGEN("personaje")  # Cargar imagen del personaje desde el diccionario de imágenes
}

PERSONAJE["imagen"] = pygame.transform.scale(PERSONAJE["imagen"], (PERSONAJE["ancho"], PERSONAJE["alto"]))
sonido_daño = assets.SONIDO("daño")  # Cargar sonido de daño desde el diccionario de sonidos

def crear_personaje(ancho_ventana, alto_ventana): # Crea un rectángulo que representa al personaje en la parte inferior de la ventana
    x = (ancho_ventana - PERSONAJE["ancho"]) // 2  # Posición inicial en el centro de la pantalla
    y = (alto_ventana - PERSONAJE["alto"]) # Posición inicial en la parte inferior de la pantalla
    ubicacion = pygame.Rect(x, y, PERSONAJE["ancho"], PERSONAJE["alto"])
    return ubicacion  # Devuelve el rectángulo que representa al personaje

def dibujar_personaje(ventana, personaje): # Dibuja el personaje en la ventana
    if PERSONAJE["imagen"]: # Verifica si la imagen del personaje está cargada
        ventana.blit(PERSONAJE["imagen"], personaje.topleft) # Dibuja la imagen del personaje en la ventana

def mover_personaje(personaje, teclas, ancho_ventana): # Mueve el personaje según las teclas presionadas

    if teclas[pygame.K_LEFT] and personaje.left > 0: # Verifica si se presiona la tecla izquierda y si el personaje no está en el borde del lado izquierdo
        personaje.x -= PERSONAJE["velocidad"] # Mueve el personaje a la izquierda
    if teclas[pygame.K_RIGHT] and personaje.right < ancho_ventana: # Verifica si se presiona la tecla derecha y si el personaje no está en el borde del lado derecho
        personaje.x += PERSONAJE["velocidad"] # Mueve el personaje a la derecha

def colision_con_obstaculo(personaje, obstaculo): # Verifica si el personaje colisiona con un obstáculo
    if personaje.colliderect(obstaculo):
        sonido_daño.play()  # Reproduce el sonido de daño