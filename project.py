import pygame

pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sprite Movement Game")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

sprite1 = pygame.Rect(100, 100, 50, 50)  
sprite2 = pygame.Rect(300, 100, 50, 50)  

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
             

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: sprite1.x -= 5
    if keys[pygame.K_RIGHT]: sprite1.x += 5
    if keys[pygame.K_UP]: sprite1.y -= 5
    if keys[pygame.K_DOWN]: sprite1.y += 5

    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, sprite1)
    pygame.draw.rect(screen, BLUE, sprite2)

    pygame.display.flip()