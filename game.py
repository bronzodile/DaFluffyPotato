import pygame
from cloud import Cloud

class Game:
    def __init__(self) -> None:
        pygame.init()

        pygame.display.set_caption('Super Ninja')
        self.screen = pygame.display.set_mode((640,480))
        self.clock = pygame.time.Clock()
        self.running = True
        self.myCloud = Cloud('data/images/clouds/cloud_1.png')
        

        self.collition_area = pygame.Rect(50,50,300,50)



    def run(self):
        while self.running:          

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.myCloud.movement[0] = True
                    if event.key == pygame.K_DOWN:
                        self.myCloud.movement[1] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        self.myCloud.movement[0] = False
                    if event.key == pygame.K_DOWN:
                        self.myCloud.movement[1] = False
            
            self.myCloud.move()
            if self.myCloud.boundRect.colliderect(self.collition_area):
                self.collition_area_colour = (0,100,255)
            else:
                self.collition_area_colour = (205,100,255)



            self.screen.fill((14,219,248))
            pygame.draw.rect(self.screen,self.collition_area_colour,self.collition_area)
            self.screen.blit(self.myCloud.img,self.myCloud.img_pos)            
            
            pygame.display.update()
            self.clock.tick(60)

Game().run()
