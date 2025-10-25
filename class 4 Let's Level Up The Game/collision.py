import pygame
color = 'black'
surface_color = 'red'
MOVEMENT_SPEED = 3
pygame.init()
font = pygame.font.Font('freesansbold.ttf',40)
class mysprite(pygame.sprite.Sprite):
    def __init__(self,color,height,width):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(surface_color)
        pygame.draw.rect(self.image,color,pygame.Rect(0,0,width,height))
        self.rect = self.image.get_rect()
    def move(self,x_change,y_change):
        self.rect.x = max(min(self.rect.x + x_change,500 - self.rect.width),0)
        self.rect.y = max(min(self.rect.y + y_change,400 - self.rect.height),0)

screen  = pygame.display.set_mode((500,400))
pygame.display.set_caption("Collision Detection")

asl = pygame.sprite.Group()
sp1 = mysprite(color,20,30)
sp1.rect.x = 80
sp1.rect.y = 150
color = 'cyan'
sp2 = mysprite(color,20,30)
sp2.rect.x = 80
sp2.rect.y = 50

asl.add(sp1,sp2)

clock = pygame.time.Clock()
exit = True
while exit:
    for event in pygame.event.get():
        if event.type ==   pygame.QUIT:
            exit = False

    keys = pygame.key.get_pressed()
    x_change = (keys[pygame.K_RIGHT - keys[pygame.K_LEFT]]) * MOVEMENT_SPEED
    y_change = (keys[pygame.K_DOWN - keys[pygame.K_UP]]) * MOVEMENT_SPEED
    sp2.move(x_change,y_change)
    screen.fill(surface_color)
    asl.draw(screen)
    if sp2.rect.colliderect(sp1.rect):
        asl.remove(sp1)
        asl.remove(sp2)
        win_text = font.render("YOU WIN!!",True,'green')
        screen.blit(win_text,(100,100))
        

    pygame.display.flip()
    clock.tick(90)

pygame.quit()