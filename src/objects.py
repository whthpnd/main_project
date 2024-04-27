'''
Файл для создания объектов и экрана(не знал куда впихнуть), в других местах не пишем!!!
'''
#импорт соседних файлов
from . import classes as cl
from . import constants as c

#импорт модуля 
import pygame 

# создаем игрока, платформы, врагов и то, что будем собирать в игре
player = cl.Player(330, 50, 50, 50, (0,0,0))
platforms_list = [cl.Platform(0, c.HEIGHT - 25, c.WIDTH, 50), cl.Platform(50, 150, 100, 20), cl.Platform(100, 350, 100, 20),
                  cl.Platform(250, 170, 100, 20)]
enemies_list = [cl.Enemy(120, 315, 50, 50, (255, 0, 0), c.speed_enemy)]
rect_list = [pygame.Rect(50, 50, 50, 50)]
#создание экрана
screen = pygame.display.set_mode((c.WIDTH, c.HEIGHT))

camera = cl.Camera(0, 0)
