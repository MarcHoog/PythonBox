import pygame

# GLOBALS
def draw_text(
            text,
            font,
            color,
            surface,
            x,
            y):
    
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)



class Screen:

    def __init__(self):
        self.font = pygame.font.SysFont(None, 20)
        self.display = pygame.display.get_surface()

    def enter(self):
        pass

    def exit(self):
        pass

    def update(self):
        pass

    def __repr__(self):
        return f'{self.__class__.__name__}'

class MainMenu(Screen):
    
    def __init__(self):
        super().__init__()
        self.status = 'inactive'

    def update(self):
        self.display.fill((0, 0, 0))
        draw_text('main_menu',self.font,(255, 255, 255), self.display, 20, 20)

    def __repr__(self):
        return f'{self.__class__.__name__}'

class OptionMenu(Screen):
    
    def __init__(self):
        super().__init__()
        self.status = 'inactive'

    def update(self):
        self.display.fill((0, 0, 0))
        draw_text('option_menu',self.font,(255, 255, 255), self.display, 20, 20)

    def __repr__(self):
        return f'{self.__class__.__name__}'

class ScreenManager:

    def __init__(self,):
        screens = {
            'main_menu' : MainMenu,
            'option_screen' : OptionMenu
        }


        self.default_screen = screens['main_menu']

        self.current_screen = self.default_screen()
        self.current_screen.enter()

    def run(self):
        self.current_screen.update()
