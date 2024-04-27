'''
Файл для создания функций, в других местах не пишем!!!
'''
#импорт соседних файлов
from . import constants as c
from . import objects as obj

#импорт модуля
import time
import pygame

# функция для отрисовки камеры
def camera_func(camera, target_rect):
    camera_x = -obj.player.x + obj.screen.WIDTH / 2
    camera_y = -obj.player.y + obj.screen.HEIGHT / 2

# функция для проверки коллизий c платформой
def check_collision_platforms(object, platform_list):
    # перебираем все платформы из списка (не группы спрайтов)
    for platform in platform_list:
        if object.rect.colliderect(platform.rect):
            if object.y_velocity > 0:  # Если спрайт падает
                # меняем переменную-флаг
                object.on_ground = True
                # ставим его поверх платформы и сбрасываем скорость по оси Y
                object.rect.bottom = platform.rect.top
                object.y_velocity = 0
            elif object.y_velocity < 0:  # Если спрайт движется вверх
                # ставим спрайт снизу платформы
                object.rect.top = platform.rect.bottom
                object.y_velocity = 0
            elif object.x_velocity > 0:  # Если спрайт движется вправо
                # ставим спрайт слева от платформы
                object.rect.right = platform.rect.left
            elif object.x_velocity < 0:  # Если спрайт движется влево
                # ставим спрайт справа от платформы
                object.rect.left = platform.rect.right


# функция проверки коллизии выбранного объекта с объектами Enemies
def check_collision_enemies(object, enemies_list):
    # running делаем видимой внутри функции чтобы было возможно
    # завершить игру
    # в списке проверяем
    for enemy in enemies_list:
        # при коллизии
        if object.rect.colliderect(enemy.rect):
            # объект пропадает из всех групп спрайтов и игра заканчивается
            object.kill()
            c.running = False


# проверка


def draw_objects(camera_x, camera_y):
    # Очистка экрана
    obj.screen.fill((0, 0, 0))
    
    # Рисование объектов на экране с учетом позиции камеры
    player_rect = pygame.Rect(obj.player.x - camera_x, obj.player.y - camera_y, 50, 50)
    pygame.draw.rect(obj.screen, (255, 255, 255), player_rect)
    
    # Обновление экрана
    pygame.display.update()


# восприятие персонажа на локацию
def location_effect(location):
    # делаем видимыми переменные быстроты персонажа
    # проверка номера локации
    if location == 1:
        # изменяем быстроту персонажа
        right_rapidity = 5
        c.left_rapidity = -5
        # изменяем высоту прыжка персонажа
        up_rapidity = -9
    # проверка номера локации
    elif location == 2:
        # изменяем быстроту персонажа
        right_rapidity = 4
        c.left_rapidity = -4
        # изменяем высоту прыжка персонажа
        up_rapidity = -8
    # проверка номера локации
    elif location == 3:
        # изменяем быстроту персонажа
        right_rapidity = 3
        c.left_rapidity = -3
        # изменяем высоту прыжка персонажа
        up_rapidity = -7
    # проверка на начало катсцены
    elif location < 0:
        # изменяем быстроту персонажа
        right_rapidity = 0
        c.left_rapidity = 0
        # изменяем высоту прыжка персонажа
        up_rapidity = 0


# смена локации, (номер локации на которую подмена)
def change_location(loc):
    # делаем видимым переменную локации
    if loc == 1:
        c.location = 1
        location_effect(c.location)
        # далее подмена bg, окружения и прочего...
    if loc == 2:
        c.location = 2
        location_effect(c.location)
        # далее подмена bg, окружения и прочего...
    if loc == 3:
        c.location = 3
        location_effect(c.location)
        # далее подмена bg, окружения и прочего...

    # катсцены обозначаем как минусовые числа
    # катсцена №-1
    if loc == -1:
        c.location = -1
        location_effect(c.location)
        start_cutscene(c.location)
        # далее подмена bg, окружения и прочего...


# запуск катсцены
def start_cutscene(location):
    # проверка на катсцену №-1
    if location == -1:
        # начало катсцены
        start_time = time.monotonic()
        # длительность катсцены
        duration = 2.0
        #пока время со старта катсцены меньше чем заданное число, продолжает идти катсцена
        #временный? костыль, программа работать будет, но только в рамках этого while
        while time.monotonic() - start_time <= duration:
            # далее подмена bg, окружения и прочего...
            pass