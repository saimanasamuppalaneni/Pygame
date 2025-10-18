import pygame
pygame.init()

screen  = pygame.display.set_mode((400,500))
pygame.draw.circle(screen,'green',(100,160),40)
pygame.draw.circle(screen,'tomato',(300,160),50,3)


done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    pygame.display.flip()