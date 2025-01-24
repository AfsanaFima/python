import math
import random
import pygame

screen_width = 800
screen_height = 700
player_start_x = 330
player_start_y = 400
enemy_start_y_min = 60
enemy_start_y_max = 160
enemy_speed_x = 4
enemy_speed_y = 40
bullet_speed_y = 10
collision_distance = 27

pygame.init()

screen = pygame.display.set_mode((screen_width,screen_height))

background = pygame.image.load('download.png')

pygame.display.set_caption('space invader')

playerimg = pygame.image.load('player.png' )

playerX = player_start_x
playerY = player_start_y
playerX_change = 25


enemyimg = []
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []
num_of_enemies  = 6 


for i in range (num_of_enemies):
    enemyimg.append(pygame.image.load('enemy.png'))
    enemy_x.append(random.randint(0,screen_width - 65))
    enemy_y.append(random.randint(enemy_start_y_min,enemy_start_y_max))
    enemy_x_change.append(enemy_speed_x)
    enemy_y_change.append(enemy_speed_y)


bulletimg = pygame.image.load('bullet.png')
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
    score = font.render("score : "+ str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))


def game_over_text ():
    over_text = over_font.render("GAME OVERRR",True,(255,250,222))
    screen.blit(over_text,(200,260))

def player (x,y) :
    screen.blit(playerimg,(x,y))

def enemy(x,y,i) :
    screen.blit(enemyimg[i],(x,y))

def fire_bullet (x,y):
    global bullet_state 
    bullet_state = 'fire'
    screen.blit(bulletimg,(x+16,y+10))


def isCollision(enemyX,enemyY,bulletX,bulletY):
    distance= math.sqrt((enemyX-bulletX)** 2 + (enemyY-bulletY)** 2)
    return distance < collision_distance



running = True
while running:
    screen.fill((0,0,0))
    screen.blit(background,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5

            if event.key == pygame.K_SPACE and bullet_state == 'ready':
                bullet_X = playerX
                fire_bullet(bullet_X,bullet_y)

        if event.type == pygame.KEYUP and event.key in [pygame.K_LEFT,pygame.K_RIGHT]:
            playerX_change == 0

    
    playerX  =  playerX_change
    playerX = max(0,min(playerX,screen_width -50))



    for i in range (num_of_enemies):
        if enemy_y[i] > 340 :
            for j in range (num_of_enemies):
                enemy_y[j] = 2000

            game_over_text()
            break

        enemy_x[i] += enemy_x_change[i]
        if enemy_x[i] <= 0 or enemy_x[i] >= screen_width  - 50:
            enemy_x_change [i] *= -1
            enemy_y[i] += enemy_y_change [i]


        if isCollision(enemy_x[i],enemy_y[i],bullet_X,bullet_y) :
            bullet_y = player_start_y
            bullet_state = 'ready'
            score_value += 1
            enemy_x[i] = random.randint(0,screen_width - 50)
            enemy_y[i] = random.randint(enemy_start_y_min,enemy_start_y_max)

        enemy(enemy_x[i],enemy_y[i],i)


    if bullet_y <= 0 :
        bullet_y = player_start_y
        bullet_state = 'ready'

    elif bullet_state =='fire' :
        fire_bullet (bullet_X,bullet_y)
        bullet_y -= bullet_Y_change

    
    player(playerX,playerY)
    show_score(text_x,text_y)
    pygame.display.update()
        

            



                        






