import pygame
import random

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        cols = 20
        rows = 16
        mole_image = pygame.image.load("mole.png")
        molposx = 0
        molposy = 0
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mole_rect = mole_image.get_rect(topleft=(molposx, molposy))
                    if mole_rect.collidepoint(event.pos):
                        molposx = random.randrange(cols) * 32
                        molposy = random.randrange(rows) * 32

            screen.fill("light green")
            for i in range(cols):
                pygame.draw.line(screen, 'black', (i * 32, 0), (i * 32, 512))
            for i in range(rows):
                pygame.draw.line(screen, 'black', (0, i * 32), (640, i * 32))
            screen.blit(mole_image, (molposx, molposy))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
