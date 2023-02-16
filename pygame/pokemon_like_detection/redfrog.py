import pygame
import datetime

class Redfrog(pygame.sprite.Sprite):
    def __init__(self, *groups,position):
        super().__init__(*groups)
        self.display = pygame.display.get_surface()

        image = pygame.image.load('./assets/RedFrogman.png').convert_alpha()
        image = pygame.transform.scale(image, (64, 64))
        self.image = image
        self.rect = self.image.get_rect(topleft=position)
        self.direction = pygame.math.Vector2(-1,0)

        self.los = 300

    def interact(self, player):
        pygame.draw.rect(self.display,'red',self.rect,1)
        if self.rect.colliderect(player.rect.inflate(10,10)):
            print("POP!")
            self.kill()