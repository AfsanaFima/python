import pygame
pygame.init()


screen = pygame.display.set_mode((400,400))
screen.fill((250,230,240))

green = "lavender"
pygame.draw.circle(screen,green,(100,100),50)

pygame.draw.circle(screen,green,(300,300),50,3)
pygame.display.update()

done = False
while not done :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True 