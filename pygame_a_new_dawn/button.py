import pygame
import functools
import colors

class MyButtonGroup(pygame.sprite.LayeredUpdates):
    def draw(self, surface):
        for sprite in self:
            sprite.draw(surface)

class Button(pygame.sprite.Sprite):
    def __init__(self, 
                    x, 
                    y, 
                    width, 
                    height, 
                    text, 
                    color, 
                    text_color,
                    group,
                    callback,
                    *args,
                    **kwargs
                    ):
        
        super().__init__(group)

        self.color = color
        self.callback = callback
        self.callback = functools.partial(self.callback, *args, **kwargs)

        
        # make the back ground of the button
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        # make the text on the button and make sure it's centered
        self.font = pygame.font.SysFont('comicsans', 30)
        self.text = self.font.render(text, 1, text_color)
        self.text_rect = self.text.get_rect()
        self.text_rect.topleft = (x + (width/2 - self.text_rect.width/2), y + (height/2 - self.text_rect.height / 2))


    def _get_dimantions(self):
        return self.rect.x, self.rect.y, self.rect.width, self.rect.height

    def is_over(self, pos):
        x,y,width,height = self._get_dimantions()
        
        if pos[0] > x and pos[0] < x + width:
            if pos[1] > y and pos[1] < y + height:
                self.image.fill((255,0,0))
                return True
        
        if not self.is_over:
            self.image.fill(self.color)
            return False

    def click(self):
        self.callback()
        
    def update(self):
        pass

    def draw(self,surface):
        surface.blit(self.image, self.rect)    
        surface.blit(self.text, self.text_rect)