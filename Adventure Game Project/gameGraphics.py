import pygame

pygame.init()

grid_size = 32
grid_width = 10
grid_height = 10
screen_width = 320
screen_height = 320

screen = pygame.display.set_mode((screen_width, screen_height))
player = pygame.Rect(0, 0, 32, 32)

running = True
while running:
    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, (255, 0, 0), player)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False

#here i added functionality for wrapping the player sprite on edges using modulo operation
            elif event.key == pygame.K_UP:
                player.y = (player.y - grid_size) % screen_height
            elif event.key == pygame.K_DOWN:
                player.y = (player.y + grid_size) % screen_height
            elif event.key == pygame.K_LEFT:
                player.x = (player.x - grid_size) % screen_width
            elif event.key == pygame.K_RIGHT:
                player.x = (player.x + grid_size) % screen_width

    pygame.display.flip()
pygame.quit()