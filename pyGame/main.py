# main.py
import pygame
from game import gameLoop

pygame.init()

dis_width = 600
dis_height = 400
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()
snake_block = 10
snake_speed = 10

gameLoop(dis_width, dis_height, dis, pygame, clock, snake_block, snake_speed)
