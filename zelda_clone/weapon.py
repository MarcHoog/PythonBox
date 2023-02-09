import pygame


# TODO just give these values Maybe??? instead of giving the full player
class WeaponSprite(pygame.sprite.Sprite):
    def __init__(self, player, groups):
        # TODO RESEARCH ASBOUT RECTANGLES
        super().__init__(groups)

        direction = player.facing
        # Graphic
        full_path = F'./assets/graphics/weapons/{player.weapon.equiped}/{direction}.png'
        self.image = pygame.image.load(full_path).convert_alpha()

        # placement
        if direction == 'right':
            self.rect = self.image.get_rect(midleft=player.rect.midright + pygame.math.Vector2(0, 16))
        elif direction == 'left':
            self.rect = self.image.get_rect(midright=player.rect.midleft + pygame.math.Vector2(0, 16))
        elif direction == 'down':
            self.rect = self.image.get_rect(midtop=player.rect.midbottom + pygame.math.Vector2(-10, 0))
        else:
            self.rect = self.image.get_rect(midbottom=player.rect.midtop + pygame.math.Vector2(-10, 0))
