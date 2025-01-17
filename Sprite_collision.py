import pygame
import random


screen_width,screen_height =500,400

movement_speed = 5
font_size = 60

pygame.init()
background_image = pygame.image.load("bg.jpg")

font = pygame.font.SysFont("times new roman",font_size)

class sprite(pygame.sprite.Sprite):
    def __init__(self,color,height,width):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        pygame.draw.rect(self.image,color,pygame.rect.Rect(0,0,width,height))
        self.rect = self.image.get_rect()

    def move(self,x_change,y_change):
        
        self.rect.x = max(0,min(self.rect.x + x_change,screen_width - self.rect.width))
        self.rect.y = max(0,min(self.rect.y + y_change,screen_height - self.rect.height))

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Sprite collision")

sprite1 = sprite(pygame.Color('black'),30,20)
sprite1.rect.x,sprite1.rect.y = 180,100
all_sprites = pygame.sprite.Group(sprite1)

sprite2 = sprite(pygame.Color('pink'),30,20)
sprite2.rect.x,sprite2.rect.y = 180,100
all_sprites = pygame.sprite.Group(sprite2)

running,won = True,False
clock = pygame.time.Clock()

while running :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            

    if not won:
        keys = pygame.key.get_pressed()
        x_change = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]* movement_speed)
        y_change = (keys[pygame.K_DOWN] - keys[pygame.K_UP]* movement_speed)
        sprite1.move(x_change,y_change)


        if sprite1.rect.colliderect(sprite2.rect):
            all_sprites.remove(sprite2)
            won = True


    screen.blit(background_image,(0,0))
    all_sprites.draw(screen)

    if won:
        win_text = font.render("Youuu wonnn !!!!",True,pygame.Color('purple'))


pygame.display.flip()
clock.tick(50)




