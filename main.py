import pygame

def main():
    pygame.init()
    ancho, alto = 1280, 720

    screen = pygame.display.set_mode((ancho, alto), pygame.SCALED)
    clock = pygame.time.Clock()
    running = True

    while running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0,0,0))
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()