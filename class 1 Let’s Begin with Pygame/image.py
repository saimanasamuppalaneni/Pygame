import pygame
pygame.init()

screen  = pygame.display.set_mode((400,500))
done = False

bg_surf = pygame.transform.scale(pygame.image.load("bg.jpg").convert(),(400,500))
img_surf = pygame.transform.scale(pygame.image.load("fl.jpg").convert(),(200,200))
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    screen.blit(bg_surf,(0,0))
    screen.blit(img_surf,(100,100))
    pygame.display.flip()

