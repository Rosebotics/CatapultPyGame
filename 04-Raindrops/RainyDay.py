import pygame
import sys
import time
import random
import hero_module


class Raindrop:
    def __init__(self, screen: pygame.Surface, x, y):
        """ Creates a Raindrop sprite that travels down at a random speed. """
        self.screen = screen
        self.x = x
        self.y = y
        self.speed = random.randint(5, 15)

    def move(self):
        """ Move the self.y value of the Raindrop down the screen (y increase) at the self.speed. """
        self.y += self.speed

    def off_screen(self):
        """ Returns true if the Raindrop y value is not shown on the screen, otherwise false. """
        return self.y > self.screen.get_height()

    def draw(self):
        """ Draws this sprite onto the screen. """
        pygame.draw.line(self.screen, pygame.Color("Blue"), (self.x, self.y),
                         (self.x, self.y + 5), 2)


class Cloud:
    def __init__(self, screen: pygame.Surface, x, y, image_filename):
        """ Creates a Cloud sprite that will produce Raindrop objects.  The cloud will be moving around. """
        # Done 24: Initialize this Cloud, as follows:
        #     - Store the screen.
        #     - Set the initial position of this Cloud to x and y.
        #     - Set the image of this Cloud to the given image filename.
        #     - Create a list for Raindrop objects as an empty list called raindrops.
        #   Use instance variables:
        #      screen  x  y  image   raindrops.
        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.image.load(image_filename)
        self.raindrops = []

    def draw(self):
        """ Draws this sprite onto the screen. """
        self.screen.blit(self.image, (self.x, self.y))

    def rain(self):
        """ Adds a Raindrop to the array of raindrops so that it looks like the Cloud is raining. """
        new_drop = Raindrop(self.screen,
                            random.randint(self.x, self.x + self.image.get_width()),
                            self.y + self.image.get_height())
        self.raindrops.append(new_drop)


def main():
    """ Main game loop that creates the sprite objects, controls interactions, and draw the screen. """
    pygame.init()
    pygame.display.set_caption("Rainy Day")
    screen = pygame.display.set_mode((1000, 600))

    clock = pygame.time.Clock()

    # test_drop = Raindrop(screen, 250, 10)
    mike = hero_module.Hero(screen, 200, 400, "Mike_umbrella.png",
                "Mike.png")
    alyssa = hero_module.Hero(screen, 700, 400, "Alyssa_umbrella.png",
                  "Alyssa.png")
    # Done 23: Make a Cloud, named cloud, with appropriate images, starting at position x=300 y=50.
    cloud = Cloud(screen, 300, 50, "another_cloud.png")

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_RIGHT]:
            cloud.x += 10
        if pressed_keys[pygame.K_LEFT]:
            cloud.x -= 10
        if pressed_keys[pygame.K_UP]:
            cloud.y -= 10
        if pressed_keys[pygame.K_DOWN]:
            cloud.y += 10

        screen.fill((255, 255, 255))

        # --- begin area of test_drop code that will be removed later
        # test_drop.move()
        # if test_drop.off_screen():
        #     test_drop.y = 10
        # test_drop.draw()

        # if mike.hit_by(test_drop):
        #     mike.last_hit_time = time.time()
        #     test_drop.x = 750
        #     test_drop.y = 10
        # if alyssa.hit_by(test_drop):
        #     alyssa.last_hit_time = time.time()
        #     test_drop.x = 250
        #     test_drop.y = 10
        # --- end area of test_drop code that will be removed later

        cloud.draw()

        # TODO 29: Remove the temporary testdrop code from this function and refactor it as follows:
        # TODO: Make the Cloud "rain", then:
        # TODO    For each Raindrop in the Cloud's list of raindrops:
            #       - move the Raindrop.
            #       - draw the Raindrop.
            # TODO  30: if the Hero (Mike or Alyssa) is hit by a Raindrop, set the Hero's last_time_hit to the current time.
            # Optional  - if the Raindrop is off the screen or hitting a Hero, remove it from the Cloud's list of raindrops.
        cloud.rain()
        for raindrop in cloud.raindrops:
            raindrop.move()
            raindrop.draw()
            if mike.hit_by(raindrop):
                mike.last_hit_time = time.time()
                cloud.raindrops.remove(raindrop)
            if alyssa.hit_by(raindrop):
                alyssa.last_hit_time = time.time()
                cloud.raindrops.remove(raindrop)
            if raindrop.off_screen():
                cloud.raindrops.remove(raindrop)

        # print(len(cloud.raindrops))


        mike.draw()
        alyssa.draw()
        pygame.display.update()


main()
