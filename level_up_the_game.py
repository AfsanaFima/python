import pygame
import random


# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Player vs Enemies Collision Game")

# Load background image
background_image = pygame.image.load("background.jpg")  
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))


# Load background music
pygame.mixer.music.load("background.mp3")  # Make sure this file is in the same folder
pygame.mixer.music.play(-1)  # Play on loop

# Colors
RED = (200, 0, 0)
BLUE = (0, 0, 200)

# Game variables
score = 0
font = pygame.font.Font(None, 36)

# Player sprite
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT // 2))

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += 5
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= 5
        if keys[pygame.K_DOWN] and self.rect.bottom < HEIGHT:
            self.rect.y += 5

# Enemy sprite
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - 50)
        self.rect.y = random.randint(0, HEIGHT - 50)

# Sprite groups
player = Player()
enemies = pygame.sprite.Group()

for _ in range(7):
    enemy = Enemy()
    enemies.add(enemy)

all_sprites = pygame.sprite.Group(player, *enemies)

# Game loop
running = True
while running:
    # Draw background image
    screen.blit(background_image, (0, 0))

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update player
    player.update()

    # Check for collisions
    collided_enemies = pygame.sprite.spritecollide(player, enemies, False)
    if collided_enemies:
        score += 1
        for enemy in collided_enemies:
            enemy.rect.x = random.randint(0, WIDTH - 50)
            enemy.rect.y = random.randint(0, HEIGHT - 50)

    # Draw all sprites
    all_sprites.draw(screen)

    # Display score
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    # Refresh display
    pygame.display.flip()
    pygame.time.delay(30)

pygame.quit()
