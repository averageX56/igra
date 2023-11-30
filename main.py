import pygame
import sys

# Инициализация Pygame
pygame.init()

# Определение цветов
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Размеры экрана
WIDTH, HEIGHT = 800, 600

# Создание экрана
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Танковая битва")

# Класс для танков
class Tank(pygame.sprite.Sprite):
    def init(self, color, x, y):
        super().init()

        self.image = pygame.Surface((50, 30))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 5

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

# Создание танков для каждого игрока
tank1 = Tank(WHITE, 100, 100)
tank2 = Tank(BLACK, 700, 500)

# Группа спрайтов
all_sprites = pygame.sprite.Group()
all_sprites.add(tank1, tank2)

# Основной игровой цикл
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    tank1.move(keys)
    tank2.move(keys)

    # Отрисовка
    screen.fill(BLACK)
    all_sprites.draw(screen)

    # Обновление экрана
    pygame.display.flip()

    # Ограничение частоты кадров
    clock.tick(60)

# Завершение Pygame
pygame.quit()
sys.exit()