import pygame, sys
import random


class Runner():
    __customes = ('smallball', 'smallball1', 'smallball2', 'smallball3', 'smallball4')
    
    
    def __init__(self, x=0, y=0):
        
        ixCustome = random.randint(0,4)
        self.custome = pygame.image.load('imagenes/{}.png'.format(self.__customes[ixCustome]))
        self.position = [x, y]
        self.name = ""
    
    def avanzar(self):
        self.position[0] += random.randint(1, 6)
        


class Game():
    runners = []
    __posY = (185,245,300,355)
    __names = ('speedy', 'flash', 'thor', 'stark')
    __startLine = -25
    __finishLine = 620
    
#    Constructor
    def __init__(self):
        self.__screen = pygame.display.set_mode((640,480))
#        self.__screen.fill((192, 57, 43))
        self.__background = pygame.image.load('imagenes/background.png')
        pygame.display.set_caption('Carrera de bichos')
        
#        Creación de corredores
        for i in range(4):
            theRunner = Runner(self.__startLine, self.__posY[i])
            theRunner.name = self.__names[i]
            self.runners.append(theRunner)
        
    def close(self):
        pygame.quit()
        sys.exit()
    
    
    def competir(self):
        gameOver = False
        while not gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = True
            
            for activeRunner in self.runners:
                activeRunner.avanzar()
                if activeRunner.position[0] >= self.__finishLine:
                    print('{} Ha ganado'.format(activeRunner.name))
                    gameOver = True
            
            self.__screen.blit(self.__background, (0,0))
            
            for runner in self.runners:
                self.__screen.blit(runner.custome, runner.position)
                
            pygame.display.flip()
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.close()
        
    
if __name__ == '__main__':
    game = Game()
    pygame.font.init()
    game.competir()