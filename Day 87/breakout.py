import pygame
import random

# Initialize pygame
pygame.init()

# Game Constants
WIDTH, HEIGHT = 500, 400
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 102, 204)
RED = (255, 0, 0)
BRICK_ROWS, BRICK_COLS = 5, 7
BRICK_WIDTH, BRICK_HEIGHT = 60, 20

# Create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Breakout Game")

# Paddle settings
paddle_width, paddle_height = 80, 10
paddle_x = (WIDTH - paddle_width) // 2
paddle_speed = 7

# Ball settings
ball_radius = 8
ball_x, ball_y = WIDTH // 2, HEIGHT // 2
ball_dx, ball_dy = random.choice([-3, 3]), -3

# Brick setup
bricks = []
for row in range(BRICK_ROWS):
    for col in range(BRICK_COLS):
        brick_x = col * (BRICK_WIDTH + 5) + 25
        brick_y = row * (BRICK_HEIGHT + 5) + 50
        bricks.append(pygame.Rect(brick_x, brick_y, BRICK_WIDTH, BRICK_HEIGHT))

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(WHITE)

    # Event handling
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move paddle
    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle_x < WIDTH - paddle_width:
        paddle_x += paddle_speed

    # Ball movement
    ball_x += ball_dx
    ball_y += ball_dy

    # Ball collision with walls
    if ball_x <= 0 or ball_x >= WIDTH - ball_radius * 2:
        ball_dx = -ball_dx
    if ball_y <= 0:
        ball_dy = -ball_dy

    # Ball collision with paddle
    paddle_rect = pygame.Rect(paddle_x, HEIGHT - 30, paddle_width, paddle_height)
    if paddle_rect.collidepoint(ball_x, ball_y + ball_radius):
        ball_dy = -ball_dy

    # Ball collision with bricks
    for brick in bricks[:]:  # Iterate over a copy of the list
        if brick.collidepoint(ball_x, ball_y):
            bricks.remove(brick)
            ball_dy = -ball_dy
            break  # Avoid multiple collisions at once

    # Draw bricks
    for brick in bricks:
        pygame.draw.rect(screen, RED, brick)

    # Draw paddle
    pygame.draw.rect(screen, BLUE, paddle_rect)

    # Draw ball
    pygame.draw.circle(screen, BLACK, (ball_x, ball_y), ball_radius)

    # Check for game over
    if ball_y > HEIGHT:
        print("Game Over!")
        running = False

    # Check for win
    if not bricks:
        print("You Win!")
        running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
