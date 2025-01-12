import pygame

def main () :
    pygame.init()
    screen_width , screen_height = 500,500
    screen = pygame.display.set_mode((screen_width,screen_height))

    pygame.display.set_caption("color changing sprite")

    colors ={
        'red' : pygame.Color('red'),
        'lavender' : pygame.Color('lavender'),
        'teal' : pygame.Color('teal'),
        'light pink' : pygame.Color('light pink'),
        'light blue' : pygame.Color('light blue')
    }

    current_color = colors['lavender']
    x,y = 40,50
    width,height = 60, 70 
    clock = pygame.time.Clock()

    done = False
    while not done :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_UP]: y -=3
            if pressed[pygame.K_DOWN]: y +=3
            if pressed[pygame.K_LEFT]: x -=3
            if pressed[pygame.K_RIGHT]: y +=3

            y = max(0,min())

