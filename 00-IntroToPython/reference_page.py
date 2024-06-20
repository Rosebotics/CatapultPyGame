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
