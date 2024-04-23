import pygame
import time
import random

class GameSettings:
    def __init__(self):
        self.colors = {
            "white": (255, 255, 255),
            "yellow": (255, 255, 102),
            "black": (0, 0, 0),
            "red": (255, 10, 10),
            "green": (0, 255, 0),
            "blue": (50, 153, 213)
        }
        self.dis_width = 600
        self.dis_height = 400
        self.snake_block = 10
        self.snake_speed = 15
        self.font_style = pygame.font.SysFont("bahnschrift", 25)
        self.score_font = pygame.font.SysFont("comicsansms", 35)
        self.food_color = self.colors["red"]

#3