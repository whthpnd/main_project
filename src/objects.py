'''
Файл для создания объектов и экрана(не знал куда впихнуть), в других местах не пишем!!!
'''
#импорт соседних файлов
from . import classes as cl
from . import constants as c

#импорт модуля 
import pygame 

# создаем игрока, платформы, врагов и то, что будем собирать в игре
player = cl.Player(50, 50)
platforms_list = [cl.Platform(0, c.HEIGHT - 25, c.WIDTH, 50), cl.Platform(50, 150, 100, 20), cl.Platform(100, 350, 100, 20),
                  cl.Platform(250, 170, 100, 20)]
enemies_list = [cl.Enemy(120, 315)]
collectibles_list = [cl.Collectible(280, 135)]
#создание экрана
screen = pygame.display.set_mode((c.WIDTH, c.HEIGHT))