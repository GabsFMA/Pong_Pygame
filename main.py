import pygame 

pygame.init()

font = pygame.font.Font('freesansbold.ttf', 20)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

WIDHT = 800
HEIGHT = 900

screen = pygame.display.set_mode((WIDHT, HEIGHT))
pygame.display.set_caption("PONG")

clock = pygame.time.Clock()
FPS = 30