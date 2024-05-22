import pygame
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pong')

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Paddle dimensions
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
BALL_SIZE = 10

# Speeds
BALL_SPEED_X, BALL_SPEED_Y = 5, 5
PADDLE_SPEED = 6

# Initialize paddles and ball
left_paddle = pygame.Rect(10, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
right_paddle = pygame.Rect(WIDTH - 20, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)

# Initialize scores
left_score = 0
right_score = 0

# Font for displaying the score
font = pygame.font.Font(None, 74)

# Game loop
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Paddle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and left_paddle.top > 0:
        left_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_s] and left_paddle.bottom < HEIGHT:
        left_paddle.y += PADDLE_SPEED
    if keys[pygame.K_UP] and right_paddle.top > 0:
        right_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and right_paddle.bottom < HEIGHT:
        right_paddle.y += PADDLE_SPEED

    # Ball movement
    ball.x += BALL_SPEED_X
    ball.y += BALL_SPEED_Y

    # Ball collision with top and bottom walls
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        BALL_SPEED_Y = -BALL_SPEED_Y

    # Ball collision with paddles
    if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
        BALL_SPEED_X = -BALL_SPEED_X

    # Ball out of bounds
    if ball.left <= 0:
        right_score += 1
        ball.x, ball.y = WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2
        BALL_SPEED_X = -BALL_SPEED_X
    if ball.right >= WIDTH:
        left_score += 1
        ball.x, ball.y = WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2
        BALL_SPEED_X = -BALL_SPEED_X

    # Drawing
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, left_paddle)
    pygame.draw.rect(screen, WHITE, right_paddle)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

    # Display scores
    left_text = font.render(str(left_score), True, WHITE)
    screen.blit(left_text, (WIDTH // 4, 10))
    right_text = font.render(str(right_score), True, WHITE)
    screen.blit(right_text, (WIDTH * 3 // 4, 10))

    pygame.display.flip()
    clock.tick(60)
import pygame
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pong')

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Paddle dimensions
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
BALL_SIZE = 10

# Speeds
BALL_SPEED_X, BALL_SPEED_Y = 5, 5
PADDLE_SPEED = 6

# Initialize paddles and ball
left_paddle = pygame.Rect(10, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
right_paddle = pygame.Rect(WIDTH - 20, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)

# Initialize scores
left_score = 0
right_score = 0

# Font for displaying the score
font = pygame.font.Font(None, 74)

# Game loop
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Paddle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and left_paddle.top > 0:
        left_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_s] and left_paddle.bottom < HEIGHT:
        left_paddle.y += PADDLE_SPEED
    if keys[pygame.K_UP] and right_paddle.top > 0:
        right_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and right_paddle.bottom < HEIGHT:
        right_paddle.y += PADDLE_SPEED

    # Ball movement
    ball.x += BALL_SPEED_X
    ball.y += BALL_SPEED_Y

    # Ball collision with top and bottom walls
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        BALL_SPEED_Y = -BALL_SPEED_Y

    # Ball collision with paddles
    if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
        BALL_SPEED_X = -BALL_SPEED_X

    # Ball out of bounds
    if ball.left <= 0:
        right_score += 1
        ball.x, ball.y = WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2
        BALL_SPEED_X = -BALL_SPEED_X
    if ball.right >= WIDTH:
        left_score += 1
        ball.x, ball.y = WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2
        BALL_SPEED_X = -BALL_SPEED_X

    # Drawing
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, left_paddle)
    pygame.draw.rect(screen, WHITE, right_paddle)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

    # Display scores
    left_text = font.render(str(left_score), True, WHITE)
    screen.blit(left_text, (WIDTH // 4, 10))
    right_text = font.render(str(right_score), True, WHITE)
    screen.blit(right_text, (WIDTH * 3 // 4, 10))

    pygame.display.flip()
    clock.tick(60)
