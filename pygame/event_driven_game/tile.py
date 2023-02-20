import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, *groups,x,y,color=(182, 0, 36)) -> None:
        super().__init__(*groups)
        self.image = pygame.Surface((32,32))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

