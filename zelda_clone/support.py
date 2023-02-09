from csv import reader
from os import walk
import pygame


def import_csv_layout(path):
    """
    Import a csv layout file as map

    Parameters
    ----------
    path : str
        The path to the csv layout file.
    """
    with open(path, 'r') as level_map:
        terrain_map = []
        layout = reader(level_map, delimiter=',')
        for row in layout:
            terrain_map.append(list(row))
        return terrain_map


def import_graphics_from(path):
    # TODO consider returning a dictionary here for more control
    """
    Import a graphics file from a dictionary

    Parameters
    ----------
    path : str
        The path to the graphics file.
    :param path:
    :return:
    """

    surface_list = []

    for _, __, img_files in walk(path):
        for image in img_files:
            full_path = path + '/' + image
            image_surf = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surf)
    return surface_list


def import_player_animations(template):
    character_path = './assets/graphics/player/'
    for animation in template.keys():
        full_path = character_path + animation
        template[animation] = import_graphics_from(full_path)

    return template


if __name__ == "__main__":
    # result = import_csv_layout('./assets/map/map_FloorBlocks.csv')
    # print(result)
    print(import_graphics_from('./assets/graphics/grass'))
