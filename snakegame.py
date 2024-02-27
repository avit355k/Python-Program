import pygame
import time
import random

pygame.init()

# Set up the display
WIDTH, HEIGHT = 640, 480
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Snake and food initial positions
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
food_pos = [random.randrange(1, (WIDTH//10)) * 10,
            random.randrange(1, (HEIGHT//10)) * 10]
food_spawn = True

# Initialize game variables
direction = 'RIGHT'
change_to = direction
score = 0

# Speed and clock
snake_speed = 15
clock = pygame.time.Clock()

# Game over function
def game_over():
    my_font = pygame.font.SysFont('times new roman', 35)
    game_over_surface = my_font.render(
        'Your Score is {}'.format(score), True, RED)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (WIDTH/2, HEIGHT/4)
    win.fill(WHITE)
    win.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()

# Main function
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        # Keystroke detection
        keys = pygame.key.get_pressed()
        for key in keys:
            if keys[pygame.K_LEFT]:
                change_to = 'LEFT'
            if keys[pygame.K_RIGHT]:
                change_to = 'RIGHT'
            if keys[pygame.K_UP]:
                change_to = 'UP'
            if keys[pygame.K_DOWN]:
                change_to = 'DOWN'

    # Change direction based on user input
    if change_to == 'RIGHT' and not direction == 'LEFT':
        direction = 'RIGHT'
    if change_to == 'LEFT' and not direction == 'RIGHT':
        direction = 'LEFT'
    if change_to == 'UP' and not direction == 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and not direction == 'UP':
        direction = 'DOWN'

    # Moving the snake
    if direction == 'RIGHT':
        snake_pos[0] += 10
    if direction == 'LEFT':
        snake_pos[0] -= 10
    if direction == 'UP':
        snake_pos[1] -= 10
    if direction == 'DOWN':
        snake_pos[1] += 10

    # Snake body growing mechanism
    snake_body.insert(0, list(snake_pos))
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        score += 1
        food_spawn = False
    else:
        snake_body.pop()

    if not food_spawn:
        food_pos = [random.randrange(1, (WIDTH//10)) * 10,
                    random.randrange(1, (HEIGHT//10)) * 10]
    food_spawn = True

    win.fill(WHITE)
    for pos in snake_body:
        pygame.draw.rect(win, GREEN, pygame.Rect(pos[0], pos[1], 10, 10))

    pygame.draw.rect(win, RED, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    # Game Over conditions
    if snake_pos[0] < 0 or snake_pos[0] > WIDTH-10:
        game_over()
    if snake_pos[1] < 0 or snake_pos[1] > HEIGHT-10:
        game_over()

    # Touching the snake body
    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            game_over()

    pygame.display.update()
    clock.tick(snake_speed)

# Quit the pygame
pygame.quit()
