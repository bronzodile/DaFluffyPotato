import pygame
from cloud import Cloud
from scripts.entities import PhysicsEntity
from scripts.utils import load_image

class Game:
    def __init__(self) -> None:
        pygame.init()

        pygame.display.set_caption('Super Ninja')
        self.screen = pygame.display.set_mode((640,480))
        self.gameSurface = pygame.Surface((320,240))
        self.clock = pygame.time.Clock()
        self.running = True

        self.movement = [0,0]
        self.assets = {
            'player': load_image('entities/player.png')
        }

        self.player = PhysicsEntity(self, 'player', (50, 50), (8,15))


    def run(self):
        while self.running:          

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = True
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = False
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = False         
 
            self.gameSurface.fill((14,219,248))
            self.player.update((self.movement[1] - self.movement[0],0))
            self.player.render(self.gameSurface)            
            
            self.screen.blit(pygame.transform.scale(self.gameSurface,self.screen.get_size()),(0,0))
            pygame.display.update()
            self.clock.tick(60)

Game().run()
