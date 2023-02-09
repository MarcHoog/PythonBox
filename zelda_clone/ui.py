import pygame
from settings import *


class UI:
    def __init__(self):
        pass

        # TODO CAN BE USED TO BETTER WEAPONS
        # general
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)

        # bar setup
        self.health_bar_rect = pygame.Rect(10, 10, HEALTH_BAR_WIDTH, BAR_HEIGHT)
        self.energy_bar_rect = pygame.Rect(10, 60, ENERGY_BAR_WIDTH, BAR_HEIGHT)

        # TODO WET 💦
        self.weapon_graphics = []
        for weapon in WEAPON_DATA.values():
            path = weapon['graphic']
            weapon = pygame.image.load(path).convert_alpha()
            self.weapon_graphics.append(weapon)

        self.magic_graphics = []
        for spell in MAGIC_DATA.values():
            path = spell['graphic']
            spell = pygame.image.load(path).convert_alpha()
            self.magic_graphics.append(spell)

    def show_bar(self, current, max_amount, bg_rect, color):
        # BG BAR
        pygame.draw.rect(self.display_surface, UI_BG_COLOR, bg_rect)

        ratio = current / max_amount
        current_width = bg_rect.width * ratio
        current_rect = bg_rect.copy()

        current_rect.width = current_width

        pygame.draw.rect(self.display_surface, color, current_rect)
        pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, bg_rect, 3)

    def show_exp(self, exp):
        text_surf = self.font.render(str(int(exp)), False, TEXT_COLOR)
        x = self.display_surface.get_width() - 20
        y = self.display_surface.get_height() - 20
        text_rect = text_surf.get_rect(bottomright=(x, y))

        pygame.draw.rect(self.display_surface, UI_BG_COLOR, text_rect.inflate(20, 20))
        self.display_surface.blit(text_surf, text_rect)
        pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, text_rect.inflate(20, 20), 4)

    def selection_box(self, left, top, can_switch):
        bg_rect = pygame.Rect(left, top, ITEM_BOX_SIZE, ITEM_BOX_SIZE)
        pygame.draw.rect(self.display_surface, UI_BG_COLOR, bg_rect)
        if can_switch:
            pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, bg_rect, 3)
        else:
            pygame.draw.rect(self.display_surface, UI_HIGHLIGHT_COLOR, bg_rect, 3)

        return bg_rect

    # TODO WET 💦
    def weapon_overlay(self, weapon_index, can_switched):
        bg_rect = self.selection_box(10, 630, can_switched)
        weapon_surf = self.weapon_graphics[weapon_index]
        weapon_rect = weapon_surf.get_rect(center=bg_rect.center)

        self.display_surface.blit(weapon_surf, weapon_rect)

    def magic_overlay(self, magic_index, can_switched):
        bg_rect = self.selection_box(130, 630, can_switched)
        magic_surf = self.magic_graphics[magic_index]
        magic_rect = magic_surf.get_rect(center=bg_rect.center)

        self.display_surface.blit(magic_surf, magic_rect)

    def display(self, player):
        self.show_bar(player.health, player.stats['health'], self.health_bar_rect, HEALTH_COLOR)
        self.show_bar(player.energy, player.stats['energy'], self.energy_bar_rect, ENERGY_COLOR)

        self.show_exp(player.exp)
        self.weapon_overlay(player.weapon.index, player.weapon_timer.is_done)
        self.magic_overlay(player.magic.index, player.magic_timer.is_done)
