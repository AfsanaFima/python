import pygame 
pygame.init()

screen_width, screen_height = 500,600

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Add Images and background")

background_image = pygame.transform.scale(pygame.image.load())

