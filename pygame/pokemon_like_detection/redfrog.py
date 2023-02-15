import pygame


class Redfrog(pygame.sprite.Sprite):
    def __init__(self, *groups,position):
        super().__init__(*groups)
        image = pygame.image.load('./assets/RedFrogman.png').convert_alpha()
        image = pygame.transform.scale(image, (64, 64))
        self.image = image
        self.rect = self.image.get_rect(topleft=position)

    def update(self):
        pass