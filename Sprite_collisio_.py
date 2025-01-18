import pygame
import random

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 400
MOVEMENT_SPEED = 5
FONT_SIZE = 60
FPS = 60

# Initialize Pygame
pygame.init()
background_image = pygame.image.load("bg.jpg")  # Ensure bg.jpg is in the same directory or provide the correct path
font = pygame.font.SysFont("times new roman", FONT_SIZE)

# Sprite Class
class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

    def move(self, x_change, y_change):
        """Handles sprite movement with boundary checks."""
        self.rect.x = max(0, min(self.rect.x + x_change, SCREEN_WIDTH - self.rect.width))
        self.rect.y = max(0, min(self.rect.y + y_change, SCREEN_HEIGHT - self.rect.height))


def draw_text(screen, text, font, color, x, y):
    """Utility function to render text on the screen."""
    rendered_text = font.render(text, True, color)
    screen.blit(rendered_text, (x, y))


def main():
    # Screen Setup
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Sprite Collision")

    # Create Sprites
    player = Sprite(pygame.Color("black"), 30, 20)
    player.rect.x, player.rect.y = 50, 50

    target = Sprite(pygame.Color("pink"), 30, 20)
    target.rect.x, target.rect.y = random.randint(50, 400), random.randint(50, 300)

    all_sprites = pygame.sprite.Group(player, target)

    # Game Variables
    running = True
    won = False
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if not won:
            # Handle Movement
            keys = pygame.key.get_pressed()
            x_change = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * MOVEMENT_SPEED
            y_change = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * MOVEMENT_SPEED
            player.move(x_change, y_change)

            # Check Collision
            if player.rect.colliderect(target.rect):
                all_sprites.remove(target)
                player.image.fill(pygame.Color("green"))  # Change player color on win
                won = True

        # Draw Everything
        screen.blit(background_image, (0, 0))
        all_sprites.draw(screen)

        if won:
            draw_text(screen, "You Won!!! 🎉", font, pygame.Color("purple"), SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
