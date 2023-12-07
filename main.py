import pygame

pygame.init()

screen = pygame.display.set_mode((1024, 720))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    
    screen.fill((0,0,0))
    pygame.display.update()