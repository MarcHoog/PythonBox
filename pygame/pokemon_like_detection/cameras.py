import pygame
from settings import CAMERA_BORDERS
from redfrog import Redfrog

class Camera(pygame.sprite.Group):
    def __init__(self,
                 display):
        
        
        super().__init__()
        self.display = display

        self.offset = pygame.math.Vector2(0,0)
        display_size = self.display.get_size()

        self.half_w = display_size[0] / 2
        self.half_h = display_size[1] / 2

        l = CAMERA_BORDERS['l']
        t = CAMERA_BORDERS['t']
        w = display_size[0] - (CAMERA_BORDERS['l'] + CAMERA_BORDERS['r'])
        h = display_size[1] - (CAMERA_BORDERS['t'] + CAMERA_BORDERS['b'])
        self.camera_rect = pygame.Rect(l,t,w,h)

    def box_target_camera(self,target):

        if target.rect.left < self.camera_rect.left:
            self.camera_rect.left = target.rect.left
        if target.rect.right > self.camera_rect.right:
            self.camera_rect.right = target.rect.right
        if target.rect.top < self.camera_rect.top:
            self.camera_rect.top = target.rect.top    
        if target.rect.bottom > self.camera_rect.bottom:
            self.camera_rect.bottom = target.rect.bottom


        self.offset.x = self.camera_rect.left - CAMERA_BORDERS['l']
        self.offset.y = self.camera_rect.top - CAMERA_BORDERS['t']

    def camera_draw(self,display,target):

        if target:
            self.box_target_camera(target)


        for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            display.blit(sprite.image, offset_pos)

    def interactables_update(self, player):
        player_vector = pygame.math.Vector2(player.rect.center)
        active_sprites = [sprite for sprite in self.sprites() if (
            player_vector - pygame.math.Vector2(sprite.rect.center)
            ).magnitude() < 400 and isinstance(sprite, Redfrog)]
        for sprite in active_sprites:
            sprite.interact(player)
        
