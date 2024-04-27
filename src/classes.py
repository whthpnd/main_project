'''
Файл для создания классов - в других местах не пишем!!!
'''
#импорт модулей
import pygame
import random
#импорт соседнего файла
from . import constants as c
# класс для игрока

class Entity(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        super().__init__()
        self.x = x
        self.y = y
        # Создание поверхности для изображения сущности и заполнение цветом
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        
        # Получение прямоугольника, описывающего положение сущности на экране
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x_velocity = 0
        self.y_velocity = 0
        self.on_ground = False

    def update(self):
        # Обновление позиции сущности на основе скоростей
        self.rect.x += self.x_velocity
        self.rect.y += self.y_velocity

class Player(Entity):
    def __init__(self, x, y, width, height, color):
        super().__init__(x, y, width, height, color)
        self.jump_power = -10

    def jump(self):
        # Прыжок игрока
        if self.on_ground:
            self.y_velocity = self.jump_power
            self.on_ground = False

    def move_left(self):
        # Движение игрока влево
        self.x_velocity = -5

    def move_right(self):
        # Движение игрока вправо
        self.x_velocity = 5

    def stop(self):
        # Остановка движения игрока
        self.x_velocity = 0


class Enemy(Entity):
    def __init__(self, x, y, width, height, color, speed):
        super().__init__(x, y, width, height, color)
        self.speed = speed
    

    def move_left(self):
        # Движение врага влево
        self.x_velocity = -self.speed

    def move_right(self):
        # Движение врага вправо
        self.x_velocity = self.speed

    def stop(self):
        # Остановка движения врага
        self.x_velocity = 0

    def update(self):
        # Обновление положения врага на основе скорости
        self.x += self.x_velocity

# класс для платформы
class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill((0,255,0))  # цвет платформы
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Camera:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def update_x(self, other_self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            other_self.rect.x -= c.right_rapidity
        if keys[pygame.K_LEFT]:
            other_self.rect.x -= c.left_rapidity