import pygame

WIDTH, HEIGHT = 1200, 800
FPS = 60

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame. time.Clock()
    running = True
    
    while running:
        # 1. Inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # 2. Physik / Update
        
        # 3. Rendering
        screen.fill((30, 30, 30))
        pygame.display.flip()
        
        clock.tick(FPS)
        
    pygame.quit()

if __name__ == "__main__":
    main()