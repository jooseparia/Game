import pygame
import time
import random
from scoreboard import Scoreboard
from game_settings import GameSettings

class Game:
    def __init__(self):
        pygame.init()
        self.game_settings = GameSettings()
        self.game_display = pygame.display.set_mode((self.game_settings.dis_width, self.game_settings.dis_height))
        pygame.display.set_caption('Snake 2')
        self.clock = pygame.time.Clock()
        self.game_over = False

    def gameLoop(self):
        x1 = self.game_settings.dis_width / 2
        y1 = self.game_settings.dis_height / 2
        x1_change = 0
        y1_change = 0
        snake_List = []
        Length_of_snake = 1
        foodx = round(random.randrange(0, self.game_settings.dis_width - self.game_settings.snake_block) / 10.0) * 10.0
        foody = round(random.randrange(0, self.game_settings.dis_height - self.game_settings.snake_block) / 10.0) * 10.0

        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT and x1_change == 0:
                        x1_change = -self.game_settings.snake_block
                        y1_change = 0
                    elif event.key == pygame.K_RIGHT and x1_change == 0:
                        x1_change = self.game_settings.snake_block
                        y1_change = 0
                    elif event.key == pygame.K_UP and y1_change == 0:
                        y1_change = -self.game_settings.snake_block
                        x1_change = 0
                    elif event.key == pygame.K_DOWN and y1_change == 0:
                        y1_change = self.game_settings.snake_block
                        x1_change = 0

            if x1 >= self.game_settings.dis_width or x1 < 0 or y1 >= self.game_settings.dis_height or y1 < 0:
                self.game_over = True
            x1 += x1_change
            y1 += y1_change
            self.game_display.fill(self.game_settings.colors["black"])
            pygame.draw.rect(self.game_display, self.game_settings.colors["red"], [foodx, foody, self.game_settings.snake_block, self.game_settings.snake_block])
            snake_Head = []
            snake_Head.append(x1)
            snake_Head.append(y1)
            snake_List.append(snake_Head)
            if len(snake_List) > Length_of_snake:
                del snake_List[0]

            for x in snake_List[:-1]:
                if x == snake_Head:
                    self.game_over = True

            for x in snake_List:
                pygame.draw.rect(self.game_display, self.game_settings.colors["green"], [x[0], x[1], self.game_settings.snake_block, self.game_settings.snake_block])

            self.display_score(Length_of_snake - 1)
            pygame.display.update()

            if x1 == foodx and y1 == foody:
                foodx = round(random.randrange(0, self.game_settings.dis_width - self.game_settings.snake_block) / 10.0) * 10.0
                foody = round(random.randrange(0, self.game_settings.dis_height - self.game_settings.snake_block) / 10.0) * 10.0
                Length_of_snake += 1

            self.clock.tick(self.game_settings.snake_speed)

    def display_score(self, score):
        value = self.game_settings.score_font.render("Your Score: " + str(score), True, self.game_settings.colors["yellow"])
        self.game_display.blit(value, [0, 0])

    def run(self):
        self.gameLoop()
        pygame.quit()
        quit()

if __name__ == "__main__":
    game = Game()
    game.run()