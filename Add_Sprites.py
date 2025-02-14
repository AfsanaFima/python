import pygame


pygame.init()


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sprite Movement")


WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


class RectangleSprite(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))  
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def move(self, dx=0, dy=0):
        self.rect.x += dx
        self.rect.y += dy


player = RectangleSprite(RED, 100, 100)  
static_sprite = RectangleSprite(BLUE, 500, 300)  


all_sprites = pygame.sprite.Group()
all_sprites.add(player, static_sprite)


clock = pygame.time.Clock()
running = True


while running:
    screen.fill(WHITE)  

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    keys = pygame.key.get_pressed()
    speed = 5  

    if keys[pygame.K_LEFT]:  
        player.move(-speed, 0)
    if keys[pygame.K_RIGHT]:  
        player.move(speed, 0)
    if keys[pygame.K_UP]:  
        player.move(0, -speed)
    if keys[pygame.K_DOWN]:  
        player.move(0, speed)

    
    all_sprites.draw(screen)

    
    pygame.display.flip()
    
    
    clock.tick(60)


pygame.quit()
