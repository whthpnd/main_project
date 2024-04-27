'''
Основной файл, only pygame ???
Классы, константы, функции, объекты пишем в других файлах!!!
Если есть ещё что-то важное, что лучше впихнуть по отдельности от мейна, говорим степану мунтяну и он делает
'''

# подключение библиотек
import pygame
import random
import time

#импорт файлов python из директории src в main
from src import constants as c
from src import classes as cl
from src import objects as obj
from src import functions as func

# инициализация Pygame
pygame.init()

# создаем счетчик частоты кадров и очков
clock = pygame.time.Clock()

# счёт игры
font = pygame.font.Font(None, 36)  # создание объекта, выбор размера шрифта
score_text = font.render("Счёт: 0", True, c.BLACK)  # выбор цвета и текст
score_rect = score_text.get_rect()  # создание хитбокса текста
score_rect.topleft = (c.WIDTH // 2, 100)  # расположение хитбокса\текста на экране

player_x = c.map_width // 2
player_y = c.map_height // 2

# создаем групп спрайтов
player_and_platforms = pygame.sprite.Group()
enemies = pygame.sprite.Group()

entityes = []

# в трех циклах добавляем объекты в соответствующие группы
for i in obj.enemies_list:
    enemies.add(i)
    entityes.append(i)

for i in obj.platforms_list:
    player_and_platforms.add(i)
    entityes.append(i)

# отдельно добавляем игрока
player_and_platforms.add(obj.player)
entityes.append(obj.player)

# игровой цикл
c.running = True

while c.running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            c.running = False
     # Очистка экрана
    obj.screen.fill((255, 255, 255))
    # Обновление счета на экране
    obj.screen.blit(score_text, score_rect)
    # проверяем нажатие на клавиши для перемещения
    keys = pygame.key.get_pressed()
    obj.player.x_velocity = 0
    if keys[pygame.K_LEFT]:
        func.location_effect(c.location)
        obj.player.x_velocity = c.left_rapidity

    if keys[pygame.K_RIGHT]:
        func.location_effect(c.location)
        obj.player.x_velocity = c.right_rapidity

    if keys[pygame.K_a]:
        func.location_effect(c.location)
        obj.player.x_velocity = c.left_rapidity
    if keys[pygame.K_d]:
        func.location_effect(c.location)
        obj.player.x_velocity = c.right_rapidity
    # условие прыжка более сложное
    if keys[pygame.K_SPACE] and obj.player.on_ground == True:
        func.location_effect(c.location)
        obj.player.y_velocity = -9
        obj.player.on_ground = False

    if keys[pygame.K_x]:
        func.change_location(-1)

    # гравитация для игрока
    obj.player.y_velocity += 0.5

    # обновляем значения атрибутов игрока и врагов
    obj.player.update()
    enemies.update()

    player_x = obj.player.x
    player_y = obj.player.y
    player_and_platforms.draw(obj.screen)
    enemies.draw(obj.screen)

    # проверяем все возможные коллизии
    func.check_collision_platforms(obj.player, obj.platforms_list)
    func.check_collision_enemies(obj.player, obj.enemies_list)

    # обновление счёта на экране
    score_text = font.render("Счёт: " + str(c.score), True, c.BLACK)

    # Обновление позиции камеры
    
    # Отрисовка объектов на экране с учетом позиции камеры
    pygame.display.update()
    clock.tick(c.FPS)

pygame.quit()