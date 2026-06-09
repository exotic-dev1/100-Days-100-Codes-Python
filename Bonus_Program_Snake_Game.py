import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

clock = pygame.time.Clock()

snake = [(100, 100)]
direction = (CELL_SIZE, 0)

food = (
    random.randrange(0, WIDTH, CELL_SIZE),
    random.randrange(0, HEIGHT, CELL_SIZE)
)

score = 0
font = pygame.font.SysFont(None, 35)

running = True

while running:
    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, CELL_SIZE):
                direction = (0, -CELL_SIZE)
            elif event.key == pygame.K_DOWN and direction != (0, -CELL_SIZE):
                direction = (0, CELL_SIZE)
            elif event.key == pygame.K_LEFT and direction != (CELL_SIZE, 0):
                direction = (-CELL_SIZE, 0)
            elif event.key == pygame.K_RIGHT and direction != (-CELL_SIZE, 0):
                direction = (CELL_SIZE, 0)

    head_x, head_y = snake[0]
    new_head = (head_x + direction[0], head_y + direction[1])

    if (
        new_head[0] < 0 or new_head[0] >= WIDTH or
        new_head[1] < 0 or new_head[1] >= HEIGHT or
        new_head in snake
    ):
        print("Game Over! Score:", score)
        running = False
        continue

    snake.insert(0, new_head)

    if new_head == food:
        score += 1
        food = (
            random.randrange(0, WIDTH, CELL_SIZE),
            random.randrange(0, HEIGHT, CELL_SIZE)
        )
    else:
        snake.pop()

    screen.fill(BLACK)

    for segment in snake:
        pygame.draw.rect(
            screen, GREEN,
            (segment[0], segment[1], CELL_SIZE, CELL_SIZE)
        )

    pygame.draw.rect(
        screen, RED,
        (food[0], food[1], CELL_SIZE, CELL_SIZE)
    )

    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(10)  # Speed

pygame.quit()