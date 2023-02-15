import pygame



class Player(pygame.sprite.Sprite):
    def __init__(self, *groups,position):
        super().__init__(*groups)
        image = pygame.image.load('./assets/Frogman.png').convert_alpha()
        image = pygame.transform.scale(image, (64, 64))
        self.image = image
        self.rect = self.image.get_rect(topleft=position)

        # movement related things
        self.direction = pygame.math.Vector2(0,0)
        self.facing = 'up'

    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.direction.y = -1
            self.facing = 'up'
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
            self.facing = 'down'
        else:
            # Resets moving so we don't keep walking
            self.direction.y = 0

        if keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.facing = 'left'

        elif keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.facing = 'right'
        else:
            # Resets moving so we don't keep walking
            self.direction.x = 0
        
        # normalize tha movement vector
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

    def move(self):
        self.rect.center += self.direction * 5

    def update(self):
        self.input()
        self.move()