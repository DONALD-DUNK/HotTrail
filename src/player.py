# player.py
import pygame

class player:
    def __init__(self, x, y):
        self.x = int(x)  
        self.y = int(y)  
        self.image = pygame.Surface((50, 50), pygame.SRCALPHA)
        pygame.draw.ellipse(self.image, (255, 255, 255), (0, 0, 25, 25))

    def display(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, 50, 50)
