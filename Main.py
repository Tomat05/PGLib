import pygame, Project

if __name__ == '__main__':
    pygame.init()
    Project.setup()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: running = False
        
        Project.update()
        pygame.display.flip()

    pygame.quit()