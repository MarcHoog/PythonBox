from statemachine import StateMachine
import pygame


class Entity(pygame.sprite.Sprite):
    "Base class for entities this class mostly handles collision and movement."
    def __init__(self, groups):
        super().__init__(groups)

        # Animation stuff
        self.frame_index = 0
        self.animation_speed = 0.15

        self.direction = pygame.math.Vector2()

        # Need to be initalized in child class
        self.obstacle_sprites = None
        self.hitbox = None
        self.rect = None

    def collision(self, direction):
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                # coliderect test if two rectangles overlapping
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0:  # move right
                        # If our player is moving to the right and they are overlapping with an
                        #   obstacle_sprites on the left
                        # then we move the right side of the player to the left part of the collision obstacle
                        self.hitbox.right = sprite.hitbox.left
                    elif self.direction.x < 0:  # move left
                        self.hitbox.left = sprite.hitbox.right

        elif direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0:  # move down
                        self.hitbox.bottom = sprite.hitbox.top
                    elif self.direction.y < 0:  # move up
                        self.hitbox.top = sprite.hitbox.bottom

    def movement(self, speed, multiplier: int = None):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        if multiplier:
            speed_multiplier = speed * multiplier
            speed += speed_multiplier

        self.hitbox.x += self.direction.x * speed
        self.collision('horizontal')
        self.hitbox.y += self.direction.y * speed
        self.collision('vertical')
        self.rect.center = self.hitbox.center
