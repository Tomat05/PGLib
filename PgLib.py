import pygame

screen = pygame.display.set_mode([1, 1])

def createWindow(width, height):
    screen = pygame.display.set_mode([width, height])

def background(r, g, b):
    screen.fill((r, g, b))

# Easier to understand than just using a random tuple as with regular pygame functions
def colour(r, g, b, a=255):
    return (r, g, b, a)

def circle(centreX, centreY, radius, fill):
    pygame.draw.circle(screen, fill, (centreX, centreY), radius)