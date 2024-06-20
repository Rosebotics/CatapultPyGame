import pygame
import sys


pygame.init()
pygame.display.set_caption("Hello David Fisher")
screen = pygame.display.set_mode((800, 600))

while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(pygame.Color("Gray"))
    pygame.draw.circle(screen, pygame.Color("Orange"), (50,50), 25)
    pygame.draw.circle(screen, pygame.Color(255, 0, 0), (400, 300), 100)
    pygame.draw.circle(screen, pygame.Color(255, 255, 0), (10, 590), 10)

    pygame.display.update()
