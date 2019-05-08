import pygame, sys

width = 640
heigh = 480

screen = pygame.display.set_mode((width, heigh))
screen.fill((0, 210, 211))
#rgb(0, 210, 211)
pygame.display.set_caption('Ciclo básico de pygame')

pygame.font.init()

gameOver = False
while not gameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True
            
    pygame.display.flip()
            
pygame.quit()
sys.exit()