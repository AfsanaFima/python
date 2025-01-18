import math
import random
import pygame

screen_width = 800
screen_height = 700
player_start_x = 330
player_start_y = 400
enemy_start_y_min = 60
enemy_start_y_max = 160
enemy_speed_x = 52
enemy_speed_y = 50
bullet_speed_y = 30
collision_distance = 54

pygame.init()

screen = pygame.display.set_mode((screen_width,screen_height))

background = pygame.image.load('download.png')

pygame.display.set_caption('space invader')

playerimg = pygame.image.load('player image' )

playerX = player_start_x
playerY = player_start_y
playerX_change = 25


enemyimg = []
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []
num_of_enemies  = []


for i in range (num_of_enemies):
    enemyimg.append(pygame.image.load('enemy.png'))
    enemy_x.append(random.randint(0,screen_width - 65))
    enemy_y.append(random.randint(enemy_start_y_max,enemy_start_y_min))
    enemy_x_change.append(enemy_speed_x)
    enemy_y_change.append(enemy_speed_y)


bulletimg = pygame.image.load('bullet.jpg')
bullet_X = 0
bullet_y = player_start_y
bullet_X_change = 0
bullet_Y_change = bullet_speed_y
bullet_state = "ready"

score_value = 0
font = pygame.font.Font('freesansbold.ttf',32)
text_x = 20
text_y = 20

over_font = pygame.font.Font('freesansbold.ttf',50)

def show_score(x,y):
    score = font.render("score : "+ str(score_value),True,(350,250,222))
    screen.blits(score,(x,y))


def game_over_text ():
    over_text = over_font.render("GAME OVERRR",True,(350,250,222))
    screen.blits(over_text,(200,260))

def player (x,y) :
    screen.blit(playerimg(x,y))

def enemy(x,y,i) :
    screen.blit(enemyimg[i],(x,y))

def fire_bullet (x,y):
    global bullet_state 
    bullet_state = 'fire'
    screen.blit(bulletimg,(x+16,y+10))


                        






