import pygame
from рабочий import *
import math
import random
import time
from tkinter import *
from tkinter import messagebox


FPS = 60

chunk_size = 1
tile_size = 150
cam_speed = 15
random_event_timer = -500

WHITE = 0xFFFFFF

cam_x, cam_y = 0, 0
res = [1540, 960]


pygame.init()
font = pygame.font.Font('font.ttf', 60)
mouse_x, mouse_y = pygame.mouse.get_pos()
world_size_chunk_x = 25//chunk_size
world_size_chunk_y = 25//chunk_size

# Создаем пустой словарь, куда далее загружаем все нужные нам текстуры
textures = dict()
for i in range(625):
    textures[str(i)] = pygame.image.load(f'images/{i}.png')
textures['cur_happy'] = pygame.image.load('images\\cur_happy.png')
textures['cur_money'] = pygame.image.load('images\\cur_money.png')
textures['std'] = pygame.image.load('images\\shop_learn.png')
textures['food'] = pygame.image.load('images\\shop_up.jpg')
textures['hs_left'] = pygame.image.load('images\\shop_down_left.png')
textures['hs_right'] = pygame.image.load('images\\shop_down_right.png')
for t in ['GK', 'KPM', 'NK', 'LK', 'ARKTICA', 'CIFRA']:
    for r in range(1, 10):
        textures[t+str(r)] = pygame.image.load('images\\'+t+'_0'+str(r)+'.jpg')
for i in range(1, 15):
    for j in range(1, 5):
        textures['dm' + str(i) + '_' + str(j)] = pygame.image.load('images\\dorm'+str(i)+'_0'+str(j+int(j > 2))+'.jpg')
for i in ['sport1', 'sport2', 'sport0', 'shop', 'food1', 'food2', 'KSP']:
    for j in range(1, 5):
        textures[i+str(j)] = pygame.image.load('images\\' + i + '_0' + str(j+int(j > 2))+'.jpg')


# chunck_on_screen() по положению камеры определяет, какие чанки из имеющихся нужно прорисовать на экране
def chunks_on_screen():
    """
    :return: список чанков, которые в данный момент изображены на экране
    """
    x1 = cam_x // (chunk_size * tile_size)
    y1 = cam_y // (chunk_size * tile_size)

    x2 = (cam_x + res[0]) // (chunk_size * tile_size)
    y2 = (cam_y + res[1]) // (chunk_size * tile_size)

    x1 = min(max(x1, 0), world_size_chunk_x - 1)
    x2 = min(max(x2, 0), world_size_chunk_x - 1)

    y1 = min(max(y1, 0), world_size_chunk_y - 1)
    y2 = min(max(y2, 0), world_size_chunk_y - 1)

    result = []
    for y in range(y1, y2 + 1):
        for x in range(x1, x2 + 1):
            result.append(x+y*world_size_chunk_x)
    return result


class Chunk:
    """
    класс чанка - квадрат на экране размером 150 * 150 пикселей
    """
    def __init__(self, x, y, type='map'):
        """
        :param x: координата x левого верхнего края чанка
        :param y: координата y левого верхнего края чанка
        :param type: тип чанка. используется для обработки нажатий на чанк
        """
        self.x, self.y = x, y
        self.type = type

    def render(self, texture_code):
        """
        :param texture_code: код чанка
        :return: отрисовывает чанк на экране с текстурой, соответсвующей коду чанка
        """
        texture = textures[texture_code]
        screen.blit(texture, (self.x - cam_x, self.y - cam_y))


