import pygame
pygame.init()
screen  = pygame.display.set_mode((640,540))
done = False

while not done:
    screen.fill((255,165,120))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            y = y -5
        if pressed[pygame.K_DOWN]:
            y = y + 5
        if pressed[pygame.K_LEFT]:
            x = x -5
        if pressed[pygame.K_RIGHT]:
            x = x + 5
    pygame.draw.rect(screen,'white',(x,y,20,20))
    pygame.draw.rect(screen,"cyan",(x,y,50,50))
    pygame.display.flip()
