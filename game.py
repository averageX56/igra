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
menu_flag = False


pygame.init()
font = pygame.font.Font('font.ttf', 60)
mouse_x, mouse_y = pygame.mouse.get_pos()
textures = dict()         # Создаем пустой словарь, куда далее загружаем все нужные нам текстуры
for i in range(625):
    textures[i] = pygame.image.load(f'images/{i}.png')
textures['cur_happy'] = pygame.image.load('images\\cur_happy.png')
textures['cur_money'] = pygame.image.load('images\\cur_money.png')
textures['std'] = pygame.image.load('images\\shop_learn.png')
textures['food'] = pygame.image.load('images\\shop_up.png')
textures['base_left'] = pygame.image.load('images\\shop_down_left.png')
textures['base_right'] = pygame.image.load('images\\shop_down_right.png')

world_size_chunk_x = 25//chunk_size
world_size_chunk_y = 25//chunk_size


##chunck_on_screen() по положению камеры определяет, какие чанки из имеющихся нужно прорисовать на экране
def chunks_on_screen():
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


#Функция по координате чанка определяет какая у него текстура(сейчас нет функционала)
def generate_tile(x, y, chunk_x, chunk_y):
    tile_x = (chunk_x // tile_size) + x
    tile_y = (chunk_y // tile_size) + y
    return int((chunk_x // chunk_size // tile_size) % 2 == 0)


#Функция обработки случайного события
def random_event(key):
    if key not in rnd_events_list:
        pass
    else:
        if key == 1:
            print(1)
        elif key == 2:
            print(2)


#Класс чанка
class Chunk():
    def __init__(self, x, y, type='map'):
        self.x, self.y = x, y
        self.type = type
        self.map = [generate_tile(-1, y, self.x, self.y) for y in range(chunk_size) for x in range(chunk_size)]

    #render() прорисовывает нужный нам чанк, выцеживая, какая у него текстура(не прописано)
    def render(self, texture_code):
        for y in range(chunk_size):
            for x in range(chunk_size):
                texture = textures[texture_code]
                screen.blit(texture, (self.x + x*tile_size - cam_x, self.y + y*tile_size - cam_y))


class Menu():
    def __init__(self, m_x=res[0]/2 - 330, m_y=res[1]/2 - 450):
        self.x, self.y = m_x, m_y
        self.flag = False
        self.type = 0
        self.chosen_point = 0

    def close_menu(self):
        self.flag = False

    def open_menu(self):
        self.flag = True
        if 'std' in chuncks_types[mouse_on_chunk_number]:
            self.type = 'std'
        elif 'food' in chuncks_types[mouse_on_chunk_number]:
            self.type = 'food'
        elif 'shop' in chuncks_types[mouse_on_chunk_number]:
            self.type = 'shop'
        elif 'hs' in chuncks_types[mouse_on_chunk_number] and len(chuncks_types[mouse_on_chunk_number]) == 4:
            self.type = 'base_left'
        elif 'hs' in chuncks_types[mouse_on_chunk_number] and len(chuncks_types[mouse_on_chunk_number]) == 3:
            self.type = 'base_right'

    def render(self):
        if self.flag is True:
            if self.type == 'std':
                screen.blit(textures['std'], (self.x, self.y))
                window.blit(pygame.transform.scale(screen, res), (0, 0))
            if self.type == 'food':
                screen.blit(textures['food'], (self.x, self.y))
                window.blit(pygame.transform.scale(screen, res), (0, 0))
            if self.type == 'base_left':
                screen.blit(textures['base_left'], (self.x, self.y))
                window.blit(pygame.transform.scale(screen, res), (0, 0))
            if self.type == 'base_right':
                screen.blit(textures['base_right'], (self.x, self.y))
                window.blit(pygame.transform.scale(screen, res), (0, 0))

    def point_detect(self):
        global chosen_x, chosen_y
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

class Building:
    def __init__(self):
        self.income = 0
        self.outcome = 0
        self.happy = 0
        self.built = 0

    def money_exsc(self):
        global money, happy
        money += (self.income - self.outcome) * self.built
        happy += self.happy * self.built

    def build_new(self):
        self.built += 1


class Dorm1(Building):
    def __init__(self):
        Building.__init__(self, self.built)
        self.income = 0.5
        self.outcome = 0.01
        self.happy = -0.01


class Dorm2(Building):
    def __init__(self):
        Building.__init__(self, self.built)
        self.income = 0.6
        self.outcome = 0.01
        self.happy = -0.05


class Dorm3(Building):
    def __init__(self):
        Building.__init__(self, self.built)
        self.income = 0.2
        self.outcome = 0.01
        self.happy = 0


class Foodc(Building):
    def __init__(self):
        Building.__init__(self, self.built)
        self.income = 0.5
        self.outcome = 0.1
        self.happy = 0.03


class Sport(Building):
    def __init__(self):
        Building.__init__(self, self.built)
        self.income = 0
        self.outcome = 0.2
        self.happy = 0.07


class Learn(Building):
    def __init__(self):
        Building.__init__(self, self.built)
        self.income = 0
        self.outcome = 0.6
        self.happy = 0.15


"""Запуск игры, вытягивание всей информации из файлов, инициализация объектов"""

#Чтение файла с кодами текстур чанков из памяти
chuncks_file = open('chuncks.txt', 'r+')
chuncks_texture_codes = []
chuncks_types = []
for i in range(625):
    chunk_info = chuncks_file.readline()
    just_code, just_type = chunk_info.split()
    chuncks_texture_codes.append(int(just_code))
    chuncks_types.append(just_type)
chuncks_file.close()

#Чтение файла с общей информацией
info_file = open('game_info.txt', 'r')
rnd_events_list = list(map(int, info_file.readline().split()))
info_file.close()


window = pygame.display.set_mode((0, 0), pygame.RESIZABLE)
fullscreen = pygame.display.set_mode((0, 0), pygame.RESIZABLE)
screen = pygame.transform.scale(window, res)
finished = False
clock = pygame.time.Clock()
chunks = []
chosen_x, chosen_y = 0, 0
Menu = Menu()
#создаём все чанки(пока нет работы с памятью)
for y in range(world_size_chunk_y):
    for x in range(world_size_chunk_x):
        chunks.append(Chunk(x*chunk_size*tile_size, y*chunk_size*tile_size))

for i in range(len(chunks)):
    chunks[i].type = chuncks_types[i]

"""Конец запуска игры. Собственно игровой процесс"""

while not finished:
    clock.tick(FPS)
    random_event_timer += 1
    Menu.point_detect()
    if random_event_timer == 1200:
        print('hello')
        rnd_num = random.randint(1, 32)
        #Обработка случайного события
        random_event(rnd_num)
        random_event_timer = 0
    screen.fill(WHITE)
    mouse_x, mouse_y = pygame.mouse.get_pos()
    mouse_on_chunk_x, mouse_on_chunk_y = ((mouse_x + cam_x)//tile_size, (mouse_y + cam_y)//tile_size)
    mouse_on_chunk_number = mouse_on_chunk_y * 25 + mouse_on_chunk_x
    #print(mouse_on_chunk_x, mouse_on_chunk_y)
    #print(clock.get_fps())

    #обработка зажатых клавиш
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

    #рендерим чанки, которые отображаются на экране
    for i in chunks_on_screen():
        chunks[i].render(chuncks_texture_codes[i])
    screen.blit(textures['cur_happy'], (20, 20))
    screen.blit(textures['cur_money'], (res[0]-420, 20))

    happy = mouse_x
    money = mouse_y

    text_1 = font.render(f'x = {happy}', 1, (217, 255, 76))
    screen.blit(text_1, (300, 45))
    text_2 = font.render(f'y = {money}', 1, (240, 175, 14))
    screen.blit(text_2, (res[0] - 200, 45))
    window.blit(pygame.transform.scale(screen, res), (0, 0))

    # if menu.flag:
    #     pygame.draw.rect(window, WHITE, pygame.Rect(res[0]/2 - 650/2, res[1]/2 - 450, 650, 800))
    if Menu.flag:
        Menu.render()

    #обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            chuncks_file.close()
            finished = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if Menu.flag is False:
                    #делаем сохранение

                    chuncks_file.close()
                    chuncks_file = open('chuncks.txt', 'w')
                    chuncks_file.seek(0)
                    for i in range(625):
                        chuncks_file.write(str(chuncks_texture_codes[i])+'  '+chuncks_types[i]+'\n')
                    chuncks_file.close()

                    info_file = open('game_info.txt', 'w')
                    info_file.seek(0)
                    for i in range(len(rnd_events_list)):
                        info_file.write(str(rnd_events_list[i])+' ')

                    #закрываем программу
                    finished = True
                else:
                    Menu.close_menu()
#обработка нажатия мыши
        elif event.type == pygame.MOUSEBUTTONDOWN:
            #ЛКМ
            if event.button == 1:
                #проверка типа нажатого тейла и соответсвующая обработка события
                if Menu.flag:
                    #нажатие при открытом меню
                    chosen_x, chosen_y = mouse_x, mouse_y
                elif (chuncks_types[mouse_on_chunk_number] in open_chuncks) and not Menu.flag:
                    #вызов меню при нажатии по чанку
                    Menu.open_menu()
                    print(chuncks_types[mouse_on_chunk_number])
    pygame.display.update()

pygame.quit()