class Menu:
    def __init__(self, m_x=res[0]/2 - 330, m_y=res[1]/2 - 450):
        self.x, self.y = m_x, m_y
        self.flag = False
        self.type = 0
        self.chosen_point = 0

    def close_menu(self):
        self.flag = False

    def build(self):

        global money, just_menu_chunck
        if self.type == 'std' and money > cost[0][self.chosen_point]:
            global std_massive
            new_textures = building_textures_std[self.chosen_point - 1 - 2 * int(self.chosen_point > 3)]
            std_massive[self.chosen_point] = True
            std_mas[self.chosen_point - 1 - 2 * int(self.chosen_point > 3)] = 1
            Learn.built += 1
            money -= cost[0][self.chosen_point]
        elif self.type == 'hs_right' and money > cost[1][self.chosen_point]:
            global hs_right_massive
            new_textures = building_textures_hs_right[self.chosen_point - 1]
            hs_right_massive[self.chosen_point] = True
            hs_right_mas[self.chosen_point - 1] = 1
            Dorm2.built += 1
            money -= cost[1][self.chosen_point]
        elif self.type == 'hs_left' and money > cost[2][self.chosen_point]:
            global hs_left_massive
            new_textures = building_textures_hs_left[self.chosen_point - 1]
            hs_left_massive[self.chosen_point] = True
            hs_left_mas[self.chosen_point - 1] = 1
            Dorm1.built += 1
            money -= cost[2][self.chosen_point]
        elif self.type == 'food' and money > cost[3][self.chosen_point]:
            global food_massive
            new_textures = building_textures_food[self.chosen_point - 1 - 3 * int(self.chosen_point > 3)]
            food_massive[self.chosen_point] = True
            food_mas[self.chosen_point - 1 - 3 * int(self.chosen_point > 3)] = 1
            Foodc.built += 1
            money -= cost[3][self.chosen_point]
        for x in buldings:
            if just_menu_chunck in x:
                just_bulding = x
                break
        k = 0
        for i in just_bulding:
            chuncks_texture_codes[i] = new_textures[k]
            k += 1

    def open_menu(self):
        self.flag = True
        if 'std' in chuncks_types[mouse_on_chunk_number]:
            self.type = 'std'
        elif ('food' in chuncks_types[mouse_on_chunk_number]) or ('shop' in chuncks_types[mouse_on_chunk_number]):
            self.type = 'food'
        elif 'hs' in chuncks_types[mouse_on_chunk_number] and len(chuncks_types[mouse_on_chunk_number]) == 4:
            self.type = 'hs_left'
        elif 'hs' in chuncks_types[mouse_on_chunk_number] and len(chuncks_types[mouse_on_chunk_number]) == 3:
            self.type = 'hs_right'

    def render(self):
        if self.flag is True:
            if self.type == 'std':
                screen.blit(textures['std'], (self.x, self.y))
                window.blit(pygame.transform.scale(screen, res), (0, 0))
            if self.type == 'food':
                screen.blit(textures['food'], (self.x, self.y))
                window.blit(pygame.transform.scale(screen, res), (0, 0))
            if self.type == 'hs_left':
                screen.blit(textures['hs_left'], (self.x, self.y))
                window.blit(pygame.transform.scale(screen, res), (0, 0))
            if self.type == 'hs_right':
                screen.blit(textures['hs_right'], (self.x, self.y))
                window.blit(pygame.transform.scale(screen, res), (0, 0))

    def __point_detect(self):
        global chosen_x, chosen_y
        print(self.chosen_point)
        if chosen_x in range(470, 738):
            if chosen_y in range(155, 205):
                self.chosen_point = 1
            elif chosen_y in range(255, 305):
                self.chosen_point = 2
            elif chosen_y in range(360, 410):
                self.chosen_point = 3
            elif chosen_y in range(460, 510):
                self.chosen_point = 4
            elif chosen_y in range(560, 610):
                self.chosen_point = 5
        if chosen_x in range(783, 1050):
            if chosen_y in range(155, 205):
                self.chosen_point = 6
            elif chosen_y in range(255, 305):
                self.chosen_point = 7
            elif chosen_y in range(360, 410):
                self.chosen_point = 8
            elif chosen_y in range(460, 510):
                self.chosen_point = 9
            elif chosen_y in range(560, 610):
                self.chosen_point = 10

    def processing_click(self):
        self.__point_detect()
        if self.type == 'std':
            if self.chosen_point in std_massive:
                if std_massive[self.chosen_point] is True:
                    print('built')
                else:
                    print('not built')
                    self.build()
        elif self.type == 'hs_right':
            if self.chosen_point in hs_right_massive:
                if hs_right_massive[self.chosen_point] is True:
                    print('built')
                else:
                    print('not built')
                    self.build()
        elif self.type == 'hs_left':
            if self.chosen_point in hs_left_massive:
                if hs_left_massive[self.chosen_point] is True:
                    print('built')
                else:
                    print('not built')
                    self.build()
        elif self.type == 'food':
            if self.chosen_point in food_massive:
                if food_massive[self.chosen_point] is True:
                    print('built')
                else:
                    print('not built')
                    self.build()


