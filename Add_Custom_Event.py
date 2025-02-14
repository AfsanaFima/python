import pygame
import random


pygame.init()


screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))


pygame.display.set_caption("Sprite Addition and Custom Event")


CHANGE_COLOR_EVENT = pygame.USEREVENT + 1


class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))  
        self.color = color
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def change_color(self):
        
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.image.fill(self.color)


sprite1 = Sprite((255, 0, 0), 200, 300)   
sprite2 = Sprite((0, 255, 0), 600, 300)  

all_sprites = pygame.sprite.Group()
all_sprites.add(sprite1, sprite2)


clock = pygame.time.Clock()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == CHANGE_COLOR_EVENT:
            sprite1.change_color()
            sprite2.change_color()

    
    screen.fill((255, 255, 255))

    
    all_sprites.draw(screen)

    
    pygame.display.flip()

    
    pygame.time.wait(2000)   
    pygame.event.post(pygame.event.Event(CHANGE_COLOR_EVENT))

    
    clock.tick(60)


pygame.quit()
