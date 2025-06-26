import pygame
import pygame.mixer as mixer # importo pygame.mixer como mixer para poder usar sonidos más adelante.
from texto import mostrar_texto
import personaje

pygame.init() # Inicializando pygame
ancho, alto = 800, 600 # declarando el ancho y el alto que tenda la pantalla.



screen = pygame.display.set_mode((ancho, alto), pygame.SCALED) # Se crea la pantalla y se la asigna a screen. A esta se le pasan los valores de alto y ancho que definimos anteriormente. También se usa pygame.SCALED.
clock = pygame.time.Clock() # 

# se crea el pj y el obstáculo
pj = personaje.crear_personaje(ancho, alto)
obstaculo = pygame.Rect(200, 550, 100, 50)

def jugar():
  
    jugando = True # Se inicializa la varianble jugando con True para que inicie el juego.

    while jugando: # Se crea el bucle principal del juego.
        events = pygame.event.get() # Se obtienen todos los eventos que ocurren con .get() y se guardan en events.
        for event in events: # Para cada event en events se verifica lo siguiente.
            if event.type == pygame.QUIT: # Si el tipo del evento actual es igual a pygame.QUIT entonces
                jugando = False # Se le asigna False a la variable running

        # Actualizar el juego (por ahora nada)
        teclas = pygame.key.get_pressed() # Se obtienen las teclas presionadas y se guardan en teclas.
        personaje.mover_personaje(pj, teclas, ancho) 

        screen.fill((30,30,30)) # Se dibuja en la pantalla rellenandola de negro.
        personaje.dibujar_personaje(screen, pj) #se dibuja el pj
        pygame.draw.rect(screen, (255, 0, 0), obstaculo)  # Dibuja el obstáculo en rojo

        screen.blit(mostrar_texto(), (50, 50)) # Coloco el texto que indica la cantidad de fallos en las cordanas dadas.

        #colision con objeto
        personaje.colision_con_obstaculo(pj, obstaculo)

        pygame.display.flip() # flip() actualiza el contenido de toda la pantalla.
        clock.tick(30) # Limita los fps a 30.



jugar()