class Building:
    def __init__(self):
        self.income = 0
        self.outcome = 0
        self.happy = 0
        self.built = 0
        self.key = 0

    def money_exsc(self):
        global money, happy
        money += (self.income - self.outcome) * self.built
        happy += self.happy * self.built


    # Функция обработки случайного события
    def random_event(self):
        """
        :param key: случайное число, от которого зависит произошедшее событие
        :return: в зависимости от key брабатывает случайное событие
        """
        if self.key not in rnd_events_list:
            pass
        else:
            if self.key == 1:
                print(1)
            elif self.key == 2:
                print(2)


class Dormitory1(Building):
    def __init__(self):
        self.built = 0
        self.income = 0.5
        self.outcome = 0.01
        self.happy = -0.01


class Dormitory2(Building):
    def __init__(self):
        self.built = 0
        self.income = 0.6
        self.outcome = 0.01
        self.happy = -0.05


class Foodbuild(Building):
    def __init__(self):
        self.built = 0
        self.income = 0.5
        self.outcome = 0.1
        self.happy = 0.03


class Learn_build(Building):
    def __init__(self):
        self.built = 0
        self.income = 0
        self.outcome = 0.6
        self.happy = 0.15


"""Запуск игры, вытягивание всей информации из файлов, инициализация объектов"""

# Чтение файла с кодами текстур чанков из памяти
chuncks_file = open('chuncks.txt', 'r')
chuncks_texture_codes = []
chuncks_types = []
for i in range(625):
    chunk_info = chuncks_file.readline()
    just_code, just_type = chunk_info.split()
    chuncks_texture_codes.append(just_code)
    chuncks_types.append(just_type)
chuncks_file.close()

# Чтение файла с общей информацией
info_file = open('game_info.txt', 'r')
std_mas = list(map(bool, list(map(int, info_file.readline().split()))))
hs_right_mas = list(map(bool, list(map(int, info_file.readline().split()))))
hs_left_mas = list(map(bool, list(map(int, info_file.readline().split()))))
food_mas = list(map(bool, list(map(int, info_file.readline().split()))))
rnd_events_list = info_file.readline().split()
info_file.close()
std_massive = dict()
hs_right_massive = dict()
hs_left_massive = dict()
food_massive = dict()
c = 0
for i in [1, 2, 3, 6, 7, 8]:
    std_massive[i] = std_mas[c]
    c += 1
c = 0
for i in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    hs_right_massive[i] = hs_right_mas[c]
    c += 1
c = 0
for i in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    hs_left_massive[i] = hs_left_mas[c]
    c += 1
c = 0
for i in [1, 2, 6, 7]:
    food_massive[i] = food_mas[c]
    c += 1


window = pygame.display.set_mode((0, 0), pygame.RESIZABLE)
fullscreen = pygame.display.set_mode((0, 0), pygame.RESIZABLE)
screen = pygame.transform.scale(window, res)
finished = False
clock = pygame.time.Clock()
chunks = []
chosen_x, chosen_y = 0, 0
money = 2000
happy = 1000
Menu = Menu()
Dorm1 = Dormitory1()
Dorm2 = Dormitory2()
Learn = Learn_build()
Foodc = Foodbuild()

# Создаём все чанки(пока нет работы с памятью)
for y in range(world_size_chunk_y):
    for x in range(world_size_chunk_x):
        chunks.append(Chunk(x*chunk_size*tile_size, y*chunk_size*tile_size))

