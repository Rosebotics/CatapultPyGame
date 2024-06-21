# Boilerplate (ExampleGameLoop)
# import pygame
# import sys
#
# pygame.init()
# pygame.display.set_caption("Hello David Fisher")
# screen = pygame.display.set_mode((800, 600))
#
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()
#
#     screen.fill(pygame.Color("Gray"))
#     ... More drawing and putting images on the screen (and stuff)
#     pygame.display.update()

# Drawing (MovingSmile)
# API --> pygame.draw.circle(screen, (r,g,b), (x, y), radius, thickness)
# pygame.draw.circle(screen, pygame.Color(80, 0, 0), (320, 245), 10)
# API --> pygame.draw.rect(screen, (r,g,b), (x, y, width, height), thickness)
# pygame.draw.rect(screen, pygame.Color(0, 0, 0), (230, 320, 180, 30))

# Images (DogBark)
# before the loop --> image1 = pygame.image.load("2dogs.JPG")
# later --> screen.blit(image1, (0, 0))

# Text (DogBark)
# font2 = pygame.font.SysFont("phosphate", 80)
# caption2 = font2.render("Mine!", True, (255, 255, 255))
# screen.blit(caption2, (100, 300))

# Sound Effects (DogBark)
# dog_bark = pygame.mixer.Sound("bark.mp3")
# dog_bark.play()

# Getting the mouse position
# if event.type == pygame.MOUSEBUTTONDOWN:
# print(f"You clicked at {pygame.mouse.get_pos()}")

# Background music
# pygame.mixer.music.load("drums.wav")
# pygame.mixer.music.play(-1)
# pygame.mixer.music.stop()

# OOP --> Make sprite classes
# Objects know stuff (instance variables)
# Objects can do stuff (methods)
# Example:
#   to make an object (instance) of a class call the constructor
# class Hero:
#     def __init__(self, screen: pygame.Surface, x, y, with_umbrella_filename, without_umbrella_filename):
#         """ Creates a Hero sprite (Mike) that does not move. If hit by rain he'll put up his umbrella. """
#         self.screen = screen
#         self.x = x
#         self.y = y
#         self.image_umbrella = pygame.image.load(with_umbrella_filename)
#         self.image_no_umbrella = pygame.image.load(without_umbrella_filename)
#         self.last_hit_time = 0
