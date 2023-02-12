import pygame

pygame.init()
font = pygame.font.Font(None, 30)


def debug(info, y=10, x=10):
    """
    A simple debug functionality that allows us to display variables and
    other information. in the top left corner of the screen
    :param info: Info to display on the left top corner of the screen.
    :param y: Location parameter
    :param x: Location parameter
    :return:
    """
    display_surface = pygame.display.get_surface()
    debug_surf = font.render(str(info), True, (255, 255, 255))
    debug_rect = debug_surf.get_rect(topleft=(x, y))
    pygame.draw.rect(display_surface, 'black', debug_rect)
    display_surface.blit(debug_surf, debug_rect)
