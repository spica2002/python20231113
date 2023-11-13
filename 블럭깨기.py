import pygame
import random

# 초기화
pygame.init()

# 화면 설정
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("블록 깨기 게임")

# 색깔 정의
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# 패들 설정
paddle_width = 100
paddle_height = 10
paddle_x = (screen_width - paddle_width) // 2
paddle_y = screen_height - paddle_height - 10

# 공 설정
ball_radius = 10
ball_x = random.randint(ball_radius, screen_width - ball_radius)
ball_y = paddle_y - ball_radius - 5
ball_speed_x = 7
ball_speed_y = -7

# 블록 설정
block_width = 50
block_height = 20
block_count = 8
block_colors = [RED, BLUE]
blocks = []

for i in range(block_count):
    block_x = i * (block_width + 2) + 1
    block_y = 50
    block_color = block_colors[i % 2]
    blocks.append(pygame.Rect(block_x, block_y, block_width, block_height))

# 게임 루프
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= 7
    if keys[pygame.K_RIGHT] and paddle_x < screen_width - paddle_width:
        paddle_x += 7

    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # 화면 경계 체크
    if ball_x <= ball_radius or ball_x >= screen_width - ball_radius:
        ball_speed_x = -ball_speed_x
    if ball_y <= ball_radius:
        ball_speed_y = -ball_speed_y

    # 패들과 공 충돌 체크
    if (
        paddle_x < ball_x < paddle_x + paddle_width
        and paddle_y < ball_y < paddle_y + paddle_height
    ):
        ball_speed_y = -ball_speed_y

    # 블록과 공 충돌 체크
    for block in blocks:
        if block.colliderect(ball_x - ball_radius, ball_y - ball_radius, 2 * ball_radius, 2 * ball_radius):
            blocks.remove(block)
            ball_speed_y = -ball_speed_y

    screen.fill(WHITE)

    pygame.draw.rect(screen, BLUE, (paddle_x, paddle_y, paddle_width, paddle_height))
    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)

    for block in blocks:
        pygame.draw.rect(screen, block_colors[blocks.index(block) % 2], block)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