for i in range(len(chunks)):
    chunks[i].type = chuncks_types[i]

"""Конец запуска игры. Собственно игровой процесс"""

while not finished:
    clock.tick(FPS)
    random_event_timer += 1
    if random_event_timer == 1200:
        rnd_num = random.randint(1, 32)
        # Обработка случайного события
        random_event(rnd_num)
        random_event_timer = 0
    screen.fill(WHITE)
    mouse_x, mouse_y = pygame.mouse.get_pos()
    mouse_on_chunk_x, mouse_on_chunk_y = ((mouse_x + cam_x)//tile_size, (mouse_y + cam_y)//tile_size)
    mouse_on_chunk_number = mouse_on_chunk_y * 25 + mouse_on_chunk_x

    # Обработка зажатых клавиш
    key = pygame.key.get_pressed()
    if key[pygame.K_a]:
        if cam_x >= 15:
            cam_x -= cam_speed
    if key[pygame.K_w]:
        if cam_y >= 15:
            cam_y -= cam_speed
    if key[pygame.K_d]:
        if cam_x <= world_size_chunk_x * tile_size - res[0] - cam_speed:
            cam_x += cam_speed
    if key[pygame.K_s]:
        if cam_y <= world_size_chunk_y * tile_size - res[1] - cam_speed:
            cam_y += cam_speed

    # Рендерим чанки, которые отображаются на экране
    for i in chunks_on_screen():
        chunks[i].render(chuncks_texture_codes[i])
    screen.blit(textures['cur_happy'], (20, 20))
    screen.blit(textures['cur_money'], (res[0]-420, 20))
    Dorm1.money_exsc()
    Dorm2.money_exsc()
    Learn.money_exsc()
    Foodc.money_exsc()
    text_1 = font.render(f'x = {round(happy)}', 1, (217, 255, 76))
    screen.blit(text_1, (260, 45))
    text_2 = font.render(f'y = {round(money)}', 1, (240, 175, 14))
    screen.blit(text_2, (res[0] - 180, 45))
    window.blit(pygame.transform.scale(screen, res), (0, 0))

    if Menu.flag:
        Menu.render()

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            chuncks_file.close()
            finished = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if Menu.flag is False:
                    # Делаем сохранение

                    chuncks_file.close()
                    chuncks_file = open('chuncks.txt', 'w')
                    chuncks_file.seek(0)
                    for i in range(625):
                        chuncks_file.write(str(chuncks_texture_codes[i])+'  '+chuncks_types[i]+'\n')
                    chuncks_file.close()

                    info_file = open('game_info.txt', 'w')
                    info_file.seek(0)
                    for i in range(len(std_mas)):
                        info_file.write(str(int(std_mas[i])) + ' ')
                    info_file.write('\n')
                    for i in range(len(hs_right_mas)):
                        info_file.write(str(int(hs_right_mas[i])) + ' ')
                    info_file.write('\n')
                    for i in range(len(hs_left_mas)):
                        info_file.write(str(int(hs_left_mas[i])) + ' ')
                    info_file.write('\n')
                    for i in range(len(food_mas)):
                        info_file.write(str(int(food_mas[i])) + ' ')
                    info_file.close()

                    # Закрываем программу
                    finished = True
                else:
                    Menu.close_menu()
# Обработка нажатия мыши
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # ЛКМ
            if event.button == 1:
                # Проверка типа нажатого тейла и соответсвующая обработка события
                if Menu.flag:
                    # Нажатие при открытом меню
                    chosen_x, chosen_y = mouse_x, mouse_y
                    Menu.processing_click()
                elif (chuncks_types[mouse_on_chunk_number] in open_chuncks) and not Menu.flag:
                    # Вызов меню при нажатии по чанку
                    Menu.open_menu()
                    just_menu_chunck = mouse_on_chunk_number
                    print(chuncks_types[mouse_on_chunk_number])
    pygame.display.update()

pygame.quit()
