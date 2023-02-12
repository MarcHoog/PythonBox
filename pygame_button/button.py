import pygame
import functools
import colors

image = pygame.image.load('./assets/boxie.png')

def get_8_percent(value):
    return value / 8

class MyButtonGroup(pygame.sprite.LayeredUpdates):
    def draw(self, surface):
        for sprite in self:
            sprite.draw(surface)
    
    def update(self):
        for sprite in self:
            sprite.update()

class Boxie(pygame.sprite.Sprite):
    # this sprite doesn't use shapes but instead uses a image
    def __init__(self, x, y,speed,distance = 30):
        super().__init__()
        self.surf = pygame.Surface((64, 64))
        self.image = image
        self.rect = self.surf.get_rect()
        
        self.rect.x = x
        self.rect.y = y
        self.distance = 30
        self.speed = speed

        self.base_x = self.rect.x
        self.max_x = self.rect.x + (self.distance * self.speed[0])
        
        # this is to make sure that the max_x is always greater than the base_x 
        # Otherwise the left side doesn't work
        if self.base_x > self.max_x:
            self.max_x, self.base_x = self.base_x, self.max_x
        
        #print(f'max_x = {self.max_x},base_x = {self.base_x}')

    def update(self):
        self.rect = self.rect.move(self.speed)
        if self.rect.x > self.max_x or self.rect.x < self.base_x:
            self.speed = [-x for x in self.speed]

            
        
    def draw(self,display):
        display.blit(self.image, self.rect)

class Animation:
    def __init__(self, object) -> None:
        
        
        self.object = object
        self.rect = object.image.get_rect()
        self.rect.x = object.x
        self.rect.y = object.y
        padding = 10

        self.ani_height = 64
        self.ani_width = 64

        self.rect.width += padding
        self.rect.height += padding
        self.ani_height += padding
        self.ani_width += padding
        self.corner_squares = []
        
        points = [[-1, -1],[1, -1],[-1, 1],[1, 1]]
        for point in points:
            width = self.rect.width
            height = self.rect.height
            
            if point[0] == -1:
                width = self.ani_width
            if point[1] == -1:
                height = self.ani_height
           
            x = self.rect.x + width * point[0]
            y = self.rect.y + height * point[1]

            self.corner_squares.append(Boxie(x,y,point))
    
    def update(self):
        for square in self.corner_squares:
            square.update()

    def draw(self, surface):
        for square in self.corner_squares:
            square.draw(surface)

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

        self.selected = False
        
        # make the back ground of the butto
        self.image = pygame.Surface((width, height))
        self.image.fill(colors.WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.image2 = pygame.Surface((width + get_8_percent(height), height + get_8_percent(height)))
        self.image2.fill(colors.GRAY)
        self.rect2 = self.image2.get_rect()
        self.rect2.x = x
        self.rect2.y = y

        self.image3 = pygame.Surface((width + get_8_percent(height) + 10, height + get_8_percent(height) + 10))
        self.image3.fill(colors.BLACK)
        self.rect3 = self.image3.get_rect()
        self.rect3.x = x - 5
        self.rect3.y = y - 5

        self.x = self.rect3.x
        self.y = self.rect3.y


        # make the text on the button and make sure it's centered
        self.font = pygame.font.Font('./font/joystix.ttf', 30)
        self.text = self.font.render(text, 1, text_color)
        self.text_rect = self.text.get_rect()
        self.text_rect.topleft = (x + (width/2 - self.text_rect.width/2), y + (height/2 - self.text_rect.height / 2))    
        self.animation = Animation(self)

    def _get_dimantions(self):
        return self.rect.x, self.rect.y, self.rect.width, self.rect.height

    def is_over(self, pos):
        x,y,width,height = self._get_dimantions()
        
        if pos[0] > x and pos[0] < x + width:
            if pos[1] > y and pos[1] < y + height:
                self.image2.fill(colors.WHITE)
                self.selected = True
                return True
        
        self.image.fill(colors.WHITE)
        self.image2.fill(colors.GRAY)
        self.selected = False
        return False

    def click(self):
        self.callback()
        
    def update(self):
        if self.selected:
            self.animation.update()

    def draw(self,surface):
        if self.selected:
            self.animation.draw(surface)

        surface.blit(self.image3, self.rect3)
        surface.blit(self.image2, self.rect2)
        surface.blit(self.image, self.rect)    
        surface.blit(self.text, self.text_rect)

