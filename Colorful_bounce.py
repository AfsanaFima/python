import pygame
import random

pygame.init()

sprite_color_change_event = pygame.USEREVENT + 1
Background_color_change_event = pygame.USEREVENT + 2

Sprite_colors = [pygame.Color('pink'),pygame.Color('blue'),pygame.Color('lavender'),pygame.Color('lightpink'),pygame.Color('skyblue'),pygame.Color('lightyellow')]

Background_colors = [pygame.Color('yellow'),pygame.Color('pink'),pygame.Color('purple'),pygame.Color('gray'),pygame.Color('skyblue'),pygame.Color('navyblue')]

class Sprite (pygame.sprite.Sprite) :
    def __init__(self,color,height,width):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill (color)
        self.rect = self.image.get_rect()
        self.velocity = [random.choice([-1,1]),random.choice([-1,1])]

    def update(self):
        if self.rect.left < 0 or self.rect.right >= 500:
           self.velocity[0] = -self.velocity[0]
           pygame.event.post(pygame.event.Event(sprite_color_change_event))

        if self.rect.top < 0 or self.rect.bottom >= 500:
           self.velocity[1] = -self.velocity[1]
           pygame.event.post(pygame.event.Event(Background_color_change_event))


    def color_change(self):
        self.image.fill(random.choice(Sprite_colors))


screen = pygame.display.set_mode((500,500))

pygame.display.set_caption("Color changing sprite")
clock = pygame.time.Clock()

sprite = Sprite(random.choice(Sprite_colors),60,60)
sprite.rect.topleft = (random.randint(0,480),random.randint(0,480))
sprites = pygame.sprite.Group(sprite)

Bg_colors = random.choice(Background_colors)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == sprite_color_change_event :
            sprite.color_change()

        if event.type == Background_color_change_event:
            Bg_colors = random.choice(Background_colors)



    sprite.update()
    screen.fill(Bg_colors )
    sprites.draw (screen)
    pygame.display.flip()

    clock.tick(240)

pygame.quit()

 