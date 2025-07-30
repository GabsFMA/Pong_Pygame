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

# Player class
class Player:
    def __init__(self, posx, posy, widht, height, speed, color):
        self.posx = posx
        self.posy = posy
        self.widht = widht
        self.height = height
        self.speed = speed
        self.color = color
        self.geekRect = pygame.Rect(self.posx, self.posy, self.widht, self.height)
        self.geek = pygame.draw.rect(screen, self.color, self.geekRect)

    def display(self):
        self.geek = pygame.draw.rect(screen, self.color, self.geekRect)

    def update(self, yFac):
        self.posy = self.posy + self.speed * yFac

        if self.posy < 0:
            self.posy = 0
        elif self.posy + self.height > HEIGHT:
            self.posy = HEIGHT - self.height

        self.geekRect = pygame.Rect(self.posx, self.posy, self.widht, self.height)

    def displayScore(self, text, score, x, y, color):
        text = font.render(text+str(score), True, color)
        textRect = text.get_rect()
        textRect.center = (x, y)

        screen.blit(text, textRect)
    
    def getRect(self):
        return self.geekRect
    
    
            