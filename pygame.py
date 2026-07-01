import pygame
import random

pygame.init()
pygame.mixer.init()

WIDTH = 800
HEIDHT = 600

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIDHT))
pygame.display.set_caption('Убеги от препятствий')
sound = pygame.mixer.Sound('electric_dreams_Web7.mp3')

clock = pygame.time.Clock()

# Границы экрана
top_Bondary = 0
bottom_bondary = HEIDHT


# Размеры объектов игры 
player_total_syze = 50
obstacle_total_size = 50


# скорость объектов
player_speed = 10
obstacle_speed = 5
score = 0
level = 1


# определение начальной позиции игрока и препятствия
player_x = WIDTH / 2 - player_total_syze / 2
player_y = HEIDHT / 2 - player_total_syze / 2

obstacle_x = WIDTH
obstacle_y = random.randint(top_Bondary, bottom_bondary - obstacle_total_size)

# контроль цикла игры 

game_start = True

# отоброжение написанный текст
def dysplay_text(text, font_size, x, y, color):
    font = pygame.font.Font(None, font_size)
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

while game_start:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_start = False

    # Обновления
    sound.play()
    
    # нажатие клавишь для игрока 
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player_y > top_Bondary:
        player_y -= player_speed
    if keys[pygame.K_DOWN] and player_x < bottom_bondary - player_total_syze:
        player_y += player_speed

    obstacle_x -= obstacle_speed
  
    if obstacle_x + obstacle_total_size < 0:
        obstacle_x = WIDTH
        obstacle_y = random.randint(top_Bondary, bottom_bondary - obstacle_total_size)
        score += 1

        if score % 10 == 0:
            level +=1
            obstacle_speed += 5

    # проверка на столкновение 
    if  player_x + player_total_syze > obstacle_x and player_x < obstacle_x + obstacle_total_size and player_y + player_total_syze > obstacle_y and player_y < obstacle_y + obstacle_total_size:
         game_start = False

    
    # отрисовка окна
    screen.fill(BLACK)

    # отрисовка
    pygame.draw.rect(screen, WHITE, (player_x, player_y, player_total_syze, player_total_syze))
    pygame.draw.rect(screen, WHITE, (obstacle_x, obstacle_y, obstacle_total_size, obstacle_total_size))

    dysplay_text(f'score: {score}', 25, 10, 10, WHITE)
    dysplay_text(f'level: {level}', 25, 10, 40, WHITE)

    pygame.display.update()
    clock.tick(60)

pygame.quit()