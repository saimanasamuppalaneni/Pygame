import pygame
import random
pygame.init()

width = 500
height = 400
screen_res = (width,height)
colors = ['red','yellow','pink','purple','black','blue','green']
bg_colors = ['red','yellow','pink','purple','black','blue','green']
clr = random.choice(colors)

screen  = pygame.display.set_mode(screen_res)
x = 100
y = 100
bg_color = 'black'

rect_obj1 = pygame.draw.rect(screen,'black',pygame.Rect(x,y,40,40))
rect_obj2 = pygame.draw.rect(screen,'black',pygame.Rect(x,y,50,60))


speed = [1,-1]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    screen.fill(bg_color)

    rect_obj1 = rect_obj1.move(speed)
    rect_obj2 = rect_obj2.move(speed)
    

    if rect_obj1.left <= 0 or rect_obj1.right >= width:
        speed[0] = -speed[0]
        clr = random.choice(colors)
        bg_color = random.choice(bg_colors)

    if rect_obj2.left <= 0 or rect_obj2.right >= width:
        speed[0] = -speed[0]
        clr = random.choice(colors)
        bg_color = random.choice(bg_colors)

    if rect_obj1.top <= 0 or rect_obj1.bottom >= height:
        speed[1] = -speed[1]
        clr = random.choice(colors)
        bg_color = random.choice(bg_colors)

    if rect_obj2.top <= 0 or rect_obj2.bottom >= height:
        speed[1] = -speed[1]
        clr = random.choice(colors)
        bg_color = random.choice(bg_colors)


    rect_obj1 = pygame.draw.rect(screen,clr,pygame.Rect(rect_obj1.x,rect_obj1.y,40,40))
    rect_obj2 = pygame.draw.rect(screen,clr,pygame.Rect(rect_obj2.x,rect_obj2.y,40,40))

    
    pygame.display.flip()