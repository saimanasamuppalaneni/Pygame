import pygame
pygame.init()

pygame.display.set_caption("My First Game Screen")
screen  = pygame.display.set_mode((640,480))
screen.fill("white")
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.draw.rect(screen,"pink",pygame.rect.Rect((100,160),(40,50)))
    
    pygame.display.flip()