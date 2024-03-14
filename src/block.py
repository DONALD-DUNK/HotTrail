import pygame

class block:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = None

    def load_image(self, file, width, height):
        self.width = width
        self.height = height
        self.image = pygame.transform.scale(pygame.image.load(file), (width, height))

    def display(self, screen):
        if self.image:
            screen.blit(self.image, (self.x, self.y))
