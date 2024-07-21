import pygame

class Cloud:
    def __init__(self,path) -> None:
        self.img = pygame.image.load(path).convert()
        self.img_pos = [320,260]
        self.boundRect = self.img.get_rect()
        self.boundRect.update(self.img_pos[0],self.img_pos[1],self.boundRect.width,self.boundRect.height)
        self.img.set_colorkey((0,0,0))
        self.movement = [False,False]
        self.velocity = 5

    def move(self):
        if (self.movement[1] - self.movement[0]) != 0:
            self.img_pos[1] += (self.movement[1] - self.movement[0]) * self.velocity
            self.boundRect.update(self.img_pos[0],self.img_pos[1],self.boundRect.width,self.boundRect.height)
