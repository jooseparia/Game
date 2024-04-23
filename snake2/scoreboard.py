import pygame.font

class Scoreboard:
    def __init__(self, game_display, game_settings):
        self.game_display = game_display
        self.game_settings = game_settings

    def display_score(self, score):
        value = self.game_settings.score_font.render("Your Score: " + str(score), True, self.game_settings.colors["yellow"])
        self.game_display.blit(value, [0, 0])