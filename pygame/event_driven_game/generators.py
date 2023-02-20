from listeners import EventListerner
import pygame
from event_factory import EventFactory as event_factory
import sys

'''
Generators are functions that generate Events

'''

def get_input():
    '''
    Generates a movement event based on the input
    '''
    direction = pygame.math.Vector2(0,0)
    key = pygame.key.get_pressed()
    if key[pygame.K_UP]:
        direction.y = -1
    elif key[pygame.K_DOWN]:
        direction.y = 1
    elif key[pygame.K_LEFT]:
        direction.x = -1 
    elif key[pygame.K_RIGHT]:
        direction.x = 1
    
    
    #if direction.magnitude() != 0:
    #    direction = direction.normalize()
    
    if direction != (0,0):
        event_factory.send_movement(direction)
    

def get_pygame_events():
    '''
    Generartes pygame events when needed
    '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            event_factory.send_quit()