import pygame
import sys


def main():
    # pre-define RGB colors for Pygame
    BLACK = pygame.Color("Black")
    WHITE = pygame.Color("White")
    IMAGE_SIZE = 470
    TEXT_HEIGHT = 30

    pygame.init()

    screen = pygame.display.set_mode((IMAGE_SIZE, IMAGE_SIZE + TEXT_HEIGHT))
    pygame.display.set_caption("Text, Sound, and an Image")

    image1 = pygame.image.load("2dogs.JPG")
    image1 = pygame.transform.scale(image1, (IMAGE_SIZE, IMAGE_SIZE))

    # print(pygame.font.get_fonts())   # See what fonts your computer has built in
    font1 = pygame.font.SysFont("comicsansms", 28)
    caption1 = font1.render("Two Dogs", True, BLACK)

    font2 = pygame.font.SysFont("phosphate", 80)
    caption2 = font2.render("Mine!", True, (255, 255, 255))

    dog_bark = pygame.mixer.Sound("bark.mp3")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                dog_bark.play()

        screen.fill(WHITE)
        screen.blit(image1, (0, 0))
        screen.blit(caption1, (screen.get_width() / 2 - caption1.get_width() / 2,
                               image1.get_height() - 4))
        screen.blit(caption2, (screen.get_width() / 2 - caption2.get_width(), 300))

        pygame.display.update()


main()


