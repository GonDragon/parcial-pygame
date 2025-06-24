import pygame
import pygame.mixer as mixer # importo pygame.mixer como mixer para poder usar sonidos más adelante.

def main():
    pygame.init() # Inicializando pygame
    ancho, alto = 800, 600 # declarando el ancho y el alto que tenda la pantalla.


    screen = pygame.display.set_mode((ancho, alto), pygame.SCALED) # Se crea la pantalla y se la asigna a screen. A esta se le pasan los valores de alto y ancho que definimos anteriormente. También se usa pygame.SCALED.
    clock = pygame.time.Clock() # 
    running = True # Se inicializa la varianble running con True para que inicie el juego.

    while running: # Se crea el bucle principal del juego.
        events = pygame.event.get() # Se obtienen todos los eventos que ocurren con .get() y se guardan en events.
        for event in events: # Para cada event en events se verifica lo siguiente.
            if event.type == pygame.QUIT: # Si el tipo del evento actual es igual a pygame.QUIT entonces
                running = False # Se le asigna False a la variable running

        # Actualizar el juego (por ahora nada)

        screen.fill((0,0,0)) # Se dibuja en la pantalla rellenandola de negro.
        pygame.display.flip() # flip() actualiza el contenido de toda la pantalla.
        clock.tick(30) # Limita los fps a 30.

if __name__ == "__main__":
    main()